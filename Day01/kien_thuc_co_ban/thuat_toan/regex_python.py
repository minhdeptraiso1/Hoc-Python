"""
=========================================================================
                    TỔNG HỢP REGEX (REGULAR EXPRESSION) TRONG PYTHON
Gồm:
✔ Regex là gì?
✔ Các ký tự đặc biệt trong regex
✔ Ký tự lặp (*, +, ?, {m,n})
✔ Nhóm (group), OR (|), escape (\\)
✔ Các hàm quan trọng: match, search, findall, split, sub
✔ Ví dụ kiểm tra email, số điện thoại, mật khẩu, CMND
=========================================================================
"""

import re


# =========================================================================
# 1) REGEX LÀ GÌ?
# - Là ngôn ngữ dùng để tìm kiếm, so khớp chuỗi ký tự theo mẫu (pattern)
# =========================================================================

print("\n===== VÍ DỤ CƠ BẢN =====")
pattern = r"Minh"
text = "Xin chào Minh!"
match = re.search(pattern, text)
print("Tìm 'Minh' trong chuỗi:", bool(match))


# =========================================================================
# 2) CÁC KÝ TỰ ĐẶC BIỆT TRONG REGEX
# .  → bất kỳ ký tự
# \d → số (0-9)
# \D → không phải số
# \w → chữ hoặc số (_)
# \W → ký tự KHÔNG phải chữ/số
# \s → khoảng trắng
# \S → không phải khoảng trắng
# =========================================================================

print("\n===== CÁC KÝ TỰ ĐẶC BIỆT =====")

demo = "A9 b_"
print("Tất cả chữ/số:", re.findall(r"\w", demo))
print("Tất cả số:", re.findall(r"\d", demo))
print("Tất cả không phải số:", re.findall(r"\D", demo))


# =========================================================================
# 3) KÝ TỰ LẶP
# *  → lặp 0 hoặc nhiều lần
# +  → lặp 1 hoặc nhiều lần
# ?  → lặp 0 hoặc 1 lần
# {m} → lặp đúng m lần
# {m,n} → từ m đến n lần
# =========================================================================

print("\n===== KÝ TỰ LẶP =====")

print("Số điện thoại có 10 số:",
      bool(re.fullmatch(r"\d{10}", "0987654321")))

print("Từ có 3 đến 5 chữ cái:",
      re.findall(r"[A-Za-z]{3,5}", "Minh An ABC"))


# =========================================================================
# 4) NHÓM (GROUP), HOẶC (|), ESCAPE
# (abc) → nhóm
# a|b  → hoặc
# \.  → ký tự dấu chấm thật
# =========================================================================

print("\n===== NHÓM & OR =====")

print("Tìm 'cat' hoặc 'dog':",
      re.findall(r"cat|dog", "I have a cat and a dog"))

# Nhóm
print("Tìm Mr hoặc Ms:",
      re.findall(r"M(r|s)\.?\s[A-Za-z]+", "Mr Minh và Ms. Lan"))


# =========================================================================
# 5) CÁC HÀM QUAN TRỌNG TRONG re MODULE
# re.match()   → kiểm tra từ đầu chuỗi
# re.search()  → tìm bất kỳ đâu trong chuỗi
# re.findall() → tìm tất cả kết quả khớp
# re.split()   → tách chuỗi bằng regex
# re.sub()     → thay thế
# =========================================================================

print("\n===== CÁC HÀM RE =====")

text = "Xin chào Minh, Minh ơi!"
print("findall:", re.findall(r"Minh", text))
print("search:", re.search(r"Minh", text))
print("match:", re.match(r"Xin", text))  # khớp từ đầu
print("split:", re.split(r"\s", text))
print("sub:", re.sub(r"Minh", "Bạn", text))


# =========================================================================
# 6) VÍ DỤ THỰC TẾ: KIỂM TRA EMAIL
# Email hợp lệ:
# - ký tự đầu: chữ/số
# - có @
# - domain dạng: tenmien.com / tenmien.vn / ...
# =========================================================================

print("\n===== CHECK EMAIL =====")

email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$"

emails = ["minh@gmail.com", "sai@@gmail", "abc@xyz"]
for e in emails:
    print(e, "->", bool(re.fullmatch(email_pattern, e)))


# =========================================================================
# 7) KIỂM TRA SỐ ĐIỆN THOẠI VIỆT NAM (10 SỐ)
# =========================================================================

print("\n===== CHECK PHONE =====")

phone_pattern = r"^(0\d{9})$"
phones = ["0987654321", "12345", "090abc123"]
for p in phones:
    print(p, "->", bool(re.fullmatch(phone_pattern, p)))


# =========================================================================
# 8) KIỂM TRA MẬT KHẨU MẠNH
# Yêu cầu:
# - ít nhất 8 ký tự
# - có chữ hoa
# - có chữ thường
# - có số
# - có ký tự đặc biệt
# =========================================================================

print("\n===== CHECK PASSWORD =====")

password_pattern = r"""
^(?=.*[a-z])       # có chữ thường
(?=.*[A-Z])         # có chữ hoa
(?=.*\d)            # có số
(?=.*[@$!%*?&])     # có ký tự đặc biệt
[A-Za-z\d@$!%*?&]{8,}$
"""

passwords = ["Pass123!", "abc", "Password123"]
for pw in passwords:
    print(pw, "->", bool(re.fullmatch(password_pattern, pw, re.VERBOSE)))


# =========================================================================
# 9) KIỂM TRA CMND / CCCD
# CMND: 9 số
# CCCD: 12 số
# =========================================================================

print("\n===== CHECK CMND / CCCD =====")

id_pattern = r"^\d{9}|\d{12}$"

ids = ["123456789", "012345678912", "abc", "123"]
for id_num in ids:
    print(id_num, "->", bool(re.fullmatch(id_pattern, id_num)))


# =========================================================================
# 10) BÀI TOÁN THỰC TẾ: TÌM TẤT CẢ SỐ TRONG CHUỖI
# =========================================================================

print("\n===== TÌM TẤT CẢ SỐ TRONG CHUỖI =====")

text = "Tôi có 3 con mèo, 2 con chó và 12 con gà."
print("Các số tìm được:", re.findall(r"\d+", text))


# =========================================================================
# 11) TÓM TẮT REGEX THƯỜNG DÙNG
# =========================================================================

print("""
================== TÓM TẮT REGEX ==================

.     → bất kỳ ký tự
\d    → số (0–9)
\w    → chữ hoặc số
\s    → khoảng trắng
+     → lặp 1+ lần
*     → lặp 0+ lần
?     → lặp 0 hoặc 1 lần
{m,n} → lặp từ m đến n
^     → bắt đầu chuỗi
$     → kết thúc chuỗi
[]    → tập ký tự
()    → nhóm
|     → OR
====================================================
""")
