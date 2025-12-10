"""
===============================================================================
                  DATA SCIENCE CƠ BẢN – NumPy, Pandas, Matplotlib
Gồm:
✔ NumPy (mảng 1D, 2D, broadcasting)
✔ Pandas DataFrame
✔ Đọc CSV, mô tả dữ liệu
✔ Vẽ biểu đồ Matplotlib
===============================================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ========================= NUMPY ===============================
print("\n===== NUMPY =====")

arr = np.array([1, 2, 3])
print("Array:", arr)
print("Broadcast +10:", arr + 10)

mat = np.array([[1, 2], [3, 4]])
print("Matrix:\n", mat)
print("Matrix * 2:\n", mat * 2)

# ========================= PANDAS ===============================
print("\n===== PANDAS =====")

data = {
    "name": ["Minh", "Lan", "Hoàng"],
    "score": [8.5, 9.0, 7.8]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

print("\nMô tả thống kê:")
print(df.describe())

# ========================= MATPLOTLIB ============================
print("\n===== MATPLOTLIB =====")

plt.plot(df["name"], df["score"], marker="o")
plt.title("Điểm theo sinh viên")
plt.xlabel("Tên")
plt.ylabel("Điểm")
plt.grid()
plt.show()
