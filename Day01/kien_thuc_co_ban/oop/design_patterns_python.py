"""
====================================================================================
                 TỔNG HỢP DESIGN PATTERNS TRONG PYTHON – FULL CODE
Gồm:
✔ Singleton
✔ Factory Method
✔ Abstract Factory
✔ Builder Pattern
✔ Adapter Pattern
✔ Facade Pattern
✔ Decorator Pattern (OOP)
✔ Observer Pattern
✔ Strategy Pattern
✔ Command Pattern
====================================================================================
"""

print("\n===================== CREATIONAL PATTERNS =====================\n")

# =============================================================================
# 1) SINGLETON PATTERN
# - Đảm bảo một class chỉ có 1 instance duy nhất
# =============================================================================

print("----- SINGLETON PATTERN -----")

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()

print("Có phải là cùng instance?:", a is b)


# =============================================================================
# 2) FACTORY METHOD
# - Tạo object mà không cần biết class con cụ thể
# =============================================================================

print("\n----- FACTORY METHOD -----")

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Gâu gâu"

class Cat(Animal):
    def speak(self):
        return "Meo meo"

class AnimalFactory:
    @staticmethod
    def create(animal_type):
        if animal_type == "dog":
            return Dog()
        if animal_type == "cat":
            return Cat()
        return None

animal = AnimalFactory.create("dog")
print("Factory tạo đối tượng:", animal.speak())


# =============================================================================
# 3) ABSTRACT FACTORY
# - Tạo nhóm object liên quan với nhau
# =============================================================================

print("\n----- ABSTRACT FACTORY -----")

class Button:
    def click(self): pass

class WinButton(Button):
    def click(self): return "Windows Button Click!"

class MacButton(Button):
    def click(self): return "Mac Button Click!"

class GUIFactory:
    def create_button(self): pass

class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

def client_code(factory):
    btn = factory.create_button()
    print(btn.click())

client_code(WinFactory())
client_code(MacFactory())


# =============================================================================
# 4) BUILDER PATTERN
# - Xây dựng object phức tạp theo từng bước
# =============================================================================

print("\n----- BUILDER PATTERN -----")

class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.gpu = None

    def __str__(self):
        return f"CPU={self.cpu}, RAM={self.ram}, GPU={self.gpu}"

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def add_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def add_ram(self, ram):
        self.computer.ram = ram
        return self

    def add_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def build(self):
        return self.computer

pc = ComputerBuilder().add_cpu("i7").add_ram("16GB").add_gpu("RTX 3060").build()
print("PC:", pc)


print("\n===================== STRUCTURAL PATTERNS =====================\n")

# =============================================================================
# 5) ADAPTER PATTERN
# - Chuyển đổi interface để 2 class không tương thích có thể làm việc cùng nhau
# =============================================================================

print("----- ADAPTER PATTERN -----")

class EuropeanPlug:
    def voltage(self):
        return 220

class USAPlug:
    def voltage(self):
        return 110

class Adapter:
    def __init__(self, plug):
        self.plug = plug

    def voltage(self):
        return self.plug.voltage() * 2  # adapter chuyển đổi

eu = EuropeanPlug()
us = USAPlug()

adapter = Adapter(us)
print("Điện áp sau adapter:", adapter.voltage())


# =============================================================================
# 6) FACADE PATTERN
# - Ẩn sự phức tạp bên trong hệ thống bằng 1 lớp đơn giản
# =============================================================================

print("\n----- FACADE PATTERN -----")

class CPU:
    def start(self): print("CPU started")

class RAM:
    def load(self): print("RAM loaded")

class HardDisk:
    def read(self): print("Hard disk reading")

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
        self.disk = HardDisk()

    def start(self):
        self.cpu.start()
        self.ram.load()
        self.disk.read()
        print("Computer started!")

pc = ComputerFacade()
pc.start()


# =============================================================================
# 7) DECORATOR PATTERN (OOP)
# - Thêm hành vi cho đối tượng mà không sửa lớp gốc
# *KHÁC VỚI decorator function trong Python!*
# =============================================================================

print("\n----- DECORATOR PATTERN (OOP) -----")

class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 2

class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 1

coffee = Coffee()
coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)

print("Giá cà phê:", coffee.cost())


print("\n===================== BEHAVIORAL PATTERNS =====================\n")

# =============================================================================
# 8) OBSERVER PATTERN
# - Khi object thay đổi → thông báo cho tất cả observer
# =============================================================================

print("----- OBSERVER PATTERN -----")

class Subject:
    def __init__(self):
        self.observers = []

    def add(self, observer):
        self.observers.append(observer)

    def notify(self, msg):
        for o in self.observers:
            o.update(msg)

class Observer:
    def update(self, msg):
        print("Nhận thông báo:", msg)

subject = Subject()
subject.add(Observer())
subject.add(Observer())

subject.notify("Có sự kiện mới!")


# =============================================================================
# 9) STRATEGY PATTERN
# - Thay đổi thuật toán lúc runtime
# =============================================================================

print("\n----- STRATEGY PATTERN -----")

class Add:
    def calc(self, a, b): return a + b

class Multiply:
    def calc(self, a, b): return a * b

class Calculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, a, b):
        return self.strategy.calc(a, b)

print("Add:", Calculator(Add()).execute(3, 4))
print("Multiply:", Calculator(Multiply()).execute(3, 4))


# =============================================================================
# 10) COMMAND PATTERN
# - Đóng gói lệnh thành object → dễ undo/redo
# =============================================================================

print("\n----- COMMAND PATTERN -----")

class Command:
    def execute(self): pass

class LightOn(Command):
    def execute(self):
        print("Bật đèn!")

class LightOff(Command):
    def execute(self):
        print("Tắt đèn!")

class Remote:
    def submit(self, command):
        command.execute()

remote = Remote()
remote.submit(LightOn())
remote.submit(LightOff())


# =============================================================================
# TÓM TẮT
# =============================================================================

print("""
====================== TÓM TẮT DESIGN PATTERNS ======================

CREATIONAL:
- Singleton → chỉ có 1 instance
- Factory Method → tạo object linh hoạt
- Abstract Factory → tạo nhóm object liên quan
- Builder → build object phức tạp theo bước

STRUCTURAL:
- Adapter → chuyển đổi interface
- Facade → đơn giản hóa hệ thống
- Decorator (OOP) → thêm chức năng runtime

BEHAVIORAL:
- Observer → publish/subscribe
- Strategy → thay đổi thuật toán runtime
- Command → đóng gói hành vi thành object

======================================================================
""")
