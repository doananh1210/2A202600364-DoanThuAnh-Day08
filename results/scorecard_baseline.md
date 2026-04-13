# Scorecard: baseline_dense

**Generated:** 2026-04-13 19:31
**Config:** baseline_dense

## Average Scores

| Metric | Score |
|--------|-------|
| Faithfulness | 5.00/5 |
| Relevance | 3.80/5 |
| Context Recall | 5.00/5 |
| Completeness | 3.60/5 |

## Per-Question Results

| ID | Category | F | R | Rc | C | Answer Preview |
|---|---|---|---|---|---|---|
| q01 | SLA | 5 | 5 | 5 | 3 | SLA xử lý ticket P1 là 4 giờ [1]. |
| q02 | Refund | 5 | 5 | 5 | 5 | Khách hàng có thể yêu cầu hoàn tiền trong vòng 7 ngày làm việc kể từ thời điểm x |
| q03 | Access Control | 5 | 5 | 5 | 5 | Để cấp quyền Level 3, cần phải được phê duyệt bởi Line Manager, IT Admin và IT S |
| q04 | Refund | 5 | 5 | 5 | 5 | Sản phẩm thuộc danh mục hàng kỹ thuật số như license key, subscription không đượ |
| q05 | IT Helpdesk | 5 | 5 | 5 | 5 | Tài khoản sẽ bị khóa sau 5 lần đăng nhập sai liên tiếp [1]. |
| q06 | SLA | 5 | 5 | 5 | 4 | Escalation trong sự cố P1 sẽ tự động escalate lên Senior Engineer nếu không có p |
| q07 | Access Control | 5 | 1 | 5 | 1 | Không đủ dữ liệu trong tài liệu hiện có để trả lời câu hỏi này. |
| q08 | HR Policy | 5 | 5 | 5 | 4 | Nhân viên sau probation period có thể làm remote tối đa 2 ngày/tuần [1]. |
| q09 | Insufficient Context | 5 | 1 | None | 3 | Không đủ dữ liệu trong tài liệu hiện có để trả lời câu hỏi này. |
| q10 | Refund | 5 | 1 | 5 | 1 | Không đủ dữ liệu trong tài liệu hiện có để trả lời câu hỏi này. |

## Detailed Notes

### [q01] SLA xử lý ticket P1 là bao lâu?

**Answer:** SLA xử lý ticket P1 là 4 giờ [1].

- Faithfulness (5): Thông tin trong câu trả lời hoàn toàn xuất phát từ tài liệu retrieved
- Relevance (5): Câu trả lời đã trực tiếp và đầy đủ giải quyết trọng tâm của câu hỏi.
- Context Recall (5): Recall=100% (1/1)
- Completeness (3): Câu trả lời đã đề cập đến thời gian xử lý ticket P1 là 4 giờ nhưng thiếu thông tin về SLA phản hồi ban đầu là 15 phút.

### [q02] Khách hàng có thể yêu cầu hoàn tiền trong bao nhiêu ngày?

**Answer:** Khách hàng có thể yêu cầu hoàn tiền trong vòng 7 ngày làm việc kể từ thời điểm xác nhận đơn hàng [1].

- Faithfulness (5): Tất cả thông tin trong câu trả lời đều xuất phát từ tài liệu đã được truy xuất.
- Relevance (5): Câu trả lời đã cung cấp thông tin cụ thể và đầy đủ về thời gian khách hàng có thể yêu cầu hoàn tiền.
- Context Recall (5): Recall=100% (1/1)
- Completeness (5): Câu trả lời đã bao gồm đầy đủ thông tin quan trọng, không thiếu sót chi tiết nào so với câu trả lời mong đợi.

### [q03] Ai phải phê duyệt để cấp quyền Level 3?

**Answer:** Để cấp quyền Level 3, cần phải được phê duyệt bởi Line Manager, IT Admin và IT Security [2].

- Faithfulness (5): Tất cả thông tin trong câu trả lời đều xuất phát từ tài liệu đã được truy xuất.
- Relevance (5): Câu trả lời đã nêu rõ những người cần phê duyệt để cấp quyền Level 3, trả lời trực tiếp và đầy đủ cho câu hỏi.
- Context Recall (5): Recall=100% (1/1)
- Completeness (5): Câu trả lời đã bao gồm đầy đủ tất cả các thông tin quan trọng.

### [q04] Sản phẩm kỹ thuật số có được hoàn tiền không?

**Answer:** Sản phẩm thuộc danh mục hàng kỹ thuật số như license key, subscription không được hoàn tiền [1].

- Faithfulness (5): Tất cả thông tin trong câu trả lời đều xuất phát từ tài liệu đã được truy xuất.
- Relevance (5): Câu trả lời đã trực tiếp và đầy đủ giải quyết trọng tâm của câu hỏi.
- Context Recall (5): Recall=100% (1/1)
- Completeness (5): Câu trả lời đã bao gồm đầy đủ thông tin quan trọng, không bỏ sót chi tiết nào so với câu trả lời mong đợi.

### [q05] Tài khoản bị khóa sau bao nhiêu lần đăng nhập sai?

**Answer:** Tài khoản sẽ bị khóa sau 5 lần đăng nhập sai liên tiếp [1].

- Faithfulness (5): Tất cả thông tin trong câu trả lời đều xuất phát từ tài liệu đã được truy xuất.
- Relevance (5): Câu trả lời đã cung cấp thông tin cụ thể và chính xác về số lần đăng nhập sai tối đa trước khi tài khoản bị khóa.
- Context Recall (5): Recall=100% (1/1)
- Completeness (5): Câu trả lời đã bao gồm đầy đủ thông tin cần thiết, không thiếu sót chi tiết nào so với câu trả lời mong đợi.

### [q06] Escalation trong sự cố P1 diễn ra như thế nào?

**Answer:** Escalation trong sự cố P1 sẽ tự động escalate lên Senior Engineer nếu không có phản hồi trong 10 phút [2].

- Faithfulness (5): Tất cả thông tin trong câu trả lời đều xuất phát từ context đã được trích xuất.
- Relevance (5): Câu trả lời đã trực tiếp và đầy đủ giải quyết trọng tâm của câu hỏi, đưa ra thông tin về quy trình escalation trong sự cố P1.
- Context Recall (5): Recall=100% (1/1)
- Completeness (4): Câu trả lời đã bao gồm thông tin về việc escalate lên Senior Engineer và thời gian 10 phút. Tuy nhiên, nó thiếu chi tiết về việc thời gian 10 phút được tính từ khi tạo ticket.

### [q07] Approval Matrix để cấp quyền hệ thống là tài liệu nào?

**Answer:** Không đủ dữ liệu trong tài liệu hiện có để trả lời câu hỏi này.

- Faithfulness (5): Câu trả lời không đưa ra bất kỳ thông tin cụ thể nào, do đó không có thông tin nào không xuất phát từ tài liệu retrieved.
- Relevance (1): Câu trả lời không cung cấp thông tin về Approval Matrix để cấp quyền hệ thống là tài liệu nào.
- Context Recall (5): Recall=100% (1/1)
- Completeness (1): Câu trả lời không cung cấp bất kỳ thông tin nào về 'Approval Matrix for System Access' hoặc 'Access Control SOP'.

### [q08] Nhân viên được làm remote tối đa mấy ngày mỗi tuần?

**Answer:** Nhân viên sau probation period có thể làm remote tối đa 2 ngày/tuần [1].

- Faithfulness (5): Tất cả thông tin trong câu trả lời đều xuất phát từ tài liệu retrieved.
- Relevance (5): Câu trả lời đã trực tiếp và đầy đủ giải quyết trọng tâm của câu hỏi.
- Context Recall (5): Recall=100% (1/1)
- Completeness (4): Câu trả lời đã đưa ra thông tin về số ngày làm remote tối đa trong tuần nhưng thiếu thông tin về việc cần được Team Lead phê duyệt.

### [q09] ERR-403-AUTH là lỗi gì và cách xử lý?

**Answer:** Không đủ dữ liệu trong tài liệu hiện có để trả lời câu hỏi này.

- Faithfulness (5): Câu trả lời không cung cấp thông tin cụ thể nào nên không có thông tin nào không trung thực so với ngữ cảnh.
- Relevance (1): Câu trả lời không cung cấp thông tin về lỗi ERR-403-AUTH và cách xử lý nó.
- Context Recall (None): No expected sources (abstain question)
- Completeness (3): Câu trả lời đã nêu rõ không tìm thấy thông tin về lỗi ERR-403-AUTH nhưng thiếu thông tin về việc lỗi có thể liên quan đến xác thực và gợi ý liên hệ IT Helpdesk.

### [q10] Nếu cần hoàn tiền khẩn cấp cho khách hàng VIP, quy trình có khác không?

**Answer:** Không đủ dữ liệu trong tài liệu hiện có để trả lời câu hỏi này.

- Faithfulness (5): Câu trả lời không đưa ra bất kỳ thông tin nào không có trong ngữ cảnh đã được truy xuất.
- Relevance (1): Câu trả lời không cung cấp thông tin về quy trình hoàn tiền khẩn cấp cho khách hàng VIP.
- Context Recall (5): Recall=100% (1/1)
- Completeness (1): Câu trả lời không cung cấp bất kỳ thông tin nào về quy trình hoàn tiền, dù cho khách hàng VIP hay không, trong khi câu trả lời mong đợi đề cập đến quy trình tiêu chuẩn áp dụng cho tất cả khách hàng.

