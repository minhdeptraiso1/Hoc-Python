from random import choice

from student_utils import (
    load_students_from_file,
    calc_avg_score,
    find_top_student,
    filter_failed
)


def main():
    file_name = input("Nhập tên file điểm sinh viên: ")
    while True:
        try:
            file_choice = int(
                input("Chọn kiểu file: \n 1. file.txt \n 2. file.sgv \n 3. file.exe\n Lựa chọn của bạn: "))

            if file_choice == 1:
                file_type = ".txt"
                break
            elif file_choice == 2:
                file_type = ".sgv"
                break
            elif file_choice == 3:
                file_type = ".exe"
                break
            else:
                print("Lựa chọn không hợp lệ! Vui lòng chọn 1, 2 hoặc 3.")
        except ValueError:
            print("Vui lòng nhập số nguyên (1, 2 hoặc 3)!")

    file = file_name + file_type

    try:
        students = load_students_from_file(file)
        if not students:
            print("\nKhông có dữ liệu sinh viên hợp lệ trong file!")
            return

        print(f"\n{'=' * 50}")
        print(f"ĐÃ TÌM THẤY {len(students)} SINH VIÊN")
        print(f"{'=' * 50}")

        avg_score = calc_avg_score(students)
        print(f"\n Điểm trung bình lớp: {avg_score:.2f}")

        top_student = find_top_student(students)
        if top_student:
            print(f"\n Sinh viên điểm cao nhất: {top_student}")

        failed_students = filter_failed(students)
        print(f"\n Danh sách sinh viên bị rớt ({len(failed_students)} người):")

        if failed_students:
            for student in failed_students:
                print(f"   - {student}")
        else:
            print("   (Không có sinh viên nào bị rớt)")

        print(f"\n{'=' * 50}")

    except FileNotFoundError:
        print(f"\n Lỗi: File '{file}' không tồn tại!")

    except Exception as e:
        print(f"\n Có lỗi xảy ra: {e}")


if __name__ == "__main__":
    main()