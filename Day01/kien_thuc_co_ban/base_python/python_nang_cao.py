"""
====================================================================
         TỔNG HỢP PYTHON NÂNG CAO – GIẢI THÍCH CHI TIẾT
   Bao gồm:
   ✔ Lambda function
   ✔ map(), filter(), reduce()
   ✔ List / Dict / Set Comprehension
   ✔ Generator & yield
   ✔ Decorator (cơ bản → nâng cao)
====================================================================
"""


# ================================================================
# 1) LAMBDA FUNCTION
# - Hàm ẩn danh, ngắn gọn, dùng khi cần logic đơn giản
# ================================================================

print("\n===== LAMBDA FUNCTION =====")

# Hàm bình thường
def add(a, b):
    return a + b

# Hàm lambda
add_lambda = lambda a, b: a + b

print("Hàm lambda:", add_lambda(3, 5))


# Lambda với sort()
numbers = [5, 2, 9, 1]
sorted_numbers = sorted(numbers, key=lambda x: x)
print("Sort với lambda:", sorted_numbers)


# ================================================================
# 2) map(), filter(), reduce()
# ================================================================

print("\n===== MAP – FILTER – REDUCE =====")

# map(): áp dụng hàm cho từng phần tử
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, nums))
print("Bình phương (map):", squared)

# filter(): lọc phần tử theo điều kiện
even = list(filter(lambda x: x % 2 == 0, nums))
print("Số chẵn (filter):", even)

# reduce(): gộp giá trị (phải import thêm)
from functools import reduce
total = reduce(lambda a, b: a + b, nums)
print("Tổng (reduce):", total)


# ================================================================
# 3) LIST COMPREHENSION
# ================================================================

print("\n===== LIST COMPREHENSION =====")

# Bình thường
squares_normal = []
for x in range(5):
    squares_normal.append(x * x)

# Comprehension
squares = [x * x for x in range(5)]
print("List comprehension:", squares)

# Lọc với điều kiện
evens = [x for x in range(10) if x % 2 == 0]
print("Số chẵn:", evens)


# ================================================================
# 4) DICT COMPREHENSION
# ================================================================

print("\n===== DICT COMPREHENSION =====")

names = ["Minh", "Lan", "Hoàng"]
name_lengths = {name: len(name) for name in names}
print("Dict comprehension:", name_lengths)


# ================================================================
# 5) SET COMPREHENSION
# ================================================================

print("\n===== SET COMPREHENSION =====")

unique_squared = {x * x for x in [1, 2, 2, 3, 3, 4]}
print("Set comprehension:", unique_squared)


# ================================================================
# 6) GENERATOR & YIELD
# - Tạo giá trị tuần tự, không tốn nhiều bộ nhớ
# ================================================================

print("\n===== GENERATOR & YIELD =====")

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# Generators không tạo list, chỉ sinh từng giá trị khi cần
for num in count_up_to(5):
    print("Generator trả:", num)


# Generator expression (giống list comprehension nhưng dùng ())
gen = (x * 2 for x in range(5))
print("Generator expression:", list(gen))


# ================================================================
# 7) DECORATOR CƠ BẢN
# ================================================================

print("\n===== DECORATOR CƠ BẢN =====")

def my_decorator(func):
    def wrapper():
        print("Trước khi chạy hàm...")
        func()
        print("Sau khi chạy hàm...")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# ================================================================
# 8) DECORATOR CÓ THAM SỐ
# ================================================================

print("\n===== DECORATOR CÓ THAM SỐ =====")

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Đang chạy hàm: {func.__name__} với args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug
def add2(a, b):
    return a + b

print("Kết quả add:", add2(3, 5))


# ================================================================
# 9) DECORATOR LỒNG NHAU (NÂNG CAO)
# ================================================================

print("\n===== DECORATOR LỒNG NHAU =====")

def deco1(func):
    def wrap():
        print("Decorator 1")
        func()
    return wrap

def deco2(func):
    def wrap():
        print("Decorator 2")
        func()
    return wrap

@deco1
@deco2
def test_func():
    print("Hàm gốc")

test_func()


# ================================================================
# 10) BÀI TOÁN THỰC TẾ: ĐO THỜI GIAN CHẠY HÀM
# ================================================================

print("\n===== ĐO THỜI GIAN CHẠY HÀM =====")

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Thời gian chạy: {time.time() - start:.5f} giây")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

slow_function()


# ================================================================
# 11) TÓM TẮT KIẾN THỨC
# ================================================================

print("""
==================== TÓM TẮT NÂNG CAO ====================

✔ Lambda → hàm ngắn gọn
✔ map() → xử lý từng phần tử
✔ filter() → lọc phần tử
✔ reduce() → tính tổng/nhân/gộp dãy
✔ Comprehension:
    List / Dict / Set → viết ngắn, nhanh, đẹp
✔ Generator → tiết kiệm bộ nhớ
✔ Decorator → sửa hành vi hàm, log, timer, auth…

============================================================
""")
