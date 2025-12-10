"""
===============================================================================
               DEPLOY MACHINE LEARNING MODEL VIA API + DOCKER
Gồm:
✔ Train model (sklearn)
✔ Lưu model (pickle)
✔ API FastAPI để predict
✔ Dockerfile để build image
===============================================================================
"""

from fastapi import FastAPI
import numpy as np
import pickle
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# ---------------------- TRAIN MODEL ----------------------
print("\nTraining model...")

iris = load_iris()
X, y = iris.data, iris.target

model = KNeighborsClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))
print("Model saved!")

# ---------------------- FASTAPI -------------------------
app = FastAPI()

@app.post("/predict")
def predict(values: list):
    arr = np.array([values])
    model = pickle.load(open("model.pkl", "rb"))
    pred = model.predict(arr)[0]
    return {"prediction": iris.target_names[pred]}


"""
---------------------- DOCKERFILE -------------------------

FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "deploy_ml_api_docker:app", "--host", "0.0.0.0", "--port", "8000"]
-----------------------------------------------------------

Build Docker image:
    docker build -t ml-api .

Run container:
    docker run -p 8000:8000 ml-api

Test API:
    POST http://127.0.0.1:8000/predict
    Body → [5.1, 3.5, 1.4, 0.2]
===============================================================================
"""
