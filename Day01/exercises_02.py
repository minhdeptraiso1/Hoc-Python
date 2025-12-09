
# Bài tập 2: Tính tổng S = 1 + 1/3! + 1/5! + ... + 1/(2n−1)!

# > **Đề bài:**
# > Viết chương trình tính `S = 1 + 1/3! + 1/5! + ... + 1/(2n−1)!`, với n được nhập từ bàn phím
#
# ---

def factorial(n: int) -> float:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Nhập n: "))

S = 1

for i in range(2, n + 1):
    odd_number = 2 * i - 1
    S += 1 / factorial(odd_number)

print("Tong S =", S)


