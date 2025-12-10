"""
=====================================================
   TỔNG HỢP KIỂU DỮ LIỆU TẬP HỢP TRONG PYTHON
   Gồm:
   ✔ LIST
   ✔ DICT
   ✔ SET
   ✔ TUPLE
=====================================================
"""


# =====================================================
# 1) LIST (Danh sách)
# - Có thứ tự (ordered)
# - Thay đổi được (mutable)
# - Cho phép trùng lặp
# =====================================================

print("\n===== LIST =====")

fruits = ["apple", "banana", "orange"]
print("List ban đầu:", fruits)

# Truy cập phần tử
print("Phần tử đầu tiên:", fruits[0])

# Thêm phần tử
fruits.append("grape")
print("Sau append:", fruits)

# Chèn vào vị trí bất kỳ
fruits.insert(1, "kiwi")
print("Sau insert:", fruits)

# Xóa phần tử theo giá trị
fruits.remove("banana")
print("Sau remove:", fruits)

# Xóa phần tử theo index
deleted = fruits.pop(0)
print("Đã pop:", deleted)
print("List hiện tại:", fruits)

# Độ dài list
print("Độ dài list:", len(fruits))

# Lặp qua list
print("\nLặp qua list:")
for fruit in fruits:
    print(fruit)


# =====================================================
# 2) DICT (Từ điển)
# - Key-value (khóa – giá trị)
# - Không có thứ tự (trước Python 3.7)
# - Key không được trùng lặp
# =====================================================

print("\n===== DICTIONARY =====")

student = {
    "name": "Minh",
    "age": 22,
    "scores": [8, 9, 7]
}

print("Dict ban đầu:", student)

# Truy cập value
print("Tên:", student["name"])

# Thêm key-value
student["school"] = "UAD"
print("Thêm trường:", student)

# Sửa key-value
student["age"] = 23
print("Sau khi sửa tuổi:", student)

# Xóa key
student.pop("scores")
print("Sau khi pop scores:", student)

# Lặp qua dict
print("\nLặp qua dict (key - value):")
for key, value in student.items():
    print(key, "=", value)


# =====================================================
# 3) SET (Tập hợp)
# - Không thứ tự (unordered)
# - Không có phần tử trùng lặp
# - Nhanh khi tìm kiếm
# =====================================================

print("\n===== SET =====")

numbers = {1, 2, 3, 3, 4}
print("Set tự loại phần tử trùng:", numbers)

# Thêm phần tử
numbers.add(5)
print("Sau add:", numbers)

# Xóa phần tử
numbers.remove(2)
print("Sau remove:", numbers)

# Toán tập hợp
A = {1, 2, 3}
B = {3, 4, 5}

print("\nGiao (A & B):", A & B)
print("Hợp (A | B):", A | B)
print("Hiệu (A - B):", A - B)

# Lặp qua set
print("\nLặp qua set:")
for n in numbers:
    print(n)


# =====================================================
# 4) TUPLE
# - Có thứ tự (ordered)
# - KHÔNG thay đổi được (immutable)
# - Nhanh & tiết kiệm bộ nhớ hơn list
# =====================================================

print("\n===== TUPLE =====")

t = (10, 20, 30, 40)
print("Tuple ban đầu:", t)

# Truy cập phần tử
print("Phần tử thứ 2:", t[1])

# Duyệt tuple
print("\nLặp qua tuple:")
for item in t:
    print(item)

# Tuple dùng để đóng gói dữ liệu không thay đổi
person = ("Minh", 22, "Đà Nẵng")
print("\nTuple thông tin:", person)

# Chuyển tuple <-> list
t_list = list(t)
print("Tuple -> List:", t_list)

t_again = tuple(t_list)
print("List -> Tuple:", t_again)


# =====================================================
# 5) SO SÁNH NHANH 4 KIỂU
# =====================================================

print("""
===== SO SÁNH NHANH =====
LIST  : Có thứ tự, thay đổi được, cho trùng lặp
TUPLE : Có thứ tự, KHÔNG thay đổi được
SET   : Không thứ tự, KHÔNG trùng lặp
DICT  : Key-value, Key không trùng lặp
""")

