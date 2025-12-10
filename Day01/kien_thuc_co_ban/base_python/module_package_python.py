"""
=================================================================================
                 TỔNG HỢP MODULE & PACKAGE TRONG PYTHON
Gồm:
✔ Module là gì?
✔ Package là gì?
✔ Import module: import, from ... import, as
✔ Thư viện chuẩn: math, random, datetime,...
✔ Tự tạo module (.py)
✔ Tự tạo package (folder + __init__.py)
✔ Cách gọi hàm giữa nhiều file
=================================================================================
"""

print("\n===== MODULE & PACKAGE TRONG PYTHON =====")


# =============================================================================
# 1) MODULE LÀ GÌ?
# - Một file Python (.py) được gọi là module
# - Dùng để tách code rõ ràng, dễ quản lý
# =============================================================================

print("\n===== MODULE – THƯ VIỆN CHUẨN =====")

import math

print("Căn bậc 2 của 16:", math.sqrt(16))
print("Góc sin của 90°:", math.sin(math.radians(90)))
print("Pi =", math.pi)


# =============================================================================
# 2) IMPORT MODULE THEO NHIỀU CÁCH
# =============================================================================

print("\n===== CÁCH IMPORT KHÁC NHAU =====")

# import toàn bộ module
import random
print("Random số 1–10:", random.randint(1, 10))

# import 1 hàm
from random import choice
print("Random chọn:", choice([1, 2, 3]))

# import alias (tên viết tắt)
import datetime as dt
print("Năm hiện tại:", dt.datetime.now().year)


# =============================================================================
# 3) TỰ TẠO MODULE – DEMO
# =============================================================================

print("\n===== TỰ TẠO MODULE =====")

# Giả sử tạo 1 file tên: mymodule.py
# Nội dung file đó như sau:
#
#   def hello(name):
#       return f'Xin chào {name}!'
#
#   def add(a, b):
#       return a + b
#
# Sau đó ta có thể import như sau:

try:
    import mymodule   # nếu module chưa tồn tại sẽ báo lỗi, nên đặt trong try
    print(mymodule.hello("Minh"))
    print("2 + 3 =", mymodule.add(2, 3))
except ModuleNotFoundError:
    print("⚠ Demo: File 'mymodule.py' chưa tồn tại. Hãy tự tạo file để thử!")


# =============================================================================
# 4) PACKAGE LÀ GÌ?
# - Là 1 thư mục chứa nhiều module
# - Bắt buộc có file __init__.py để Python hiểu đây là package
# =============================================================================

print("\n===== PACKAGE – CẤU TRÚC =====")

"""
Ví dụ tạo package:

project/
   ├── mypackage/
   │       ├── __init__.py
   │       ├── math_utils.py
   │       ├── string_utils.py
   └── main.py

Nội dung math_utils.py:
    def add(a, b):
        return a + b

Nội dung string_utils.py:
    def upper(s):
        return s.upper()

Nội dung __init__.py:
    from .math_utils import add
    from .string_utils import upper

Cách dùng trong main.py:
    from mypackage import add, upper
    print(add(2, 3))
    print(upper("minh"))
"""


# =============================================================================
# 5) GIẢ LẬP PACKAGE ĐỂ DEMO TRONG FILE NÀY
# (Không chạy được nếu không tạo folder thật)
# =============================================================================

print("\n===== DEMO PACKAGE (MÔ PHỎNG) =====")

try:
    from mypackage import add, upper
    print(add(5, 6))
    print(upper("hello"))
except ModuleNotFoundError:
    print("⚠ Demo: Hãy tạo folder 'mypackage' và các file bên trong để thử!")


# =============================================================================
# 6) __init__.py DÙNG ĐỂ:
# - Xác định package
# - Gom các hàm để import dễ hơn
# - Chạy code khi package được import (không khuyến khích)
# =============================================================================

print("\n===== __init__.py =====")

"""
File __init__.py có thể rỗng, hoặc dùng để:
✔ Export hàm/tên để import từ package tiện hơn:
    from .module import function
✔ Khởi tạo các biến package
✔ Setup environment ban đầu (hiếm dùng)
"""


# =============================================================================
# 7) BÀI TOÁN THỰC TẾ: MODULE QUẢN LÝ SINH VIÊN
# =============================================================================

print("\n===== VÍ DỤ MODULE THỰC TẾ =====")

"""
Tạo file student.py:
-----------------------
def avg(scores):
    return sum(scores) / len(scores)

def show(name, scores):
    print(name, "- Điểm TB:", avg(scores))

Tạo file main.py:
-----------------------
import student
student.show("Minh", [8, 9, 10])
"""


# =============================================================================
# 8) TÓM TẮT
# =============================================================================

print("""
======================= TÓM TẮT MODULE & PACKAGE =======================

MODULE:
- Là 1 file .py
- import module:      import math
- import 1 hàm:       from math import sqrt
- import với alias:   import math as m

PACKAGE:
- Là 1 thư mục chứa nhiều module
- Phải có __init__.py
- Cách import:
    from package import module
    from package.module import function

__init__.py:
- Dùng để đánh dấu package
- Gom các hàm để import dễ hơn
=======================================================================
""")
