# Danh sách học viên (list các tuple)
students = [
    ("SV01", "Nguyen Van A", 20),
    ("SV02", "Tran Thi B", 21),
    ("SV03", "Le Van C", 19),
]

# Dict lưu điểm từng môn cho từng sinh viên
scores = {
    "SV01": {"math": 8.0, "python": 7.5},
    "SV02": {"math": 6.5, "python": 8.5},
    "SV03": {"math": 9.0, "python": 9.5},
}

# Set các môn học hiện có
courses = {"math", "python"}

#a. Dùng vòng lặp + unpacking tuple để in ra danh sách học viên theo forma
def print_students(list_of_students: list[tuple[str, str, int]]) -> None:
    """
    print list of students ("SV01", "Nguyen Van A", 20), to format : SV01 - Nguyen Van A (20)
    """
    for student_id, name, age in list_of_students:
        print(f"{student_id} - {name} ({age})")

print_students(students)

#b. Tạo một list mới python_scores chỉ chứa tuple (student_id, name, python_score)
def create_python_scores(students_list: list[tuple[str, str, float]],
                         scores_dict: dict) -> list[tuple[str, str, float]]:
    python_scores = []
    for student_id, name, age in students_list:
        python_score = scores_dict[student_id]["python"]
        python_scores.append((student_id, name, python_score))
    return python_scores

python_scores = create_python_scores(students, scores)
print(f"python_scores = {python_scores}")

#c. Tìm học viên có điểm Python cao nhất từ python_scores và in ra: Top Python: <name> - <score>
def find_max_score_python(python_scores: list[tuple[str, str, float]]) -> tuple[str, float]:
    max_score = 0
    student_name_top = ""
    for _, student_name, python_score in python_scores:
        if python_score > max_score:
            max_score = python_score
            student_name_top = student_name
    return student_name_top, max_score

student_name, max_score = find_max_score_python(python_scores)
print(f"Top Python: {student_name} - {max_score}")
#d. Thêm môn mới "database" vào courses (dùng set) và gán tạm điểm database = 0 cho tất cả sinh viên trong scores
def add_new_course(courses: set[str], scores_dict: dict,
                   course_name: str, default_score: float | None = 0) -> None:
    courses.add(course_name)
    for student_id in scores_dict:
        scores_dict[student_id][course_name] = default_score

add_new_course(courses, scores, "database", 0)
print(scores)