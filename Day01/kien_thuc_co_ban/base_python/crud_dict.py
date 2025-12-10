# ========================
# DANH SÁCH SINH VIÊN
# ========================
students = [
    {"id": 1, "name": "Minh", "scores": [8, 9, 7]},
    {"id": 2, "name": "Lan", "scores": [9, 10, 9]},
    {"id": 3, "name": "Hoàng", "scores": [6, 7, 8]},
]


# ========================
# CÁC HÀM CHỨC NĂNG
# ========================

def avg_score(scores):
    return sum(scores) / len(scores)


def show_students():
    print("\n===== DANH SÁCH SINH VIÊN =====")
    for s in students:
        print(f"ID: {s['id']}, Tên: {s['name']}, Điểm TB: {avg_score(s['scores']):.2f}")
    print()


def add_student():
    print("\n=== THÊM SINH VIÊN ===")
    id = int(input("Nhập ID: "))
    name = input("Nhập tên: ")
    scores = list(map(float, input("Nhập điểm (cách nhau bằng dấu cách): ").split()))

    students.append({"id": id, "name": name, "scores": scores})
    print(">> Thêm thành công!\n")


def edit_student():
    print("\n=== SỬA SINH VIÊN ===")
    id = int(input("Nhập ID sinh viên cần sửa: "))

    for s in students:
        if s["id"] == id:
            new_name = input("Tên mới (Enter để giữ nguyên): ")
            new_scores = input("Điểm mới (Enter để giữ nguyên): ")

            if new_name != "":
                s["name"] = new_name

            if new_scores != "":
                s["scores"] = list(map(float, new_scores.split()))

            print(">> Sửa thành công!\n")
            return

    print(">> Không tìm thấy sinh viên!\n")


def delete_student():
    print("\n=== XÓA SINH VIÊN ===")
    id = int(input("Nhập ID sinh viên cần xóa: "))

    for s in students:
        if s["id"] == id:
            students.remove(s)
            print(">> Xóa thành công!\n")
            return

    print(">> Không tìm thấy sinh viên!\n")


def find_student_by_name():
    print("\n=== TÌM SINH VIÊN THEO TÊN ===")
    name = input("Nhập tên cần tìm: ").lower()

    found = False
    for s in students:
        if s["name"].lower() == name:
            print(f"ID: {s['id']}, Tên: {s['name']}, Điểm TB: {avg_score(s['scores']):.2f}")
            found = True

    if not found:
        print(">> Không tìm thấy sinh viên!\n")


# ========================
# MENU CHÍNH
# ========================
def menu():
    while True:
        print("========== QUẢN LÝ SINH VIÊN ==========")
        print("1. Hiển thị danh sách")
        print("2. Thêm sinh viên")
        print("3. Sửa sinh viên")
        print("4. Xóa sinh viên")
        print("5. Tìm sinh viên theo tên")
        print("6. Thoát")

        choice = input("Chọn chức năng (1-6): ")

        if choice == "1":
            show_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            edit_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            find_student_by_name()
        elif choice == "6":
            print(">> Thoát chương trình. Bye!")
            break
        else:
            print(">> Lựa chọn không hợp lệ!\n")


# CHẠY CHƯƠNG TRÌNH
menu()
