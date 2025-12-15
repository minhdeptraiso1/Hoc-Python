from file_utils import read_file_content, count_word_frequency, get_top_words


def main():

    file_name = input("Nhập tên file cần phân tích: ")
    while True:
        try:
            file_choice = int(
                input("Chọn kiểu file: \n 1. file.txt \n 2. file.sgv \n 3. file.exe\n Lựa chọn của bạn: "))

            if file_choice == 1:
                file_type = ".txt"
                break
            elif file_choice == 2:
                file_type = ".sgv"
                break
            elif file_choice == 3:
                file_type = ".exe"
                break
            else:
                print("Lựa chọn không hợp lệ! Vui lòng chọn 1, 2 hoặc 3.")
        except ValueError:
            print("Vui lòng nhập số nguyên (1, 2 hoặc 3)!")

    file = file_name + file_type
    try:
        content = read_file_content(file)

        frequency = count_word_frequency(content)

        total_words = sum(frequency.values())

        top_words = get_top_words(frequency, 10)

        print(f"\nTổng số từ: {total_words}")
        print("Top 10 từ xuất hiện nhiều nhất:")

        for word, count in top_words:
            print(f"- {word}: {count}")

    except FileNotFoundError:
        print(f"Lỗi: File '{file}' không tồn tại!")

    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")


if __name__ == "__main__":
    main()