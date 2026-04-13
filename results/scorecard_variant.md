# Scorecard: variant_hybrid_rerank

**Generated:** 2026-04-13 19:33
**Config:** variant_hybrid_rerank

## Average Scores

| Metric | Score |
|--------|-------|
| Faithfulness | 5.00/5 |
| Relevance | 3.80/5 |
| Context Recall | 5.00/5 |
| Completeness | 3.80/5 |

## Per-Question Results

| ID | Category | F | R | Rc | C | Answer Preview |
|---|---|---|---|---|---|---|
| q01 | SLA | 5 | 5 | 5 | 4 | SLA xử lý ticket P1 là 4 giờ [1]. |
| q02 | Refund | 5 | 5 | 5 | 5 | Khách hàng có thể yêu cầu hoàn tiền trong vòng 7 ngày làm việc kể từ thời điểm x |
| q03 | Access Control | 5 | 5 | 5 | 5 | Để cấp quyền Level 3, cần phải được phê duyệt bởi Line Manager, IT Admin và IT S |
| q04 | Refund | 5 | 5 | 5 | 5 | Không, sản phẩm thuộc danh mục hàng kỹ thuật số như license key, subscription kh |
| q05 | IT Helpdesk | 5 | 5 | 5 | 5 | Tài khoản sẽ bị khóa sau 5 lần đăng nhập sai liên tiếp [1]. |
| q06 | SLA | 5 | 5 | 5 | 4 | Escalation trong sự cố P1 diễn ra theo hai quy trình. Đầu tiên, nếu cần thay đổi |
| q07 | Access Control | 5 | 1 | 5 | 1 | Không đủ dữ liệu trong tài liệu hiện có để trả lời câu hỏi này. |
| q08 | HR Policy | 5 | 5 | 5 | 4 | Nhân viên sau thời gian thử việc có thể làm việc từ xa tối đa 2 ngày mỗi tuần [1 |
| q09 | Insufficient Context | 5 | 1 | None | 3 | Không đủ dữ liệu trong tài liệu hiện có để trả lời câu hỏi này. |
| q10 | Refund | 5 | 1 | 5 | 2 | Không đủ dữ liệu trong tài liệu hiện có để trả lời câu hỏi này. |

## Detailed Notes

### [q01] SLA xử lý ticket P1 là bao lâu?

**Answer:** SLA xử lý ticket P1 là 4 giờ [1].

- Faithfulness (5): Thông tin trong câu trả lời hoàn toàn xuất phát từ tài liệu retrieved.
- Relevance (5): Câu trả lời đã đưa ra thời gian cụ thể cho SLA xử lý ticket P1, trả lời trực tiếp và đầy đủ cho câu hỏi.
- Context Recall (5): Recall=100% (1/1)
- Completeness (4): Câu trả lời đã đúng về thời gian xử lý ticket P1 là 4 giờ nhưng thiếu thông tin về SLA phản hồi ban đầu là 15 phút.

### [q02] Khách hàng có thể yêu cầu hoàn tiền trong bao nhiêu ngày?

**Answer:** Khách hàng có thể yêu cầu hoàn tiền trong vòng 7 ngày làm việc kể từ thời điểm xác nhận đơn hàng [1][3].

- Faithfulness (5): Tất cả thông tin trong câu trả lời đều xuất phát từ tài liệu đã được truy xuất.
- Relevance (5): Câu trả lời đã trực tiếp và đầy đủ giải quyết trọng tâm của câu hỏi.
- Context Recall (5): Recall=100% (1/1)
- Completeness (5): Câu trả lời đã bao gồm đầy đủ thông tin quan trọng, không thiếu sót chi tiết nào so với câu trả lời mong đợi.

### [q03] Ai phải phê duyệt để cấp quyền Level 3?

**Answer:** Để cấp quyền Level 3, cần phải được phê duyệt bởi Line Manager, IT Admin và IT Security [2].

- Faithfulness (5): Tất cả thông tin trong câu trả lời đều xuất phát từ tài liệu retrieved.
- Relevance (5): Câu trả lời đã nêu rõ những người cần phê duyệt để cấp quyền Level 3, trả lời trực tiếp và đầy đủ cho câu hỏi.
- Context Recall (5): Recall=100% (1/1)
- Completeness (5): Câu trả lời đã bao gồm đầy đủ tất cả các thông tin quan trọng.

### [q04] Sản phẩm kỹ thuật số có được hoàn tiền không?

**Answer:** Không, sản phẩm thuộc danh mục hàng kỹ thuật số như license key, subscription không được hoàn tiền [1].

- Faithfulness (5): Tất cả thông tin trong câu trả lời đều xuất phát từ tài liệu đã được truy xuất.
- Relevance (5): Câu trả lời đã trực tiếp và đầy đủ giải quyết trọng tâm của câu hỏi.
- Context Recall (5): Recall=100% (1/1)
- Completeness (5): Câu trả lời đã bao gồm đầy đủ thông tin quan trọng, không bỏ sót chi tiết nào so với câu trả lời mong đợi.

### [q05] Tài khoản bị khóa sau bao nhiêu lần đăng nhập sai?

**Answer:** Tài khoản sẽ bị khóa sau 5 lần đăng nhập sai liên tiếp [1].

- Faithfulness (5): Tất cả thông tin trong câu trả lời đều xuất phát từ tài liệu đã được truy xuất.
- Relevance (5): Câu trả lời đã trực tiếp và đầy đủ giải quyết trọng tâm của câu hỏi.
- Context Recall (5): Recall=100% (1/1)
- Completeness (5): Câu trả lời đã bao gồm đầy đủ thông tin cần thiết, không thiếu sót chi tiết nào so với câu trả lời mong đợi.

### [q06] Escalation trong sự cố P1 diễn ra như thế nào?

**Answer:** Escalation trong sự cố P1 diễn ra theo hai quy trình. Đầu tiên, nếu cần thay đổi quyền hệ thống để khắc phục sự cố, On-call IT Admin có thể cấp quyền tạm thời (tối đa 24 giờ) sau khi được Tech Lead phê duyệt bằng lời. Sau 24 giờ, phải có ticket chính thức hoặc quyền sẽ bị thu hồi tự động. Mọi quyền tạm thời phải được ghi log vào hệ thống Security Audit [1]. Thứ hai, nếu không có phản hồi trong vòng 10 phút, sự cố sẽ tự động được escalate lên Senior Engineer [2].

- Faithfulness (5): Mọi thông tin trong câu trả lời đều xuất phát từ tài liệu retrieved. Câu trả lời đã mô tả chính xác quy trình escalation trong sự cố P1, bao gồm việc cấp quyền tạm thời và việc tự động escalate lên Senior Engineer nếu không có phản hồi trong vòng 10 phút.
- Relevance (5): Câu trả lời đã mô tả chi tiết quy trình escalation trong sự cố P1, bao gồm cả việc thay đổi quyền hệ thống và việc escalate lên Senior Engineer nếu không có phản hồi.
- Context Recall (5): Recall=100% (1/1)
- Completeness (4): Câu trả lời đã bao gồm thông tin về việc escalate lên Senior Engineer nếu không có phản hồi trong 10 phút, tuy nhiên lại thêm vào thông tin không liên quan về việc cấp quyền tạm thời cho On-call IT Admin, điều này không được đề cập trong expected answer.

### [q07] Approval Matrix để cấp quyền hệ thống là tài liệu nào?

**Answer:** Không đủ dữ liệu trong tài liệu hiện có để trả lời câu hỏi này.

- Faithfulness (5): Câu trả lời không đưa ra bất kỳ thông tin nào không có trong context.
- Relevance (1): Câu trả lời không cung cấp thông tin về Approval Matrix để cấp quyền hệ thống là tài liệu nào.
- Context Recall (5): Recall=100% (1/1)
- Completeness (1): Câu trả lời không cung cấp bất kỳ thông tin nào về 'Approval Matrix for System Access' hoặc 'Access Control SOP'

### [q08] Nhân viên được làm remote tối đa mấy ngày mỗi tuần?

**Answer:** Nhân viên sau thời gian thử việc có thể làm việc từ xa tối đa 2 ngày mỗi tuần [1].

- Faithfulness (5): Tất cả thông tin trong câu trả lời đều xuất phát từ tài liệu đã được truy xuất. Nhân viên sau thời gian thử việc có thể làm việc từ xa tối đa 2 ngày mỗi tuần được nêu rõ trong context.
- Relevance (5): Câu trả lời đã trực tiếp và đầy đủ giải quyết trọng tâm của câu hỏi.
- Context Recall (5): Recall=100% (1/1)
- Completeness (4): Câu trả lời đã đúng nhưng thiếu thông tin về việc cần được Team Lead phê duyệt.

### [q09] ERR-403-AUTH là lỗi gì và cách xử lý?

**Answer:** Không đủ dữ liệu trong tài liệu hiện có để trả lời câu hỏi này.

- Faithfulness (5): Câu trả lời không cung cấp thông tin nào cả, do đó không có thông tin nào không xuất phát từ context.
- Relevance (1): Câu trả lời không cung cấp thông tin về lỗi ERR-403-AUTH và cách xử lý nó.
- Context Recall (None): No expected sources (abstain question)
- Completeness (3): Câu trả lời đã nêu rõ không có thông tin trong tài liệu, nhưng thiếu thông tin về việc lỗi có thể liên quan đến xác thực và đề xuất liên hệ IT Helpdesk.

### [q10] Nếu cần hoàn tiền khẩn cấp cho khách hàng VIP, quy trình có khác không?

**Answer:** Không đủ dữ liệu trong tài liệu hiện có để trả lời câu hỏi này.

- Faithfulness (5): Câu trả lời không đưa ra bất kỳ thông tin nào, do đó không có thông tin nào không xuất phát từ tài liệu retrieved.
- Relevance (1): Câu trả lời không cung cấp thông tin về quy trình hoàn tiền khẩn cấp cho khách hàng VIP.
- Context Recall (5): Recall=100% (1/1)
- Completeness (2): Câu trả lời đã bỏ sót thông tin về quy trình hoàn tiền tiêu chuẩn và thời gian xử lý, cũng như việc không có quy trình đặc biệt cho khách hàng VIP.

