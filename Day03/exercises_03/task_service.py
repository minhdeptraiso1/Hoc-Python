from datetime import datetime
from models import Task


def load_tasks(filename: str) -> list[Task]:
    tasks = []

    try:
        with open(filename, 'r') as f:
            for line_num, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue

                try:
                    parts = line.split(';')

                    if len(parts) != 3:
                        print(f"Cảnh báo: Dòng {line_num} sai format: {line}")
                        continue

                    description = parts[0].strip()
                    date_str = parts[1].strip()
                    status = parts[2].strip()

                    due_date = datetime.strptime(date_str, "%Y-%m-%d")

                    task = Task(description, due_date, status)
                    tasks.append(task)

                except ValueError as e:
                    print(f"Cảnh báo: Dòng {line_num} - Lỗi parse ngày: {line}")
                    continue
                except Exception as e:
                    print(f"Cảnh báo: Dòng {line_num} - Lỗi: {e}")
                    continue

    except FileNotFoundError:
        print(f"File '{filename}' chưa tồn tại. Sẽ tạo mới khi lưu.")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")

    return tasks


def save_tasks(filename: str, tasks: list[Task]) -> None:

    try:
        with open(filename, 'w') as f:
            for task in tasks:
                date_str = task.due_date.strftime("%Y-%m-%d")
                line = f"{task.description};{date_str};{task.status}\n"
                f.write(line)
        print(" Đã lưu thành công!")
    except Exception as e:
        print(f" Lỗi khi lưu file: {e}")


def get_overdue_tasks(tasks: list[Task]) -> list[Task]:

    now = datetime.now()
    overdue = []

    for task in tasks:
        if task.is_overdue(now):
            overdue.append(task)

    return overdue


def add_new_task(tasks: list[Task]) -> bool:

    try:
        description = input("Nhập mô tả công việc: ").strip()

        if not description:
            print(" Mô tả không được để trống!")
            return False

        date_str = input("Nhập ngày hạn (YYYY-MM-DD): ").strip()


        due_date = datetime.strptime(date_str, "%Y-%m-%d")


        new_task = Task(description, due_date, "todo")
        tasks.append(new_task)

        print(f" Đã thêm task: {new_task}")
        return True

    except ValueError:
        print("Lỗi: Ngày không đúng format YYYY-MM-DD!")
        return False
    except Exception as e:
        print(f"Lỗi: {e}")
        return False


def mark_task_done(tasks: list[Task]) -> bool:

    if not tasks:
        print("Không có task nào!")
        return False

    print("\nDanh sách task:")
    for i, task in enumerate(tasks, start=1):
        print(f"   {i}. {task}")

    try:
        choice = input("\nNhập số thứ tự task cần đánh dấu done: ").strip()
        index = int(choice) - 1

        if index < 0 or index >= len(tasks):
            print("Số thứ tự không hợp lệ!")
            return False

        tasks[index].mark_as_done()
        print(f"Đã đánh dấu done: {tasks[index]}")
        return True

    except ValueError:
        print("Vui lòng nhập số!")
        return False
    except Exception as e:
        print(f"Lỗi: {e}")
        return False