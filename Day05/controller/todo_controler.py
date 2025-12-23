from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, Response

from dependencies.db import get_db
from schemas.request.todo_schema import TodoCreate, SearchTodo, TodoUpdate

from schemas.response.error_response import ErrorSchema
from schemas.response.todo_out import TodoOut
from services.todo_service import TodoService
from ultils.response import response_success

todo_router = APIRouter(prefix="/todos", tags=["Todo Controller"])


@todo_router.post(
    "/",
    response_model=TodoOut,
    status_code=HTTPStatus.CREATED,
    responses={
        409: {"model": ErrorSchema, "description": "Todo title already exists"},
        422: {"model": ErrorSchema, "description": "Validation Error"},
    },
)
async def create_todo(
    request: TodoCreate, response: Response, db: Session = Depends(get_db)
) -> JSONResponse:
    todo = TodoService(db).create_todo(request)

    response.headers["location"] = f"/todos/{todo.id}"

    return response_success(todo.model_dump(), HTTPStatus.CREATED)


@todo_router.get(
    "/{todo_id}",
    response_model=TodoOut,
    status_code=HTTPStatus.OK,
    responses={
        404: {"model": ErrorSchema, "description": "Todo not found"},
        422: {"model": ErrorSchema, "description": "Validation Error"},
    },
)
async def get_todo(todo_id: int, db: Session = Depends(get_db)) -> JSONResponse:
    todo = TodoService(db).get_todo(todo_id)
    return response_success(todo.model_dump(), HTTPStatus.OK)


@todo_router.get(
    "/",
    response_model=list[TodoOut],
    status_code=HTTPStatus.OK,
    responses={
        422: {"model": ErrorSchema, "description": "Validation Error"},
    },
)
async def list_todos(
    db: Session = Depends(get_db), filters: SearchTodo = Depends()
) -> JSONResponse:
    todos = TodoService(db).list_todos(filters)
    return response_success(todos, HTTPStatus.OK)

@todo_router.delete(
    "/{todo_id}",
    status_code=HTTPStatus.NO_CONTENT,
)
async def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
):
    TodoService(db).delete_todo(todo_id)

@todo_router.put(
    "/{todo_id}",
    response_model=TodoOut,
    status_code=HTTPStatus.OK,
    responses={
        404: {"model": ErrorSchema, "description": "Todo not found"},
        409: {"model": ErrorSchema, "description": "Todo title already exists"},
        422: {"model": ErrorSchema, "description": "Validation Error"},
    },
)
async def update_todo_put(
    todo_id: int,
    request: TodoCreate,
    db: Session = Depends(get_db),
) -> JSONResponse:
    todo = TodoService(db).update_todo_put(todo_id, request)
    return response_success(todo.model_dump(), HTTPStatus.OK)


@todo_router.patch(
    "/{todo_id}",
    response_model=TodoOut,
    status_code=HTTPStatus.OK,
    responses={
        404: {"model": ErrorSchema, "description": "Todo not found"},
        409: {"model": ErrorSchema, "description": "Todo title already exists"},
        422: {"model": ErrorSchema, "description": "Validation Error"},
    },
)
async def update_todo_patch(
    todo_id: int,
    request: TodoUpdate,
    db: Session = Depends(get_db),
) -> JSONResponse:
    todo = TodoService(db).update_todo_patch(todo_id, request)
    return response_success(todo.model_dump(), HTTPStatus.OK)
