"""
===============================================================================
             DATA ENGINEERING PIPELINE (ETL + Airflow)

Giúp em hiểu cách xây dựng Pipeline xử lý dữ liệu chuyên nghiệp.

Nội dung:

✔ ETL: Extract → Transform → Load
✔ Lưu data dạng CSV
✔ Airflow DAG (workflow automation)
✔ Tự động hóa pipeline hàng ngày
===============================================================================
"""

# ========================= ETL PIPELINE ===============================

print("\n===== SIMPLE ETL PIPELINE =====")

import pandas as pd

def extract():
    df = pd.DataFrame({
        "name": ["Minh", "Lan", "Huy"],
        "score": [9, 8, 7]
    })
    print("Extract complete.")
    return df

def transform(df):
    df["score2"] = df["score"] * 2
    print("Transform complete.")
    return df

def load(df):
    df.to_csv("output.csv", index=False)
    print("Load complete. Data saved!")

df_raw = extract()
df_clean = transform(df_raw)
load(df_clean)


# ========================= AIRFLOW DAG ===============================

print("\n===== AIRFLOW DAG EXAMPLE =====")

"""
Lưu file: dags/etl_dag.py

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    print("Extracting...")

def transform():
    print("Transforming...")

def load():
    print("Loading...")

with DAG(
    dag_id="etl_pipeline",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    t1 = PythonOperator(task_id="extract", python_callable=extract)
    t2 = PythonOperator(task_id="transform", python_callable=transform)
    t3 = PythonOperator(task_id="load", python_callable=load)

    t1 >> t2 >> t3
"""


print("Airflow DAG demo ready!")
