"""
============================================================
   OOP CƠ BẢN TRONG PYTHON – FILE TỔNG HỢP GIẢI THÍCH CHI TIẾT
   Gồm:
   ✔ Class
   ✔ Object (instance)
   ✔ Thuộc tính (attribute)
   ✔ Phương thức (method)
   ✔ Hàm khởi tạo __init__
   ✔ Tính kế thừa (inheritance)
   ✔ Tính đa hình (polymorphism)
   ✔ Tính đóng gói (encapsulation cơ bản)
============================================================
"""


# ==========================================================
# 1) CLASS VÀ OBJECT
# Class = khuôn mẫu
# Object = đối tượng được tạo từ class
# ==========================================================

print("\n===== CLASS & OBJECT =====")

class Student:
    # Hàm khởi tạo (constructor)
    def __init__(self, name, age):
        self.name = name      # thuộc tính
        self.age = age

    # Phương thức (method)
    def introduce(self):
        print(f"Tôi là {self.name}, {self.age} tuổi")

# Tạo object
s1 = Student("Minh", 22)
s1.introduce()


# ==========================================================
# 2) THUỘC TÍNH (ATTRIBUTE)
# Thuộc tính: biến gắn với object hoặc class
# ==========================================================

print("\n===== CLASS ATTRIBUTE & INSTANCE ATTRIBUTE =====")

class Car:
    wheels = 4   # thuộc tính cấp lớp (class attribute)

    def __init__(self, brand, year):
        self.brand = brand    # thuộc tính cấp đối tượng
        self.year = year

c1 = Car("Toyota", 2020)
print("Hãng xe:", c1.brand)
print("Số bánh xe:", c1.wheels)


# ==========================================================
# 3) PHƯƠNG THỨC (METHOD)
# Method = hàm bên trong class
# Tham số đầu tiên luôn là self (đại diện object)
# ==========================================================

print("\n===== METHOD =====")

class Dog:
    def bark(self):
        print("Gâu gâu!")

d = Dog()
d.bark()


# ==========================================================
# 4) HÀM __init__ (CONSTRUCTOR)
# Tự chạy khi tạo object
# ==========================================================

print("\n===== CONSTRUCTOR (__init__) =====")

class Person:
    def __init__(self, name):
        self.name = name
        print("Object Person đã được tạo!")

p = Person("Lan")


# ==========================================================
# 5) TÍNH KẾ THỪA (INHERITANCE)
# Class con kế thừa thuộc tính + phương thức class cha
# ==========================================================

print("\n===== INHERITANCE =====")

class Animal:
    def eat(self):
        print("Động vật đang ăn")

class Cat(Animal):  # class Cat kế thừa Animal
    def speak(self):
        print("Meo meo")

my_cat = Cat()
my_cat.eat()   # phương thức từ class cha
my_cat.speak()


# ==========================================================
# 6) ĐA HÌNH (POLYMORPHISM)
# Cùng 1 phương thức nhưng xử lý khác nhau tuỳ object
# ==========================================================

print("\n===== POLYMORPHISM =====")

class Bird:
    def sound(self):
        print("Chíp chíp")

class Duck:
    def sound(self):
        print("Quạc quạc")

animals = [Bird(), Duck()]
for a in animals:
    a.sound()    # mỗi object tự xử lý theo cách riêng


# ==========================================================
# 7) ĐÓNG GÓI (ENCAPSULATION)
# Ẩn dữ liệu bên trong object
# Dùng dấu _ hoặc __ để hạn chế truy cập
# ==========================================================

print("\n===== ENCAPSULATION =====")

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print("Số dư:", acc.get_balance())


# ==========================================================
# 8) VÍ DỤ OOP CƠ BẢN HOÀN CHỈNH: QUẢN LÝ SINH VIÊN
# ==========================================================

print("\n===== OOP EXAMPLE: QUẢN LÝ SINH VIÊN =====")

class Student2:
    def __init__(self, id, name, scores):
        self.id = id
        self.name = name
        self.scores = scores

    def avg(self):
        return sum(self.scores) / len(self.scores)

    def info(self):
        print(f"{self.id} - {self.name} - Điểm TB: {self.avg():.2f}")


class StudentManager:
    def __init__(self):
        self.list = []

    def add(self, student):
        self.list.append(student)

    def show(self):
        for s in self.list:
            s.info()


# Demo
m = StudentManager()
m.add(Student2(1, "Minh", [8, 9, 7]))
m.add(Student2(2, "Lan", [9, 8, 10]))
m.show()


# ==========================================================
# 9) TÓM TẮT KIẾN THỨC OOP CƠ BẢN
# ==========================================================

print("""
================= TÓM TẮT OOP CƠ BẢN =================

✔ Class: khuôn mẫu tạo object
✔ Object: thể hiện của class
✔ Attribute: thuộc tính dữ liệu
✔ Method: hành động của object
✔ __init__: hàm khởi tạo
✔ Inheritance: class con kế thừa class cha
✔ Polymorphism: cùng tên method nhưng xử lý khác nhau
✔ Encapsulation: che giấu thông tin bằng _ hoặc __

========================================================
""")
