# Bài tập 1: Dict tần suất từ trong file (Module + File I/O + Exception)

## Đề bài:
# > Viết chương trình phân tích một file text (ví dụ: `article.txt`) và in ra tần suất xuất hiện của từng từ
#
# ### Yêu cầu chức năng
# 1. Chương trình hỏi người dùng:
# ```text
# Nhập tên file cần phân tích:
# ```
#
# 2. Đọc toàn bộ nội dung file, chuẩn hóa:
# * chuyển hết về chữ thường (`lower()`)
# * bỏ các dấu câu cơ bản: `.,;:?!()[]` (có thể dùng `replace`)
#
# 3. Tách từ theo dấu cách, đếm số lần xuất hiện của từng từ
# 4. In ra:
# * Tổng số từ
# * Top 10 từ xuất hiện nhiều nhất cùng số lần xuất hiện
#
# Ví dụ:
#
# ```text
# Tổng số từ: 250
# Top 10 từ xuất hiện nhiều nhất:
# - python: 20
# - code: 15
# - file: 12
# ...
# ```
#
# ### Yêu cầu kỹ thuật
# * Tách code thành ít nhất 2 file:
#   * `file_utils.py`: chứa các hàm:
#     ```python
#         def read_file_content(filename: str) -> str: ...
#         def count_word_frequency(text: str) -> dict[str, int]: ...
#     ```
#   * `main.py`: xử lý input người dùng, gọi hàm từ `file_utils`
# * Phải dùng:
#   * `with open(...)` để đọc file
#   * `try/except` để xử lý:
#     * `FileNotFoundError`: báo “File không tồn tại”
#     * các lỗi khác: in “Có lỗi xảy ra: ...”
#   * Không dùng thư viện ngoài (chỉ dùng built-in)
#
# ---