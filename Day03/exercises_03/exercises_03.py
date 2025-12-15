# # Bài tập 3: To-do List theo ngày với DateTime + File + OOP + Exception
#
# ## Đề bài:
# > Xây dựng chương trình quản lý danh sách công việc (to-do list) theo ngày, lưu vào file `tasks.txt` với format mỗi dòng:
#
# ```text
# Mô tả;YYYY-MM-DD;trạng_thái
# Học Python;2025-01-10;todo
# Đi tập gym;2025-01-09;done
# Đi chơi;2025-01-08;todo
# ```
#
# ### Yêu cầu chức năng
# 1. Định nghĩa class `Task`:
# ```python
# from datetime import datetime
#
# class Task:
#     def __init__(self, description: str, due_date: datetime, status: str = "todo"):
#         self.description = description
#         self.due_date = due_date # datetime
#         self.status = status # "todo" hoặc "done"
#
#     # Trả về True nếu quá hạn và chưa done
#     def is_overdue(self, now: datetime) -> bool:
#         ...
#
#     def __str__(self) -> str:
#         # Ví dụ: "[TODO] Học Python (Hạn: 2025-01-10)"
#         ...
#
# ```
#
# 2. Viết hàm:
#
# ```python
# def load_tasks(filename: str) -> list[Task]: ...
# def save_tasks(filename: str, tasks: list[Task]) -> None: ...
# ```
#
# * Dùng `datetime.strptime(due_str, "%Y-%m-%d")` để parse ngày
# * Xử lý lỗi format ngày => bỏ qua dòng và in cảnh báo
#
# 3. Chương trình có menu:
#
# ```text
# 1. Xem tất cả task
# 2. Xem các task quá hạn
# 3. Thêm task mới
# 4. Đánh dấu task là done
# 5. Thoát
# ```
#
# 4. Chi tiết:
# * “Xem tất cả task”: in lần lượt từng Task (dùng `__str__`)
# * “Xem các task quá hạn”:
#   * Dùng `datetime.now()` để lấy thời điểm hiện tại
#   * In các task `is_overdue(now) == True`
# * “Thêm task mới”:
#   * Nhập: mô tả, ngày hạn dạng `YYYY-MM-DD`
#   * Nếu ngày sai format => báo lỗi, không thêm
#   * Thêm vào list và ghi lại file `tasks.txt`
# * “Đánh dấu task là done”:
#   * Hiển thị danh sách có đánh số:
#     ```text
#         1. [TODO] Học Python (Hạn: 2025-01-10)
#         2. [TODO] Đi tập gym (Hạn: 2025-01-09)
#     ```
#   * Nhập số thứ tự, đổi `status` thành `"done"`, lưu lại file
#
# ### Yêu cầu kỹ thuật
# * Bắt buộc dùng:
#   * `datetime` (`now()`, `strptime`, `strftime` nếu muốn format khi in)
#   * `with open` cho file I/O
#   * `try/except` cho:
#     * lỗi file
#     * lỗi parse ngày
#     * lỗi nhập số thứ tự không hợp lệ (`ValueError`)
# * Tách code thành ít nhất 2 file:
#   * `models.py` (chứa Task)
#   * `task_service.py` (chứa hàm `load_tasks`, `save_tasks`, xử lý logic)
#   * `main.py` (menu + luồng chương trình)
