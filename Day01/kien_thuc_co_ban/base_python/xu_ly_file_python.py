"""
=================================================================================
              XỬ LÝ FILE TRONG PYTHON – TỔNG HỢP ĐẦY ĐỦ & GIẢI THÍCH CHI TIẾT
Gồm:
✔ Đọc / ghi file TXT
✔ Đọc / ghi file CSV
✔ Đọc / ghi file JSON
✔ with open
✔ append (ghi nối tiếp)
✔ xử lý lỗi file
=================================================================================
"""

import csv
import json

# =============================================================================
# 1) FILE TXT
# =============================================================================

print("\n===== FILE TXT =====")

# ----------------------
# GHI FILE TXT
# ----------------------
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Xin chào Python!\n")
    f.write("Dòng thứ 2.\n")

print("Đã ghi file TXT.")

# ----------------------
# ĐỌC FILE TXT
# ----------------------
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("Nội dung file TXT:")
print(content)

# ----------------------
# GHI NỐI TIẾP (APPEND)
# ----------------------
with open("data.txt", "a", encoding="utf-8") as f:
    f.write("Dòng mới thêm vào cuối file.\n")

print("Đã append vào file TXT.")


# =============================================================================
# 2) FILE CSV (Comma Separated Values)
# - Thường dùng cho dữ liệu dạng bảng, Excel, database export
# =============================================================================

print("\n===== FILE CSV =====")

students = [
    ["ID", "Name", "Score"],
    [1, "Minh", 8.5],
    [2, "Lan", 9.0],
    [3, "Hoàng", 7.8]
]

# ----------------------
# GHI FILE CSV
# ----------------------
with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(students)

print("Đã ghi file CSV.")

# ----------------------
# ĐỌC FILE CSV
# ----------------------
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    print("Dữ liệu CSV đọc được:")
    for row in reader:
        print(row)


# =============================================================================
# 3) FILE JSON
# - Dùng để lưu cấu trúc dữ liệu phức tạp: dict, list, object
# - JSON rất quan trọng trong API, backend, web
# =============================================================================

print("\n===== FILE JSON =====")

person = {
    "name": "Minh",
    "age": 22,
    "scores": [8, 9, 7],
    "address": {"city": "Đà Nẵng", "district": "Hải Châu"}
}

# ----------------------
# GHI FILE JSON
# ----------------------
with open("person.json", "w", encoding="utf-8") as f:
    json.dump(person, f, indent=4, ensure_ascii=False)

print("Đã ghi file JSON.")

# ----------------------
# ĐỌC FILE JSON
# ----------------------
with open("person.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Nội dung file JSON:")
print(data)


# =============================================================================
# 4) XỬ LÝ LỖI KHI ĐỌC FILE
# =============================================================================

print("\n===== XỬ LÝ LỖI FILE =====")

try:
    with open("khong_ton_tai.txt", "r") as f:
        f.read()
except FileNotFoundError:
    print("❌ File không tồn tại!")
except PermissionError:
    print("❌ Không có quyền truy cập file!")
else:
    print("File đọc thành công!")
finally:
    print("Luôn chạy dù có lỗi hay không.")


# =============================================================================
# 5) BÀI TOÁN THỰC TẾ:
#    Đọc CSV → Tính điểm TB → Lưu sang JSON
# =============================================================================

print("\n===== BÀI TOÁN THỰC TẾ: CSV → JSON =====")

# Ghi file CSV ví dụ
data = [
    ["name", "math", "english"],
    ["Minh", 8, 9],
    ["Lan", 9, 10],
    ["Hoàng", 7, 8],
]

with open("scores.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(data)

# Đọc CSV và tính điểm trung bình
students_avg = []
with open("scores.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        avg = (int(row["math"]) + int(row["english"])) / 2
        students_avg.append({
            "name": row["name"],
            "avg": avg
        })

# Lưu JSON
with open("scores_avg.json", "w", encoding="utf-8") as f:
    json.dump(students_avg, f, indent=4, ensure_ascii=False)

print("Đã chuyển CSV → JSON thành công!")


# =============================================================================
# 6) TÓM TẮT
# =============================================================================

print("""
======================== TÓM TẮT ========================

TXT:
  open(file, 'w') → ghi
  open(file, 'r') → đọc
  open(file, 'a') → ghi nối tiếp
  with open(...) → tự đóng file

CSV:
  csv.writer → ghi từng dòng
  csv.reader → đọc từng dòng
  csv.DictReader → đọc theo header

JSON:
  json.dump → ghi JSON vào file
  json.load → đọc JSON từ file

========================================================
""")
