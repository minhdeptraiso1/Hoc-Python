"""
===========================================================================
                TỔNG HỢP THUẬT TOÁN CƠ BẢN – SORT & SEARCH
Gồm:
✔ Linear Search
✔ Binary Search
✔ Bubble Sort
✔ Selection Sort
✔ Insertion Sort
✔ Merge Sort
✔ Quick Sort
Giải thích dễ hiểu + ví dụ trực tiếp
===========================================================================
"""

# ========================================================================
# 1) LINEAR SEARCH (Tìm tuyến tính)
# - Duyệt từng phần tử từ trái → phải
# - Đơn giản, áp dụng mọi trường hợp
# ========================================================================

print("\n===== LINEAR SEARCH =====")

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # trả về vị trí
    return -1          # không tìm thấy

numbers = [5, 2, 9, 1, 7]
print("Mảng:", numbers)
print("Tìm số 9:", linear_search(numbers, 9))
print("Tìm số 3:", linear_search(numbers, 3))


# ========================================================================
# 2) BINARY SEARCH (Tìm nhị phân)
# - Yêu cầu: mảng phải SORT trước
# - Chia đôi → so sánh → thu hẹp phạm vi
# ========================================================================

print("\n===== BINARY SEARCH =====")

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_arr = [1, 2, 5, 7, 9, 12]
print("Mảng đã sắp xếp:", sorted_arr)
print("Tìm số 7:", binary_search(sorted_arr, 7))


# ========================================================================
# 3) BUBBLE SORT
# - So sánh từng cặp phần tử → đổi chỗ nếu sai
# - Dễ hiểu nhất nhưng chậm
# ========================================================================

print("\n===== BUBBLE SORT =====")

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:        # nếu sai thứ tự → đổi chỗ
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print("Bubble Sort:", bubble_sort(numbers))


# ========================================================================
# 4) SELECTION SORT
# - Chọn phần tử nhỏ nhất và đưa về đầu
# ========================================================================

print("\n===== SELECTION SORT =====")

def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print("Selection Sort:", selection_sort(numbers))


# ========================================================================
# 5) INSERTION SORT
# - Chèn từng phần tử vào đúng vị trí
# - Tốt cho dữ liệu gần như đã sắp xếp
# ========================================================================

print("\n===== INSERTION SORT =====")

def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Dịch chuyển các phần tử lớn hơn key sang phải
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr

print("Insertion Sort:", insertion_sort(numbers))


# ========================================================================
# 6) MERGE SORT (Chia để trị)
# - Chia đôi mảng → sort từng nửa → trộn lại
# - Rất nhanh và ổn định
# ========================================================================

print("\n===== MERGE SORT =====")

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])      # sort nửa trái
    right = merge_sort(arr[mid:])     # sort nửa phải

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # So sánh và trộn hai nửa lại
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Thêm phần còn lại
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print("Merge Sort:", merge_sort(numbers))


# ========================================================================
# 7) QUICK SORT (Nhanh nhất trong thực tế)
# - Chọn pivot (điểm chốt)
# - Chia mảng thành 2 phần < pivot và > pivot
# - Sort đệ quy
# ========================================================================

print("\n===== QUICK SORT =====")

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]   # chọn phần tử giữa làm pivot
    left = [x for x in arr if x < pivot]
    mid  = [x for x in arr if x == pivot]
    right= [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)

print("Quick Sort:", quick_sort(numbers))


# ========================================================================
# 8) TÓM TẮT ƯU NHƯỢC ĐIỂM
# ========================================================================

print("""
=================== TÓM TẮT SORT & SEARCH ===================

SEARCH:
- Linear Search: dễ, nhưng chậm (O(n))
- Binary Search: rất nhanh (O(log n)), nhưng cần mảng đã sort

SORT:
- Bubble Sort: dễ hiểu, chậm → dùng học thuật toán
- Selection Sort: đơn giản, không ổn định
- Insertion Sort: tốt cho mảng gần như sort
- Merge Sort: nhanh, ổn định, O(n log n)
- Quick Sort: nhanh nhất thực tế, trung bình O(n log n)

==============================================================
""")
