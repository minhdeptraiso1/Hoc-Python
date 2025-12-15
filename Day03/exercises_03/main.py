from task_service import (
    load_tasks,
    save_tasks,
    get_overdue_tasks,
    add_new_task,
    mark_task_done
)


def display_menu():

    print("\n" + "=" * 50)
    print("QUẢN LÝ TO-DO LIST")
    print("=" * 50)
    print("1. Xem tất cả task")
    print("2. Xem các task quá hạn")
    print("3. Thêm task mới")
    print("4. Đánh dấu task là done")
    print("5. Thoát")
    print("=" * 50)


def view_all_tasks(tasks):
    if not tasks:
        print("\nKhông có task nào!")
        return

    print(f"\nTất cả task ({len(tasks)} task):")
    for i, task in enumerate(tasks, start=1):
        print(f"   {i}. {task}")


def view_overdue_tasks(tasks):
    overdue = get_overdue_tasks(tasks)

    if not overdue:
        print("\nKhông có task nào quá hạn!")
        return

    print(f"\nCác task quá hạn ({len(overdue)} task):")
    for i, task in enumerate(overdue, start=1):
        print(f"   {i}. {task}")


def main():
    FILENAME = "data.txt"

    tasks = load_tasks(FILENAME)
    print(f"Đã load {len(tasks)} task từ file '{FILENAME}'")

    while True:
        display_menu()

        try:
            choice = input("\nNhập lựa chọn (1-5): ").strip()

            if choice == "1":
                view_all_tasks(tasks)

            elif choice == "2":
                view_overdue_tasks(tasks)

            elif choice == "3":
                if add_new_task(tasks):
                    save_tasks(FILENAME, tasks)

            elif choice == "4":
                if mark_task_done(tasks):
                    save_tasks(FILENAME, tasks)

            elif choice == "5":
                print("\nTạm biệt! Đã lưu tất cả thay đổi.")
                break

            else:
                print("Lựa chọn không hợp lệ! Vui lòng chọn 1-5.")

        except KeyboardInterrupt:
            print("\n\nTạm biệt!")
            break
        except Exception as e:
            print(f"\nLỗi: {e}")


if __name__ == "__main__":
    main()