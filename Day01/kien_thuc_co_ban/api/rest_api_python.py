"""
===============================================================================
                 REST API with Flask & FastAPI (Python)
Gồm:
✔ API cơ bản với Flask
✔ CRUD: GET, POST, PUT, DELETE
✔ API cơ bản với FastAPI
✔ Automatic Swagger UI
===============================================================================
"""

# =============================================================================
# 1) FLASK REST API
# =============================================================================

print("\n===== FLASK REST API =====")

from flask import Flask, request, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Minh"},
    {"id": 2, "name": "Lan"}
]

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

@app.route("/students/<int:sid>", methods=["GET"])
def get_student(sid):
    for s in students:
        if s["id"] == sid:
            return jsonify(s)
    return jsonify({"error": "Not found"}), 404

@app.route("/students", methods=["POST"])
def add_student():
    data = request.json
    students.append(data)
    return jsonify({"message": "Added!"})

@app.route("/students/<int:sid>", methods=["PUT"])
def update_student(sid):
    data = request.json
    for s in students:
        if s["id"] == sid:
            s.update(data)
            return jsonify({"message": "Updated!"})
    return jsonify({"error": "Not found"}), 404

@app.route("/students/<int:sid>", methods=["DELETE"])
def delete_student(sid):
    global students
    students = [s for s in students if s["id"] != sid]
    return jsonify({"message": "Deleted!"})


"""
Chạy Flask:
    flask --app rest_api_python.py run --debug
"""


# =============================================================================
# 2) FASTAPI REST API
# =============================================================================

print("\n===== FASTAPI REST API =====")

from fastapi import FastAPI
from pydantic import BaseModel

app2 = FastAPI()

class Student(BaseModel):
    id: int
    name: str

db = [
    Student(id=1, name="Huy"),
    Student(id=2, name="Trang")
]

@app2.get("/students")
async def get_all():
    return db

@app2.get("/students/{sid}")
async def get_student(sid: int):
    for s in db:
        if s.id == sid:
            return s
    return {"error": "Not found"}

@app2.post("/students")
async def create_student(student: Student):
    db.append(student)
    return {"message": "Student created!"}

@app2.put("/students/{sid}")
async def update_student(sid: int, student: Student):
    for i, s in enumerate(db):
        if s.id == sid:
            db[i] = student
            return {"message": "Updated!"}
    return {"error": "Not found"}

@app2.delete("/students/{sid}")
async def delete_student(sid: int):
    global db
    db = [s for s in db if s.id != sid]
    return {"message": "Deleted!"}


"""
Chạy FastAPI:
    uvicorn rest_api_python:app2 --reload

Swagger UI tự tạo:
    http://127.0.0.1:8000/docs
=====================================================================
"""
