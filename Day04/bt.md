* Tạo `.venv`:

```bash
    python -m venv .venv
```

* Kích hoạt `.venv`
    * Windows:
        * PowerShell / CMD: `.\.venv\Scripts\activate`
        * Git Bash: `source .venv/Scripts/activate`
    * Linux/Mac: `source .venv/bin/activate`

Sau khi kích hoạt, terminal sẽ có (`.venv`)

* Lưu ý KHÔNG commit `(.venv)`
    * Không chia sẻ qua Git
    * Dùng `requirements.txt` để install thư viện
        * `pip install -r requirements.txt`

```bash
    pip install fastapi uvicorn
```

Tạo / cập nhật file `requirements.txt`:

* Sau khi đã cài các thư viện cần thiết => chạy lệnh:
    * `pip freeze > requirements.txt`
    * Trong đó:
        * `pip freeze`: tạo danh sách các gói thư viện theo format chuẩn
      ```text
          fastapi==0.124.2
          uvicorn==0.38.0
          pydantic==2.12.5
          starlette==0.50.0
          anyio==4.12.0
          ...
      ```
        * Toán tử `>` (của terminal): chuyển toàn bộ nội dung đó vào file `requirements.txt`

Như vậy các máy của dev khác chỉ cần kích hoạt `.venv` và chạy `pip install -r requirements.txt` để cài toàn bộ thư viện
Tạo file `main.py` ở thư mục gốc dự án

```python
from fastapi import FastAPI

from controllers.todo_controller import todo_router

app = FastAPI(
    title="Todo API",
    description="A simple Todo API with FastAPI",
    version="1.0.0")
app.include_router(todo_router, prefix="/todos", tags=["Todos"])

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",  # Tên file:tên app variable
        # host="0.0.0.0",  # Cho phép truy cập từ mọi IP
        host="127.0.0.1",
        port=8000,
        reload=True  # Auto-reload khi code thay đổi (chỉ dùng development)
    )
```

Tạo file `ultils.py` ở thư mục gốc dự án

```python
from fastapi import HTTPException
from typing import List, Optional


def exists_title(title: str, _todos: List[dict], exclude_id: Optional[int] = None) -> None:
    """
    Kiểm tra title đã tồn tại trong _todos hay chưa.

    Args:
        title (str): title cần check
        _todos (List[dict]): danh sách todo hiện tại
        exclude_id (Optional[int]): nếu truyền, bỏ qua item có id này (dùng khi update)

    Raises:
        HTTPException: status 400 nếu title đã tồn tại
    """
    for t in _todos:
        if t["title"] == title:
            if exclude_id is None or t["id"] != exclude_id:
                raise HTTPException(status_code=400, detail="Title already exists")


def id_is_exists(id: int, _todos: list[dict]) -> dict:
    """
    Kiểm tra id có tồn tại trong _todos hay chưa và lấy ra todo.

    Args:
        id (int): id cần check
        _todos (list[dict]): danh sách todo hiện tại
    Raises:
        HTTPException: status 400 nếu ko tìm thấy id
    """
    for t in _todos:
        if t["id"] == id:
            return t
    raise HTTPException(status_code=404, detail="Id does not found")

```

Tạo file service

```python
from fastapi import HTTPException

from schemas.todo_schema.get_todo_by_keyword import SearchTodo
from schemas.todo_schema.todo_create import TodoCreate
from schemas.todo_schema.todo_out import TodoOut
from schemas.todo_schema.todo_update import TodoUpdate
from ultils.todo_ultils import exists_title, id_is_exists

_todos: list[dict] = []
_id_counter = 1


def create_todo(todo: TodoCreate) -> TodoOut:
    global _id_counter
    exists_title(todo.title, _todos)
    stored_todo = {
        "id": _id_counter,
        "title": todo.title,
        "description": todo.description,
        "priority": todo.priority,
        "done": todo.done,
    }
    _todos.append(stored_todo)
    _id_counter += 1
    return TodoOut(**stored_todo)


def update_todo_patch(id: int, todo: TodoUpdate) -> TodoOut:
    item = id_is_exists(id, _todos)
    if todo.title is not None:
        exists_title(todo.title, _todos, exclude_id=id)
        item["title"] = todo.title
    if todo.description is not None:
        item["description"] = todo.description
    if todo.priority is not None:
        item["priority"] = todo.priority
    if todo.done is not None:
        item["done"] = todo.done

    return TodoOut(**item)


def update_todo_put(id: int, todo: TodoCreate) -> TodoOut:
    item = id_is_exists(id, _todos)
    exists_title(todo.title, _todos, exclude_id=id)
    item.update({
        "title": todo.title,
        "description": todo.description,
        "priority": todo.priority,
        "done": todo.done
    })

    return TodoOut(**item)


def delete_todo(id: int) -> None:
    _todos.remove(id_is_exists(id, _todos))


def get_todo_by_id(id: int) -> TodoOut:
    return TodoOut(**id_is_exists(id, _todos))


def get_all_by_keyword(search: SearchTodo) -> list[TodoOut]:
    results = _todos.copy()

    if search.done is not None:
        results = [t for t in results if t["done"] == search.done]

    if search.keyword:
        keyword_lower = search.keyword.lower()
        results = [t for t in results if keyword_lower in t["title"].lower()]

    return [TodoOut(**t) for t in results]

```

Tạo schema

```python

from typing import Optional
from pydantic import BaseModel, Field


class SearchTodo(BaseModel):
    done: Optional[bool] = Field(None, description="Status todo: true/false")
    keyword: Optional[str] = Field(None, description="Keyword to search")

    class Config:
        json_schema_extra = {
            "example": {
                "done": True,
                "keyword": "go to"
            }
        }

```

```python

from typing import Optional
from pydantic import BaseModel, Field


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=200, description="title todo")
    description: Optional[str] = Field(None, max_length=1000, description="description todo")
    priority: int = Field(1, ge=1, le=5, description="lv todo 1 - 5")
    done: bool = Field(False, description="done : true/false")

    class Config:
        json_schema_extra = {
            "title": "go to techzen",
            "description": "go to techzen at 8:30 am",
            "priority": 3,
            "done": False,
        }

```

```python
from pydantic import Field, BaseModel
from typing import Optional


class TodoOut(BaseModel):
    id: int = Field(..., description="Id task")
    title: str
    description: Optional[str]
    priority: int
    done: bool

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Complete project",
                "description": "Finish the FastAPI todo app",
                "priority": 3,
                "done": False
            }
        }


```

```python

from typing import Optional
from pydantic.v1 import BaseModel, Field


class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=200, description="title todo")
    description: Optional[str] = Field(None, max_length=1000, description="description todo")
    priority: Optional[int] = Field(1, ge=1, le=5, description="lv todo 1 - 5")
    done: Optional[bool] = Field(False, description="done : true/false")

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Buy groceries",
                "description": "Milk, eggs, bread",
                "priority": 2,
                "done": False
            }
        }
```

Tạo errresponse

```python
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    str: str
```

Tạo controller

```python

from typing import List, Optional
from fastapi import APIRouter, Query

from schemas.err_schema.error_response import ErrorResponse
from schemas.todo_schema.get_todo_by_keyword import SearchTodo
from schemas.todo_schema.todo_create import TodoCreate
from schemas.todo_schema.todo_out import TodoOut
from schemas.todo_schema.todo_update import TodoUpdate
from service import todo_service

todo_router = APIRouter()


@todo_router.post("", status_code=201, response_model=TodoOut, responses={
    400: {"model": ErrorResponse, "description": "Invalid input on business logic"}
}, )
def create_todo(todo: TodoCreate) -> TodoOut:
    return todo_service.create_todo(todo)


@todo_router.patch("/{id}", status_code=200, response_model=None, responses={
    400: {"model": ErrorResponse, "description": "Invalid input on business logic"}
})
def update_todo_patch(id: int, todo: TodoUpdate) -> TodoOut:
    return todo_service.update_todo_patch(id, todo)


@todo_router.put("/{id}", status_code=200, response_model=None, responses={
    400: {"model": ErrorResponse, "description": "Invalid input on business logic"}
})
def update_todo_put(id: int, todo: TodoCreate) -> TodoOut:
    return todo_service.update_todo_put(id, todo)


@todo_router.delete("/{id}", status_code=204, response_model=None, responses={
    400: {"model": ErrorResponse, "description": "Invalid input on business logic"}
})
def delete_todo(id: int) -> None:
    return todo_service.delete_todo(id)


@todo_router.get("/{id}", status_code=200, response_model=None, responses={
    400: {"model": ErrorResponse, "description": "Invalid input on business logic"}
})
def get_todo(id: int) -> TodoOut:
    return todo_service.get_todo_by_id(id)


@todo_router.get("/", response_model=List[TodoOut])
def get_todos(
        done: Optional[bool] = Query(None, description="Status todo: true/false"),
        keyword: Optional[str] = Query(None, description="Keyword to search"),
):
    search = SearchTodo(done=done, keyword=keyword)
    return todo_service.get_all_by_keyword(search)

```