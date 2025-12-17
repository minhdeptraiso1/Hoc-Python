import uvicorn
from fastapi import FastAPI

from controllers.todo_controller import todo_router

app = FastAPI(
    title="Todo API",
    description="A simple Todo API with FastAPI",
    version="1.0.0")
app.include_router(todo_router, prefix="/todos", tags=["Todos"])

if __name__ == '__main__':
    uvicorn.run(
        "main:app",  # Tên file:tên app variable
        # host="0.0.0.0",  # Cho phép truy cập từ mọi IP
        host="127.0.0.1",
        port=8000,
        reload=True  # Auto-reload khi code thay đổi (chỉ dùng development)
    )
