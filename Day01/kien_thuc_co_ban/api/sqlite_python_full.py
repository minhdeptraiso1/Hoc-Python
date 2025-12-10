"""
===============================================================================
                 SQL + PYTHON (SQLite3) – TỔNG HỢP CƠ BẢN → NÂNG CAO
Gồm:
✔ Kết nối SQLite
✔ Tạo bảng
✔ INSERT – SELECT – UPDATE – DELETE
✔ Dùng cursor
✔ Dùng parameter để tránh SQL Injection
✔ Lấy dữ liệu dạng tuple & dict
✔ Ví dụ CRUD quản lý sinh viên
===============================================================================
"""

import sqlite3

# =============================================================================
# 1) KẾT NỐI DATABASE SQLITE
# - SQLite tạo file .db
# - Nếu file chưa tồn tại → tự tạo
# =============================================================================

print("\n===== 1) KẾT NỐI DATABASE =====")

conn = sqlite3.connect("students.db")   # tạo file database
cursor = conn.cursor()

print("Kết nối SQLite thành công!")


# =============================================================================
# 2) TẠO BẢNG
# =============================================================================

print("\n===== 2) TẠO BẢNG =====")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    score REAL
)
""")

conn.commit()
print("Đã tạo bảng students (nếu chưa có).")


# =============================================================================
# 3) INSERT DỮ LIỆU
# =============================================================================

print("\n===== 3) INSERT DỮ LIỆU =====")

cursor.execute("INSERT INTO students (name, age, score) VALUES (?, ?, ?)",
               ("Minh", 22, 8.5))

cursor.execute("INSERT INTO students (name, age, score) VALUES (?, ?, ?)",
               ("Lan", 21, 9.0))

conn.commit()
print("Đã chèn dữ liệu thành công!")


# =============================================================================
# 4) SELECT DỮ LIỆU
# =============================================================================

print("\n===== 4) SELECT DỮ LIỆU =====")

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("Danh sách sinh viên:")
for row in rows:
    print(row)     # dạng tuple: (id, name, age, score)


# =============================================================================
# 5) LẤY DỮ LIỆU DẠNG DICTIONARY (TÊN CỘT)
# =============================================================================

print("\n===== 5) SELECT DẠNG DICT =====")

# Đặt row_factory để trả về dict
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(dict(row))


# =============================================================================
# 6) UPDATE DỮ LIỆU
# =============================================================================

print("\n===== 6) UPDATE DỮ LIỆU =====")

cursor.execute("UPDATE students SET score = ? WHERE name = ?", (9.5, "Minh"))
conn.commit()

print("Đã cập nhật điểm cho Minh!")


# =============================================================================
# 7) DELETE DỮ LIỆU
# =============================================================================

print("\n===== 7) DELETE DỮ LIỆU =====")

cursor.execute("DELETE FROM students WHERE name = ?", ("Lan",))
conn.commit()

print("Đã xóa sinh viên tên Lan!")


# =============================================================================
# 8) HÀM CRUD HOÀN CHỈNH (TẠO – ĐỌC – SỬA – XÓA)
# =============================================================================

print("\n===== 8) CRUD HOÀN CHỈNH =====")

def add_student(name, age, score):
    cursor.execute("INSERT INTO students (name, age, score) VALUES (?, ?, ?)",
                   (name, age, score))
    conn.commit()

def get_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

def update_student(id, new_score):
    cursor.execute("UPDATE students SET score = ? WHERE id = ?", (new_score, id))
    conn.commit()

def delete_student(id):
    cursor.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()


# Demo CRUD
print("Thêm sinh viên Huy:")
add_student("Huy", 23, 8.0)

print("Danh sách sau khi thêm:")
for row in get_students():
    print(row)

print("Cập nhật điểm Huy:")
update_student(3, 9.2)

print("Sau UPDATE:")
for row in get_students():
    print(row)

print("Xóa sinh viên id=3:")
delete_student(3)

print("Sau DELETE:")
for row in get_students():
    print(row)


# =============================================================================
# 9) ĐÓNG KẾT NỐI
# =============================================================================

print("\n===== 9) ĐÓNG DATABASE =====")

conn.close()
print("Đã đóng kết nối database.")
