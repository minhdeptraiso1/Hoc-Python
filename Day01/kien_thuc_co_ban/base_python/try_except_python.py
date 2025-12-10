"""
========================================================
    TỔNG HỢP XỬ LÝ LỖI (EXCEPTION) TRONG PYTHON
    Bao gồm:
    ✔ try / except cơ bản
    ✔ Bắt nhiều lỗi cùng lúc
    ✔ except cụ thể từng lỗi
    ✔ try / except / else
    ✔ try / except / finally
    ✔ raise (tự tạo lỗi)
    ✔ Custom Exception (tạo class lỗi riêng)
    ✔ Ví dụ thực tế
========================================================
"""


# ======================================================
# 1) TRY / EXCEPT CƠ BẢN
# ======================================================

print("\n===== TRY / EXCEPT CƠ BẢN =====")

try:
    x = 10 / 0
except:
    print("Lỗi rồi! Không thể chia cho 0.")


# ======================================================
# 2) BẮT NHIỀU LOẠI LỖI
# ======================================================

print("\n===== BẮT NHIỀU LỖI =====")

try:
    a = int("abc")
except ValueError:
    print("Không thể chuyển 'abc' thành số nguyên!")


# ======================================================
# 3) BẮT NHIỀU EXCEPTION TRONG CÙNG 1 EXCEPT
# ======================================================

print("\n===== BẮT NHIỀU LỖI TRONG 1 EXCEPT =====")

try:
    result = 10 / 0
except (ZeroDivisionError, TypeError):
    print("Đã xảy ra lỗi chia số hoặc lỗi kiểu dữ liệu!")


# ======================================================
# 4) TRY / EXCEPT / ELSE
# - else chỉ chạy khi KHÔNG có lỗi
# ======================================================

print("\n===== TRY / EXCEPT / ELSE =====")

try:
    number = int("123")
except ValueError:
    print("Lỗi chuyển đổi!")
else:
    print("Không lỗi! Giá trị:", number)


# ======================================================
# 5) TRY / EXCEPT / FINALLY
# - finally luôn chạy dù có lỗi hoặc không có lỗi
# - dùng để đóng kết nối, file, database
# ======================================================

print("\n===== TRY / EXCEPT / FINALLY =====")

try:
    f = open("fake_file.txt", "r")
except FileNotFoundError:
    print("Không tìm thấy file!")
finally:
    print("Dòng này luôn chạy (dọn dẹp tài nguyên).")


# ======================================================
# 6) TỰ TẠO LỖI BẰNG raise
# ======================================================

print("\n===== TỰ TẠO LỖI (raise) =====")

def check_age(age):
    if age < 0:
        raise ValueError("Tuổi không được âm!")
    return age

try:
    check_age(-5)
except ValueError as e:
    print("Lỗi:", e)


# ======================================================
# 7) TẠO LỖI RIÊNG (CUSTOM EXCEPTION)
# ======================================================

print("\n===== CUSTOM EXCEPTION =====")

class TooSmallError(Exception):
    """Lỗi: số quá nhỏ"""
    pass

def check_number(n):
    if n < 10:
        raise TooSmallError("Số phải >= 10")
    return n

try:
    check_number(5)
except TooSmallError as e:
    print("Custom Error:", e)


# ======================================================
# 8) VÍ DỤ THỰC TẾ: NHẬP SỐ AN TOÀN
# ======================================================

print("\n===== NHẬP SỐ AN TOÀN =====")

while True:
    try:
        value = int(input("Nhập số nguyên: "))
        break
    except ValueError:
        print("Vui lòng nhập một số hợp lệ!")

print("Bạn đã nhập:", value)


# ======================================================
# 9) VÍ DỤ THỰC TẾ: CHIA HAI SỐ
# ======================================================

print("\n===== CHIA HAI SỐ =====")

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Không chia cho 0 được!"

print(safe_divide(10, 2))
print(safe_divide(10, 0))


# ======================================================
# 10) VÍ DỤ: ĐỌC FILE (XỬ LÝ FILE NOT FOUND)
# ======================================================

print("\n===== ĐỌC FILE =====")

filename = "khong_ton_tai.txt"

try:
    with open(filename, "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File không tồn tại:", filename)
else:
    print("Nội dung file:", data)


# ======================================================
# 11) TỔNG HỢP TÓM TẮT
# ======================================================

print("""
=================== TÓM TẮT ===================
try:
    # Đoạn code có nguy cơ gây lỗi
except ErrorType:
    # Bắt lỗi cụ thể
except:
    # Bắt mọi lỗi
else:
    # Chạy khi không có lỗi
finally:
    # Luôn luôn chạy (dọn dẹp, đóng file)
raise ErrorType("Message")
# --> tự tạo lỗi
================================================
""")
