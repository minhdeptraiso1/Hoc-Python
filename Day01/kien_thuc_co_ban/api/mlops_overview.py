"""
===============================================================================
                         MLOps TỔNG HỢP – FULL INTRO
Gồm:
✔ Pipeline ML
✔ Tách bước ETL – Train – Evaluate – Deploy
✔ Lưu model bằng pickle / joblib
✔ Logging & Monitoring
✔ Versioning với MLflow
✔ CI/CD cho ML
✔ ví dụ pipeline ML mini
===============================================================================
"""

import pickle
import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
import mlflow


# ====================== 1) LOGGING ==========================

print("\n===== LOGGING =====")

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MLPipeline")

logger.info("Bắt đầu chạy pipeline ML...")


# ====================== 2) DATA LOADING ======================

print("\n===== LOAD DATA =====")

def load_data():
    iris = load_iris()
    X, y = iris.data, iris.target
    return train_test_split(X, y, test_size=0.2)

X_train, X_test, y_train, y_test = load_data()
logger.info("Data loaded.")


# ====================== 3) TRAIN MODEL =======================

print("\n===== TRAIN MODEL =====")

def train_model(X_train, y_train):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model

model = train_model(X_train, y_train)
logger.info("Model trained.")


# ====================== 4) EVALUATION ========================

print("\n===== EVALUATE MODEL =====")

def evaluate(model, X_test, y_test):
    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)
    logger.info(f"Accuracy = {acc}")
    return acc

accuracy = evaluate(model, X_test, y_test)


# ====================== 5) SAVE MODEL ========================

print("\n===== SAVE MODEL =====")

pickle.dump(model, open("model.pkl", "wb"))
joblib.dump(model, "model.joblib")

logger.info("Model saved!")


# ====================== 6) MLFLOW TRACKING ===================

print("\n===== MLFLOW LOGGING =====")

mlflow.set_experiment("MLExperiment")

with mlflow.start_run():
    mlflow.log_param("model", "LogisticRegression")
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "model")


# ====================== 7) PIPELINE COMPLETE =================

print("\nPipeline ML hoàn tất!")
#docker file
# FROM python:3.10
# WORKDIR /app
# COPY . .
# RUN pip install -r requirements.txt
# CMD ["python", "mlops_overview.py"]
