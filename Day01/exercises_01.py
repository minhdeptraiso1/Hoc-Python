# Bài tập 1: Kiểm tra và tìm ngày kế tiếp, ngày trước đó

## Đề bài:
# > * Nhập vào thông tin 1 ngày (ngày – tháng – năm)
# > * Kiểm tra ngày có hợp lệ hay không?
# > * Nếu hợp lệ hãy tìm ra ngày kế tiếp (ngày – tháng – năm) & ngày trước đó (ngày – tháng – năm)
#
# ### Hướng dẫn các bước thực hiện
#
# * Bước 1: Nhập vào ngày, tháng, năm từ bàn phím
# * Bước 2: Kiểm tra xem ngày, tháng, năm nhập vào có hợp lệ hay không. Cần xác định số ngày tối đa của mỗi tháng (lưu ý tháng 2 trong năm nhuận), và xem xét liệu ngày nhập vào có vượt quá số ngày tối đa đó hay không
# * Bước 3: Nếu ngày, tháng, năm hợp lệ, tìm ngày kế tiếp và ngày trước đó
#   * Để tìm ngày kế tiếp, có thể tăng ngày lên 1
#     * Nếu ngày vượt quá số ngày tối đa của tháng, đặt lại ngày về 1 và tăng tháng lên 1
#     * Nếu tháng vượt quá 12, đặt lại tháng về 1 và tăng năm lên 1
#   * Để tìm ngày trước đó, có thể giảm ngày đi 1
#     * Nếu ngày nhỏ hơn 1, đặt ngày về ngày cuối của tháng trước và giảm tháng đi 1
#     * Nếu tháng nhỏ hơn 1, đặt tháng về 12 và giảm năm đi 1
# * Bước 4: In ngày kế tiếp và ngày trước đó ra màn hình console
#
# ---
def check_is_leap_year(year: int) -> bool:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

day_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

def next_day(day: int, month: int, year: int):
    if day == day_in_month[month] and month < 12:
        return 1, month + 1, year
    elif day == day_in_month[month] and month == 12:
        return 1, 1, year + 1
    else:
        return day + 1, month, year

def back_day(day: int, month: int, year: int):
    if day > 1:
        return day - 1, month, year

    if month > 1:
        return day_in_month[month - 1], month - 1, year
    else:
        return 31, 12, year - 1

def valid_date(day: int, month: int, year: int) -> bool:
    if month < 1 or month > 12:
        return False
    if day < 1 or day > day_in_month[month]:
        return False
    if year < 1 :
        return False
    return True


day = int(input("Nhap ngay: "))
month = int(input("Nhap thang: "))
year = int(input("Nhap nam: "))


day_in_month[2] = 29 if check_is_leap_year(year) else 28

if not valid_date(day, month, year):
    print("Ngay ko dung")
    exit()

print("Ngay dung")

print("Ngay ke tiep:", next_day(day, month, year))
print("Ngay truoc do:", back_day(day, month, year))


