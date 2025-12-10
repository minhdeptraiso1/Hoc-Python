"""
===============================================================================
            PYTHON OOP NÂNG CAO – TỔNG HỢP ĐẦY ĐỦ + GIẢI THÍCH CHI TIẾT
Gồm:
✔ Abstract Class (abc)
✔ Interface trong Python
✔ Multiple Inheritance (đa kế thừa)
✔ MRO (Method Resolution Order) – C3 Linearization
✔ super() nâng cao
✔ Diamond Problem & cách Python giải quyết
✔ Ví dụ thực tế
===============================================================================
"""

from abc import ABC, abstractmethod


# =============================================================================
# 1) ABSTRACT CLASS (LỚP TRỪU TƯỢNG)
# - Không thể tạo đối tượng từ abstract class
# - Dùng để định nghĩa khuôn mẫu
# - Lớp con bắt buộc override các abstract method
# =============================================================================

print("\n===== ABSTRACT CLASS =====")

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Gâu gâu!")

class Cat(Animal):
    def speak(self):
        print("Meo meo!")

animals = [Dog(), Cat()]
for a in animals:
    a.speak()


# =============================================================================
# 2) INTERFACE KIỂU PYTHON
# - Python không có từ khóa interface
# - Nhưng có thể dùng abstract class chỉ chứa abstract method
# =============================================================================

print("\n===== INTERFACE (PYTHON STYLE) =====")

class Printable(ABC):

    @abstractmethod
    def print_info(self):
        pass

class Student(Printable):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_info(self):
        print(f"{self.name} – Điểm: {self.score}")

s = Student("Minh", 9)
s.print_info()


# =============================================================================
# 3) MULTIPLE INHERITANCE (ĐA KẾ THỪA)
# - Một class có thể kế thừa nhiều class cùng lúc
# =============================================================================

print("\n===== MULTIPLE INHERITANCE =====")

class A:
    def show(self):
        print("A.show")

class B:
    def show(self):
        print("B.show")

class C(A, B):  # kế thừa A trước rồi đến B
    pass

obj = C()
obj.show()  # ưu tiên class A trước (theo MRO)


# =============================================================================
# 4) MRO – METHOD RESOLUTION ORDER
# - Thứ tự Python tìm method trong đa kế thừa
# - Python dùng thuật toán C3 Linearization
# =============================================================================

print("\n===== MRO (Method Resolution Order) =====")

class X:
    pass

class Y:
    pass

class Z(X, Y):
    pass

print("MRO của class Z:", Z.mro())


# =============================================================================
# 5) super() NÂNG CAO
# - super() gọi phương thức cha theo MRO
# =============================================================================

print("\n===== super() NÂNG CAO =====")

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")
        super().greet()

c = Child()
c.greet()


# =============================================================================
# 6) DIAMOND PROBLEM (VẤN ĐỀ HÌNH KIM CƯƠNG)
#   A
#  / \
# B   C
#  \ /
#   D
#
# Python giải quyết bằng MRO (C3)
# =============================================================================

print("\n===== DIAMOND PROBLEM =====")

class A:
    def hello(self):
        print("A.hello")

class B(A):
    def hello(self):
        print("B.hello")
        super().hello()

class C(A):
    def hello(self):
        print("C.hello")
        super().hello()

# D kế thừa B rồi C
class D(B, C):
    def hello(self):
        print("D.hello")
        super().hello()

d = D()
d.hello()

print("\nMRO của D:", D.mro())


# =============================================================================
# 7) ABSTRACT + MULTIPLE INHERITANCE (ỨNG DỤNG THỰC TẾ)
# =============================================================================

print("\n===== ỨNG DỤNG: HỆ THỐNG THANH TOÁN =====")

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class LoggingMixin:
    def log(self, message):
        print("[LOG]:", message)

class CreditCard(PaymentMethod, LoggingMixin):
    def pay(self, amount):
        self.log(f"Thanh toán {amount} bằng Credit Card")
        print("Đã thanh toán thành công bằng thẻ!")

class MoMo(PaymentMethod, LoggingMixin):
    def pay(self, amount):
        self.log(f"Thanh toán {amount} bằng MoMo")
        print("Thanh toán MoMo thành công!")

cc = CreditCard()
momo = MoMo()

cc.pay(500_000)
momo.pay(200_000)


# =============================================================================
# 8) TÓM TẮT OOP NÂNG CAO
# =============================================================================

print("""
===================== TÓM TẮT OOP NÂNG CAO =====================

✔ ABSTRACT CLASS
    - Dùng để định nghĩa khuôn mẫu
    - Class con phải override abstract method

✔ INTERFACE (KIỂU PYTHON)
    - Abstract class chỉ chứa abstract methods

✔ MULTIPLE INHERITANCE
    - Dùng để kết hợp nhiều behavior

✔ MRO (Method Resolution Order)
    - Python tìm method theo thứ tự: Class → Cha 1 → Cha 2...
    - Dùng thuật toán C3 Linearization
    - Xem bằng: Class.mro()

✔ DIAMOND PROBLEM
    - Python giải quyết bằng MRO nên không bị lỗi

✔ super()
    - Gọi method cha theo đúng MRO
=================================================================
""")
