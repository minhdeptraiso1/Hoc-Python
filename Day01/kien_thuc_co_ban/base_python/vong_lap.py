"""
===========================================
   TỔNG HỢP VÒNG LẶP TRONG PYTHON
   Gồm:
   ✔ for loop
   ✔ while loop
   ✔ range()
   ✔ break – continue
   ✔ else trong vòng lặp
   ✔ lặp list, dict, string
   ✔ enumerate()
   ✔ vòng lặp lồng nhau
===========================================
"""


# ======================================================
# 1) VÒNG LẶP FOR
# ======================================================

print("\n===== VÍ DỤ FOR CƠ BẢN =====")

# Lặp range(n) -> từ 0 đến n - 1
for i in range(5):
    print("i =", i)


print("\n===== RANGE(start, end, step) =====")
for i in range(2, 10, 2):
    print("Số chẵn:", i)


print("\n===== LẶP QUA LIST =====")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print("Trái cây:", fruit)


print("\n===== LẶP QUA STRING =====")
for char in "Minh":
    print("Ký tự:", char)


print("\n===== LẶP QUA DICTIONARY =====")
student = {"name": "Lan", "age": 20, "score": 9}

print("\n-- Lặp qua key --")
for key in student:
    print(key)

print("\n-- Lặp key và value --")
for key, value in student.items():
    print(key, "=", value)


# ======================================================
# 2) VÒNG LẶP WHILE
# ======================================================

print("\n===== VÒNG LẶP WHILE =====")
i = 1
while i <= 5:
    print("i =", i)
    i += 1


# ======================================================
# 3) BREAK – CONTINUE
# ======================================================

print("\n===== BREAK – DỪNG VÒNG LẶP =====")
for i in range(10):
    if i == 5:
        break  # dừng ngay lập tức
    print(i)


print("\n===== CONTINUE – BỎ QUA LẦN LẶP =====")
for i in range(6):
    if i == 3:
        continue  # bỏ qua i = 3
    print(i)


# ======================================================
# 4) ELSE TRONG VÒNG LẶP
# ======================================================

print("\n===== ELSE TRONG VÒNG LẶP =====")
for i in range(3):
    print(i)
else:
    print("Vòng lặp kết thúc bình thường (không break)")

print("\n===== ELSE KHÔNG CHẠY KHI CÓ BREAK =====")
for i in range(5):
    if i == 2:
        break
    print(i)
else:
    print("Dòng này sẽ không chạy vì có break")


# ======================================================
# 5) ENUMERATE – LẤY CẢ INDEX + VALUE
# ======================================================

print("\n===== ENUMERATE =====")
names = ["Minh", "Lan", "Hoàng"]
for index, name in enumerate(names):
    print(f"Index {index} có giá trị {name}")


# ======================================================
# 6) VÒNG LẶP LỒNG NHAU (NESTED LOOP)
# ======================================================

print("\n===== VÒNG LẶP LỒNG NHAU =====")
for i in range(3):
    for j in range(2):
        print(f"(i={i}, j={j})")


# ======================================================
# 7) ỨNG DỤNG THỰC TẾ – TÍNH TỔNG 1 → N
# ======================================================

print("\n===== TÍNH TỔNG 1 → N =====")
n = 5
total = 0
for i in range(1, n + 1):
    total += i

print(f"Tổng từ 1 đến {n} là {total}")


# ======================================================
# 8) BÀI TOÁN: TÌM SỐ LỚN NHẤT TRONG LIST
# ======================================================

print("\n===== TÌM SỐ LỚN NHẤT =====")
numbers = [3, 7, 2, 8, 9, 4]

max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num

print("Số lớn nhất là:", max_value)


# ======================================================
# 9) BÀI TOÁN: ĐẾM SỐ KÝ TỰ TRONG CHUỖI
# ======================================================

print("\n===== ĐẾM CHỮ 'a' TRONG CHUỖI =====")
text = "banana"
count_a = 0
for char in text:
    if char == "a":
        count_a += 1

print("Số lượng chữ 'a':", count_a)


# ======================================================
# 10) MENU LẶP BẰNG WHILE
# ======================================================

print("\n===== MENU LẶP WHILE =====")
while True:
    print("1. Xin chào")
    print("2. Tạm biệt")
    print("3. Thoát")

    choice = input("Nhập lựa chọn: ")

    if choice == "1":
        print("Xin chào bạn!")
    elif choice == "2":
        print("Tạm biệt bạn!")
    elif choice == "3":
        print("Thoát chương trình...")
        break
    else:
        print("Lựa chọn không hợp lệ!")
