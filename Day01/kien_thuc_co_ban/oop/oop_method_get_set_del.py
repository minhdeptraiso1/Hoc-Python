"""
===========================================
   OOP NÂNG CAO TRONG PYTHON – FILE TỔNG HỢP
   Gồm:
   ✔ Class Method
   ✔ Static Method
   ✔ Overriding
   ✔ Overloading (mô phỏng)
   ✔ Property Getter / Setter
===========================================
"""


# ======================================================
# 1) CLASS METHOD – STATIC METHOD
# ======================================================

class Student:
    # Biến cấp lớp (class variable)
    # ---> Gắn với class chứ không phải từng object
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1  # tăng số lượng sinh viên

    # CLASS METHOD
    # Dùng @classmethod
    # Tham số đầu tiên là "cls" (đại diện cho class Student)
    @classmethod
    def get_count(cls):
        return cls.count

    # STATIC METHOD
    # Không có self, không có cls
    # Dùng cho các hàm tiện ích (utility)
    @staticmethod
    def welcome():
        print("Chào mừng bạn đến lớp học Python!")


# ======================================================
# 2) OVERRIDING – CLASS CON GHI ĐÈ METHOD CỦA CLASS CHA
# ======================================================

class Animal:
    def speak(self):
        print("Động vật phát ra âm thanh chung chung")


class Dog(Animal):
    # Ghi đè hàm speak() của class cha
    def speak(self):
        print("Gâu gâu – Tôi là chó")


class Cat(Animal):
    def speak(self):
        print("Meo meo – Tôi là mèo")


# ======================================================
# 3) OVERLOADING (MÔ PHỎNG)
# Python KHÔNG hỗ trợ overloading thật sự
# Nhưng ta mô phỏng bằng default params hoặc *args
# ======================================================

class Calculator:
    # Overloading kiểu default argument
    def add(self, a, b, c=0):
        return a + b + c

    # Overloading kiểu dùng *args
    def add_all(self, *numbers):
        return sum(numbers)


# ======================================================
# 4) PROPERTY GETTER – SETTER – DELETER
# Dùng để đóng gói dữ liệu + kiểm soát truy cập
# ======================================================

class Person:
    def __init__(self, age):
        self._age = age  # thuộc tính private-like

    # GETTER
    @property
    def age(self):
        return self._age

    # SETTER – kiểm soát giá trị gán vào
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Tuổi không được âm!")
        self._age = value

    # DELETER
    @age.deleter
    def age(self):
        print("Đang xóa thuộc tính age...")
        del self._age


# ======================================================
# DEMO CHẠY THỰC TẾ
# ======================================================
if __name__ == "__main__":

    print("\n===== DEMO CLASS METHOD & STATIC METHOD =====")
    s1 = Student("Minh")
    s2 = Student("Lan")
    Student.welcome()
    print("Số lượng sinh viên:", Student.get_count())

    print("\n===== DEMO OVERRIDING =====")
    animals = [Dog(), Cat(), Animal()]
    for a in animals:
        a.speak()

    print("\n===== DEMO OVERLOADING MÔ PHỎNG =====")
    calc = Calculator()
    print("2 số:", calc.add(3, 5))
    print("3 số:", calc.add(3, 5, 7))
    print("Nhiều số:", calc.add_all(1, 2, 3, 4, 5))

    print("\n===== DEMO PROPERTY =====")
    p = Person(20)
    print("Tuổi hiện tại:", p.age)  # gọi getter

    p.age = 25  # gọi setter
    print("Tuổi sau cập nhật:", p.age)

    # del p.age  # xóa thuộc tính (nếu muốn thử)
