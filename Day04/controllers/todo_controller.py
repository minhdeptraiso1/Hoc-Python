from typing import List, Optional

from fastapi import APIRouter, Query

from schemas.err_schema.errroresponse import ErrorResponse
from schemas.todo_schema.todo_create import TodoCreate
from schemas.todo_schema.todo_out import TodoOut
from schemas.todo_schema.todo_search import SearchTodo
from schemas.todo_schema.todo_update import TodoUpdate
from services import todo_service

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
        limit: Optional[int] = Query(10, description="Limit"),
):
    search = SearchTodo(done=done, keyword=keyword, limit=limit)
    return todo_service.get_all_by_keyword(search)
