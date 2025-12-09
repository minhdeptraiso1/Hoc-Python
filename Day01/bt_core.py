#tinh tong 1 den n
def sum_to_n(n: int) -> int:
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

n = int(input("nhap n"))
if n > 0:
    print("Tong sum =", sum_to_n(n))
else:
    print("so n khong hop le")

#kiem tra nam nhuan
def check_is_leap_year(year: int) -> bool:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

#dem ky tu
def count_char(string: str) -> int:
    string = string.lower().strip()
    if string == "":
        return 0
    else:
        count = 0
        for char in string:
            count += 1
        return count





# ham`
def say_bye(name: str) -> str:
   # print("Bye", x)
    print(f"Bye, {name}")

say_bye("Minh")
# khai bao f de {x} la kieu string
#hoac print("Name: {}, Value: {:.2f}".format(name, value))
 #gan tham so mac dinh
def power_x(base: int, exponent: int = 2) -> int:
    return base ** exponent


print(power_x(2))


# ve hinh
#tam giac can
row, col = 5, 6
for i in range(row):
    for j in range(col):
        if j <= i:
            print("*", end=" ")
        else:
            break
    print()
print()
# hinh chu nhat rong
row, col = 5, 6
for i in range(row):
    for j in range(col):
        if i == 0 or i == row - 1  or j == 0 or j == col -1 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()
# hinh vuong
row, col = 5, 5
for i in range(row):
    for j in range(col):
        print("*", end=" ")
    print()



# nhap chuoi va dem ky tu a
string_input = str(input("nhap chuoi:"))
total_string_a = 0
for char_input in string_input:
    if char_input.lower() == "a":
        print(char_input)
        total_string_a += 1
print(total_string_a)

# nhap n tinh tong 1->n
n = int(input("nhap so:"))
total = 0
if n <= 0:
    print("nhap so > 0")
for i in range(1,n+1):
    total = total + i
    print(total)
print(total)



# viết chương trình nhập tuổi
#In trẻ con (0-11)
#thiếu niên (12-17)
#thanh niên (18-30)
#nguoi gia (>30)
while True:
    old = int(input("Nhập số tuổi:"))

    if old < 0:
        print("Tuoi khong duoc < 0")
    elif old <= 11:
        print("Trẻ con")
    elif old <= 17:
        print("Thiếu niên")
    elif old <= 30:
        print("Thanh niên")
    else:
        print("Người già")

    tieptuc = input("Bạn có muốn tiếp tục? (y/n): ")

    if tieptuc.lower().strip() == "n":
        print("Kết thúc chương trình!")
        break

# giải thích :
# while + dk lặp .lower để về in thường .strip để bỏ khoảng trắng ( = .trim())

#bt2 kiểm tra chawnx lẻ dng toán tử 3 ngôi

number = int(input("Nhap so :"))
print("So khong duoc < 0")
if number < 0:
    check = "so chan" if number % 2 == 0 else "so le"
    print(check)

# toan tu 3 ngoi a = "dk dung" neu dk dung :(if 3 > 2) else "dk sai"


#bt3 kiem tra nam nhuan

year = int(input("Nhap nam:"))
if year < 0:
    print("So nam duoc < 0")
elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("nam nhuan")
else:
    print("nam khong nhuan")

# or: hoac, and: va, not: phu dinh( tuong tu !=)

# ve hinh
row, col = 5, 6
for i in range(row):
    for j in range(col):
        print(i, end=" ")
    print()

