"""
rag_answer.py — Sprint 2 + 3: Retrieval & Grounded Answer (HOÀN CHỈNH)
=======================================================================
Sprint 2: Dense retrieval + Grounded answer với citation
Sprint 3: Hybrid retrieval (Dense + BM25/RRF) + Cross-encoder rerank

Chạy:  python rag_answer.py
"""

import os
import re
import json
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from dotenv import load_dotenv

load_dotenv()

# =============================================================================
# CONFIG
# =============================================================================
CHROMA_DB_DIR = Path(__file__).parent / "chroma_db"
COLLECTION_NAME = "rag_lab"

TOP_K_SEARCH = 10    # Retrieval rộng: lấy 10 candidates
TOP_K_SELECT = 3     # Đưa vào prompt: top 3 sau rerank/select

LLM_PROVIDER = "openai"
LLM_MODEL = "gpt-4"
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

# Cache objects
_chroma_collection = None
_bm25_index = None
_bm25_chunks = None
_rerank_model = None


# =============================================================================
# CHROMADB CONNECTION
# =============================================================================
def get_collection():
    """Lấy ChromaDB collection (Singleton)."""
    global _chroma_collection
    if _chroma_collection is not None:
        return _chroma_collection

    import chromadb
    client = chromadb.PersistentClient(path=str(CHROMA_DB_DIR))
    _chroma_collection = client.get_collection(COLLECTION_NAME)
    return _chroma_collection


# =============================================================================
# SPRINT 2: DENSE RETRIEVAL
# =============================================================================
def retrieve_dense(query: str, top_k: int = TOP_K_SEARCH) -> List[Dict[str, Any]]:
    """
    Dense retrieval: Embed query → tìm top-k chunks gần nhất trong ChromaDB.
    Score = 1 - distance (ChromaDB cosine distance).
    """
    from index import get_embedding

    collection = get_collection()
    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )

    chunks = []
    for doc, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        chunks.append({
            "text": doc,
            "metadata": meta,
            "score": round(1 - dist, 4),  # Convert distance → similarity
        })

    return chunks


# =============================================================================
# SPRINT 3: SPARSE RETRIEVAL (BM25)
# =============================================================================
def _build_bm25_index():
    """Build BM25 index từ tất cả chunks trong ChromaDB (lần đầu)."""
    global _bm25_index, _bm25_chunks
    if _bm25_index is not None:
        return _bm25_index, _bm25_chunks

    from rank_bm25 import BM25Okapi

    collection = get_collection()
    all_data = collection.get(include=["documents", "metadatas"])

    _bm25_chunks = []
    corpus = []

    for doc_id, doc, meta in zip(
        all_data["ids"], all_data["documents"], all_data["metadatas"]
    ):
        _bm25_chunks.append({
            "id": doc_id,
            "text": doc,
            "metadata": meta,
        })
        # Tokenize đơn giản: lowercase + split theo khoảng trắng và dấu câu
        tokens = re.findall(r'\w+', doc.lower())
        corpus.append(tokens)

    _bm25_index = BM25Okapi(corpus)
    return _bm25_index, _bm25_chunks


def retrieve_sparse(query: str, top_k: int = TOP_K_SEARCH) -> List[Dict[str, Any]]:
    """
    Sparse retrieval: BM25 keyword search.
    Mạnh ở: mã lỗi (ERR-403), tên riêng (P1), exact keyword.
    """
    bm25, chunks = _build_bm25_index()

    tokens = re.findall(r'\w+', query.lower())
    scores = bm25.get_scores(tokens)

    # Sort by score descending
    ranked_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)

    results = []
    for idx in ranked_indices[:top_k]:
        if scores[idx] > 0:
            chunk = chunks[idx]
            results.append({
                "text": chunk["text"],
                "metadata": chunk["metadata"],
                "score": round(float(scores[idx]), 4),
            })

    return results


# =============================================================================
# SPRINT 3: HYBRID RETRIEVAL (RRF)
# =============================================================================
def retrieve_hybrid(
    query: str,
    top_k: int = TOP_K_SEARCH,
    dense_weight: float = 0.6,
    sparse_weight: float = 0.4,
) -> List[Dict[str, Any]]:
    """
    Hybrid retrieval: Dense + BM25 gộp bằng Reciprocal Rank Fusion (RRF).
    RRF_score(doc) = w_dense / (60 + rank_dense) + w_sparse / (60 + rank_sparse)
    """
    K = 60  # Hằng số RRF chuẩn

    # Lấy kết quả từ cả 2 nguồn
    dense_results = retrieve_dense(query, top_k=top_k)
    sparse_results = retrieve_sparse(query, top_k=top_k)

    # Xây dict: text → chunk info + RRF score
    fusion = {}  # key: text[:100] (để tránh trùng)

    def chunk_key(chunk):
        return chunk["text"][:100]

    # Dense scores
    for rank, chunk in enumerate(dense_results):
        key = chunk_key(chunk)
        if key not in fusion:
            fusion[key] = {
                "text": chunk["text"],
                "metadata": chunk["metadata"],
                "rrf_score": 0,
                "dense_rank": rank + 1,
                "sparse_rank": None,
            }
        fusion[key]["rrf_score"] += dense_weight / (K + rank + 1)
        fusion[key]["dense_rank"] = rank + 1

    # Sparse scores
    for rank, chunk in enumerate(sparse_results):
        key = chunk_key(chunk)
        if key not in fusion:
            fusion[key] = {
                "text": chunk["text"],
                "metadata": chunk["metadata"],
                "rrf_score": 0,
                "dense_rank": None,
                "sparse_rank": rank + 1,
            }
        fusion[key]["rrf_score"] += sparse_weight / (K + rank + 1)
        fusion[key]["sparse_rank"] = rank + 1

    # Sort by RRF score
    sorted_chunks = sorted(fusion.values(), key=lambda x: x["rrf_score"], reverse=True)

    results = []
    for item in sorted_chunks[:top_k]:
        results.append({
            "text": item["text"],
            "metadata": item["metadata"],
            "score": round(item["rrf_score"], 4),
        })

    return results


# =============================================================================
# SPRINT 3: RERANKING (Cross-Encoder)
# =============================================================================
def rerank(
    query: str,
    candidates: List[Dict[str, Any]],
    top_k: int = TOP_K_SELECT,
) -> List[Dict[str, Any]]:
    """
    Rerank bằng Cross-Encoder: chấm lại từng cặp (query, chunk).
    Chính xác hơn Bi-Encoder (dùng khi embed) nhưng chậm hơn.

    Funnel: Search rộng (top-10) → Rerank → Select (top-3)
    """
    global _rerank_model

    if _rerank_model is None:
        from sentence_transformers import CrossEncoder
        print("  Loading Cross-Encoder reranker (lần đầu)...")
        _rerank_model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
        print("  ✓ Reranker loaded!")

    # Tạo pairs (query, chunk_text) để cross-encoder chấm
    pairs = [[query, chunk["text"]] for chunk in candidates]
    scores = _rerank_model.predict(pairs)

    # Gắn score mới và sort
    scored = list(zip(candidates, scores))
    scored.sort(key=lambda x: x[1], reverse=True)

    results = []
    for chunk, score in scored[:top_k]:
        results.append({
            "text": chunk["text"],
            "metadata": chunk["metadata"],
            "score": round(float(score), 4),
        })

    return results


# =============================================================================
# SPRINT 2: CONTEXT BLOCK + GROUNDED PROMPT
# =============================================================================
def build_context_block(chunks: List[Dict[str, Any]]) -> str:
    """
    Đóng gói chunks thành context block có đánh số [1], [2], [3]...
    Mỗi chunk có header gồm: source, section, score.
    """
    parts = []
    for i, chunk in enumerate(chunks, 1):
        meta = chunk.get("metadata", {})
        source = meta.get("source", "unknown")
        section = meta.get("section", "")
        date = meta.get("effective_date", "")
        score = chunk.get("score", 0)
        text = chunk.get("text", "")

        header = f"[{i}] {source}"
        if section:
            header += f" | {section}"
        if date and date != "unknown":
            header += f" | effective: {date}"
        header += f" | score={score:.2f}"

        parts.append(f"{header}\n{text}")

    return "\n\n".join(parts)


def build_grounded_prompt(query: str, context_block: str) -> str:
    """
    Grounded prompt với 4 quy tắc vàng:
    1. Evidence-only: Chỉ trả lời từ context
    2. Abstain: Thiếu context → "Không đủ dữ liệu"
    3. Citation: Gắn [1], [2]... khi trích dẫn
    4. Short, clear, stable: Ngắn, rõ, nhất quán
    """
    return f"""Bạn là trợ lý nội bộ của khối CS + IT Helpdesk. Hãy trả lời câu hỏi DỰA TRÊN CÁC TÀI LIỆU ĐÃ ĐƯỢC TRUY XUẤT bên dưới.

QUY TẮC BẮT BUỘC:
1. CHỈ trả lời từ ngữ cảnh (context) bên dưới. KHÔNG được dùng kiến thức bên ngoài.
2. Nếu ngữ cảnh KHÔNG ĐỦ để trả lời, hãy nói rõ: "Không đủ dữ liệu trong tài liệu hiện có để trả lời câu hỏi này."
3. Trích dẫn nguồn bằng số trong ngoặc vuông [1], [2], [3] tương ứng với từng đoạn context.
4. Trả lời ngắn gọn, rõ ràng, đúng trọng tâm câu hỏi. Dùng tiếng Việt.

Câu hỏi: {query}

Tài liệu truy xuất được:
{context_block}

Trả lời:"""


# =============================================================================
# SPRINT 2: LLM CALL
# =============================================================================
def call_llm(prompt: str) -> str:
    """
    Gọi LLM để sinh câu trả lời.
    Hỗ trợ cả OpenAI và Google Gemini.
    Temperature = 0 để output ổn định cho evaluation.
    """
    if LLM_PROVIDER == "openai":
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=512,
        )
        return response.choices[0].message.content.strip()

    elif LLM_PROVIDER == "gemini":
        import google.generativeai as genai
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        model = genai.GenerativeModel(GEMINI_MODEL)
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=0,
                max_output_tokens=512,
            )
        )
        return response.text.strip()

    else:
        raise ValueError(f"LLM_PROVIDER không hợp lệ: {LLM_PROVIDER}. Dùng 'openai' hoặc 'gemini'.")


# =============================================================================
# RAG PIPELINE
# =============================================================================
def rag_answer(
    query: str,
    retrieval_mode: str = "dense",
    top_k_search: int = TOP_K_SEARCH,
    top_k_select: int = TOP_K_SELECT,
    use_rerank: bool = False,
    verbose: bool = False,
    rerank_mode: Optional[str] = None,
    top_k: int = TOP_K_SELECT,
) -> Dict[str, Any]:
    """
    RAG pipeline: Retrieve → Rerank (optional) → Build prompt → Call LLM.
    """
    # Step 1: Retrieve
    if retrieval_mode == "dense":
        candidates = retrieve_dense(query, top_k=TOP_K_SEARCH)
    elif retrieval_mode == "sparse":
        candidates = retrieve_sparse(query, top_k=TOP_K_SEARCH)
    elif retrieval_mode == "hybrid":
        candidates = retrieve_hybrid(query, top_k=TOP_K_SEARCH)
    else:
        raise ValueError(f"retrieval_mode không hợp lệ: {retrieval_mode}")

    # Check for no candidates (Abstain case)
    if not candidates:
        return {
            "answer": "Không đủ dữ liệu trong tài liệu hiện có để trả lời câu hỏi này.",
            "sources": [],
            "chunks_used": [],
            "config": {
                "retrieval_mode": retrieval_mode,
                "top_k_search": top_k_search,
                "top_k_select": top_k_select,
                "use_rerank": use_rerank,
            }
        }

    # Step 2: Rerank (optional)
    if use_rerank:
        candidates = rerank(query, candidates, top_k=top_k_select)

    # Limit candidates to top_k_select
    candidates = candidates[:top_k_select]

    # Step 3: Build grounded prompt
    context_block = build_context_block(candidates)
    prompt = build_grounded_prompt(query, context_block)

    # Step 4: Call LLM
    answer = call_llm(prompt)

    # Step 5: Return answer + sources
    sources = [chunk["metadata"] for chunk in candidates]
    return {
        "answer": answer,
        "sources": sources,
        "chunks_used": candidates,
        "config": {
            "retrieval_mode": retrieval_mode,
            "top_k_search": top_k_search,
            "top_k_select": top_k_select,
            "use_rerank": use_rerank,
        }
    }


# =============================================================================
# COMPARISON (Sprint 3)
# =============================================================================
def compare_retrieval_strategies(query: str) -> None:
    """So sánh Dense vs Hybrid vs Hybrid+Rerank trên cùng 1 câu hỏi."""
    configs = [
        {"label": "Dense (baseline)", "retrieval_mode": "dense", "use_rerank": False},
        {"label": "Hybrid (RRF)", "retrieval_mode": "hybrid", "use_rerank": False},
    ]  # Removed Hybrid + Rerank to follow A/B rule

    results_log = []

    for cfg in configs:
        print(f"\n--- {cfg['label']} ---")
        try:
            result = rag_answer(
                query,
                retrieval_mode=cfg["retrieval_mode"],
                use_rerank=cfg["use_rerank"],
                verbose=False,
            )
            print(f"Answer: {result['answer'][:200]}")
            print(f"Sources: {result['sources']}")

            # Log results
            results_log.append({
                "Query": query,
                "Variant": cfg["label"],
                "Answer": result["answer"],
                "Sources": result["sources"],
            })
        except Exception as e:
            print(f"Lỗi: {e}")

    # Save comparison log to file
    with open("comparison_log.json", "w", encoding="utf-8") as f:
        json.dump(results_log, f, ensure_ascii=False, indent=4)


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Sprint 2 + 3: RAG Answer Pipeline")
    print("=" * 60)

    # Test queries
    test_queries = [
        "SLA xử lý ticket P1 là bao lâu?",
        "Khách hàng có thể yêu cầu hoàn tiền trong bao nhiêu ngày?",
        "Ai phải phê duyệt để cấp quyền Level 3?",
        "ERR-403-AUTH là lỗi gì?",  # Câu không có trong docs → test abstain
    ]

    print("\n--- Sprint 2: Dense Baseline ---")
    for q in test_queries:
        print(f"\n{'─'*50}")
        print(f"Q: {q}")
        try:
            result = rag_answer(q, retrieval_mode="dense", verbose=True)
            print(f"\nA: {result['answer']}")
            print(f"Sources: {result['sources']}")

            # Verify citation in the answer
            if "[1]" not in result["answer"] and result["sources"]:
                print("Warning: Answer does not contain expected citation [1].")
        except Exception as e:
            print(f"Lỗi: {e}")

    print(f"\n\n{'='*60}")
    print("--- Sprint 3: So sánh Dense vs Hybrid vs Hybrid+Rerank ---")
    compare_retrieval_strategies("SLA xử lý ticket P1 là bao lâu?")
    compare_retrieval_strategies("Approval Matrix cấp quyền cho ai?")
