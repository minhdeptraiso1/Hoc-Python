"""
===============================================================================
             MACHINE LEARNING NÂNG CAO – sklearn
Gồm:
✔ Support Vector Machine (SVM)
✔ Random Forest
✔ Neural Network (MLPClassifier)
✔ Confusion Matrix + Accuracy
===============================================================================
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

# Load dữ liệu Iris
iris = load_iris()
X = iris.data
y = iris.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# ------------------ SVM ------------------
print("\n===== SVM CLASSIFIER =====")
svm = SVC(kernel="rbf")
svm.fit(X_train, y_train)
pred_svm = svm.predict(X_test)
print("Accuracy SVM =", accuracy_score(y_test, pred_svm))
print("Confusion Matrix:\n", confusion_matrix(y_test, pred_svm))

# ---------------- Random Forest -------------
print("\n===== RANDOM FOREST =====")
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)
pred_rf = rf.predict(X_test)
print("Accuracy RandomForest =", accuracy_score(y_test, pred_rf))

# ----------------- Neural Network -----------
print("\n===== MLP NEURAL NETWORK =====")
mlp = MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=1000)
mlp.fit(X_train, y_train)
pred_mlp = mlp.predict(X_test)
print("Accuracy MLP =", accuracy_score(y_test, pred_mlp))

print("\nDONE!")
