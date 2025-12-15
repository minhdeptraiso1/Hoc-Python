# # Bài tập 2: Quản lý điểm sinh viên với File I/O + OOP + Exception
#
# ## Đề bài:
# > Viết chương trình quản lý điểm sinh viên, dữ liệu được lưu trong file `students.txt`, mỗi dòng có format:
#
# ```text
# Tên,Tuổi,Điểm
# An,20,8.5
# Binh,21,6.0
# Chi,19,4.5
# ```
#
# ### Yêu cầu chức năng
# 1. Định nghĩa class `Student`:
# ```python
# class Student:
#     def __init__(self, name: str, age: int, score: float):
#         self.name = name
#         self.age = age
#         self.score = score
#
#     def is_passed(self) -> bool:  # đậu nếu score >= 5
#         ...
#
#     def __str__(self) -> str:
#         # "An (20 tuổi) – Điểm: 8.5"
#         ...
# ```
#
# 2. Viết hàm:
#
# ```python
# def load_students_from_file(filename: str) -> list[Student]: ...
# ```
#
# * Dùng `with open(...)` đọc file:
#   * Bỏ qua các dòng trống
#   * Xử lý lỗi:
#     * Dòng sai format (thiếu cột, không parse được `age` hoặc `score`) => bỏ qua dòng đó và in cảnh báo
#
# 3. Viết các hàm xử lý:
#
# * `def calc_avg_score(students: list[Student]) -> float`
# * `def find_top_student(students: list[Student]) -> Student | None`
# * `def filter_failed(students: list[Student]) -> list[Student]` (danh sách sinh viên rớt)
#
# 4. Trong `main.py`:
# * Hỏi tên file:
#
# ```text
# Nhập tên file điểm sinh viên:
# ```
#
# * In ra:
#   * Điểm trung bình lớp
#   * Sinh viên điểm cao nhất
#   * Danh sách sinh viên bị rớt
#
# ### Yêu cầu kỹ thuật
# * Sử dụng OOP đúng nghĩa (class `Student`)
# * Sử dụng list các object + các hàm xử lý list này
# * Có `try/except` để:
#   * Bắt lỗi không mở được file
#   * Bắt lỗi khi parse dữ liệu từng dòng
# * Nên dùng `type hint` cho hàm
#
#
# ---