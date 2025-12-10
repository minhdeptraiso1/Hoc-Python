"""
===============================================================================
                      FULL MLOPS PIPELINE — Kubeflow

Xây dựng pipeline MLOps chuyên nghiệp

3 bước chuẩn ML: Load → Train → Evaluate

Kubeflow pipeline (YAML) để deploy trên Kubernetes

Đây là tiêu chuẩn cho AI Enterprise
===============================================================================
"""

from kfp import dsl
import kfp

# ===================== STEP 1: LOAD DATA =====================

@dsl.component
def load_data_op():
    import pandas as pd
    df = pd.read_csv("data.csv")
    print("Loaded:", df.shape)
    return df.to_json()


# ===================== STEP 2: TRAIN =========================

@dsl.component
def train_model_op(data_json: str):
    import pandas as pd
    import pickle
    from sklearn.linear_model import LogisticRegression

    df = pd.read_json(data_json)
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    model = LogisticRegression()
    model.fit(X, y)

    pickle.dump(model, open("/mnt/model.pkl", "wb"))
    return "model_saved"


# ===================== STEP 3: EVALUATE ======================

@dsl.component
def evaluate_op():
    import pickle
    import numpy as np

    model = pickle.load(open("/mnt/model.pkl", "rb"))
    pred = model.predict([[1, 2, 3]])
    print("Test prediction:", pred)


# ===================== PIPELINE ==============================

@dsl.pipeline(name="ML Kubeflow Pipeline")
def pipeline():
    data = load_data_op()
    train = train_model_op(data.output)
    evaluate = evaluate_op().after(train)


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(pipeline, "ml_pipeline.yaml")
