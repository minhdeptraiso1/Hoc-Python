# Bài tập 3: Thao tác chuỗi

# > **Đề bài:**
# > Viết chương trình để chuẩn hoá câu:
# >* Bỏ khoảng trắng thừa (giữa các từ chỉ còn 1 khoảng trắng)
# >* Viết hoa chữ cái đầu câu
# >* Đảm bảo câu kết thúc bằng chính xác một dấu chấm “.”
# >  * Nếu thừa nhiều dấu chấm liên tiếp thì rút gọn còn “.”
# >
# > Ví dụ: "Hello worlD, this Is python.. " => "Hello world, this is python."

def normalize_sentence(s: str) -> str:
    s = s.strip() # bo khoang trang = trim()

    s = s.lower() # in thuong

    while s.endswith("."): # xoa dau cham cuoi string
        s = s[:-1]

    words = s.split() # tach thanh mang

    s = " ".join(words) #gep lai voi " "

    if len(s) > 0: # in hoa chu cai dau
        s = s[0].upper() + s[1:]

    s += "." # noi chuoi

    return s

sentence = "Hello worlD, this Is python.. "
print("Câu sau khi chuẩn hoá:", normalize_sentence(sentence))
