# class student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#         self.school = "DAU"
#
#
#     def helo(self):
#         print("Hello, my name is %s" % self.name)
#
# s1 = student("A", 100)
# s2 = student("B", 100)
#
# print(s1.name, s1.score, s1.school)
# print(s2.name, s2.score, s2.school)
# s1.helo()
# s2.helo()
#dong goi
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance   # private
#
#     def get_balance(self):
#         return self.__balance
#
# acc = BankAccount(1000)
# print(acc.get_balance())
#get set
# class Person:
#     def __init__(self, age):
#         self._age = age
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if value < 0:
#             raise ValueError("Age must be positive")
#         self._age = value
#
# p = Person(20)
# p.age = 30
# print(p.age)
#ke thua
# class Animal:
#     def speak(self):
#         print("Animal sound")
#
# class Dog(Animal):
#     def speak(self):
#         print("Gâu gâu")
#
# d = Dog()
# d.speak()
#da hinh
# class Cat:
#     def speak(self):
#         return "Meo"
#
# class Dog:
#     def speak(self):
#         return "Gâu"
#
# animals = [Cat(), Dog()]
# for a in animals:
#     print(a.speak())   # tùy class mà output khác nhau
#truu tuong
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         print("Gâu gâu")
#
# class Cat(Animal):
#     def speak(self):
#         print("Meo Meo Meo")
#
# Cat().speak()
#static method va class method
class MathUtil:

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def hello(cls):
        print("This is class:", cls.__name__)

print(MathUtil.add(2, 3))
MathUtil.hello()




