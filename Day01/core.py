import string


# khai bao bien
name = "Minh"
age = 22
print(name, age)
# cau lenh dieu kien
if age > 22:
    print("lon hon 22")
elif age == 22:
    print("bang 22")
else:
    print("nho hon 22")

# toan tu 3 ngoi
print("lon hon 22" if age > 22 else "nho hon 22")

status = "dep trai" if not age > 22 else "xau trai"
print(status)

# vong lap
for i in range(5):
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1



#ham (function)

def xin_chao(x: string) -> string:
    print("xin chao" , x)

xin_chao("minh")

#list
fruits = ["apple", "banana", "orange"]
print(fruits[0])

#dict
student = {
    "name": "Minh",
    "age": 22,
    "class": "CT3"
}

print(student["name"])

#input

ho_va_ten = input("Ten cua ban :")
print(ho_va_ten)


a = int(input("nhap so a :"))
b = int(input("nhap so b :"))
c = a + b
print("Tong cua " ,a ," va " ,b ,"bang " ,c)
