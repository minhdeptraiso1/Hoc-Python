"""
===============================================================================
                     MACHINE LEARNING CƠ BẢN (Python + sklearn)
Gồm:
✔ Các bước ML
✔ Load dataset
✔ Train/Test split
✔ Train mô hình (Linear Regression, KNN, Decision Tree)
✔ Đánh giá mô hình
✔ Dự đoán dữ liệu mới
===============================================================================
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris, fetch_california_housing


# =============================================================================
# 1) MACHINE LEARNING WORKFLOW
# =============================================================================

print("\n===== MACHINE LEARNING WORKFLOW =====")

"""
1) Thu thập dữ liệu
2) Tiền xử lý dữ liệu
3) Chia Train/Test
4) Huấn luyện mô hình
5) Đánh giá
6) Dự đoán
"""


# =============================================================================
# 2) REGRESSION — Dự đoán giá nhà (California Housing)
# =============================================================================

print("\n===== LINEAR REGRESSION =====")

data = fetch_california_housing()
X = data.data
y = data.target

# chia dữ liệu 80% train - 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model_lr = LinearRegression()
model_lr.fit(X_train, y_train)

pred = model_lr.predict(X_test)
print("MSE =", mean_squared_error(y_test, pred))


# =============================================================================
# 3) CLASSIFICATION — Iris Dataset
# =============================================================================

print("\n===== KNN CLASSIFIER =====")

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

pred = knn.predict(X_test)
print("Accuracy KNN =", accuracy_score(y_test, pred))


# =============================================================================
# 4) DECISION TREE CLASSIFIER
# =============================================================================

print("\n===== DECISION TREE =====")

tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)

pred = tree.predict(X_test)
print("Accuracy Decision Tree =", accuracy_score(y_test, pred))


# =============================================================================
# 5) DỰ ĐOÁN MẪU MỚI
# =============================================================================

print("\n===== PREDICT NEW SAMPLE =====")

new_flower = np.array([[5.1, 3.5, 1.4, 0.2]])   # sepal & petal
predict_class = knn.predict(new_flower)

print("Dự đoán loại hoa =", iris.target_names[predict_class][0])


# =============================================================================
# TÓM TẮT
# =============================================================================

print("""
===================== TÓM TẮT MACHINE LEARNING =====================

✔ Regression → dự đoán số (Linear Regression)
✔ Classification → dự đoán nhãn (KNN, Decision Tree)
✔ sklearn → thư viện ML mạnh mẽ
✔ Các bước ML:
    - Load data
    - Train/Test split
    - Fit model
    - Predict
    - Evaluate

====================================================================
""")
