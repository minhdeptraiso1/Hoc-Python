from student import Student


def load_students_from_file(filename: str) -> list[Student]:
    students = []

    with open(filename, 'r') as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue

            try:
                parts = line.split(',')

                if len(parts) != 3:
                    print(f"Cảnh báo: Dòng {line_num} sai format (thiếu cột): {line}")
                    continue

                name = parts[0].strip()
                age = int(parts[1].strip())
                score = float(parts[2].strip())

                student = Student(name, age, score)
                students.append(student)

            except ValueError as e:
                print(f"Cảnh báo: Dòng {line_num} không parse được (age hoặc score không hợp lệ): {line}")
                continue
            except Exception as e:
                print(f"Cảnh báo: Dòng {line_num} có lỗi: {e}")
                continue

    return students


def calc_avg_score(students: list[Student]) -> float:
    if not students:
        return 0.0

    total_score = sum(student.score for student in students)
    return total_score / len(students)


def find_top_student(students: list[Student]) -> Student | None:
    if not students:
        return None

    top_student = students[0]
    for student in students[1:]:
        if student.score > top_student.score:
            top_student = student

    return top_student


def filter_failed(students: list[Student]) -> list[Student]:
    failed_students = []
    for student in students:
        if not student.is_passed():
            failed_students.append(student)

    return failed_students