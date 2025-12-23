from http import HTTPStatus

from sqlalchemy.orm import Session

from exception.app_exception import AppException
from models import Todo
from repository import TodoRepository
from schemas.request.todo_schema import TodoCreate, SearchTodo, TodoUpdate
from schemas.response.todo_out import TodoOut


class TodoService:
    def __init__(self, db: Session):
        self.db = db
        self.todo_repository = TodoRepository(db)

    def create_todo(self, data: TodoCreate) -> TodoOut:
        if self.is_exist_by_title(data.title):
            raise AppException(
                status_code=HTTPStatus.CONFLICT,
                code="TODO_ALREADY_EXISTS",
                message=f"Todo with title '{data.title}' already exists.",
            )

        new_todo = Todo(**data.model_dump())
        created_todo = self.todo_repository.create(new_todo)
        return TodoOut.model_validate(created_todo)

    def get_todo(self, todo_id: int) -> TodoOut:
        todo = self.todo_repository.get_by_id(todo_id)

        if todo is None:
            raise AppException(
                status_code=HTTPStatus.NOT_FOUND,
                code="TODO_NOT_FOUND",
                message=f"Todo with id '{todo_id}' not found.",
            )

        return TodoOut.model_validate(todo)

    def list_todos(self, filters: SearchTodo) -> list[Todo]:
        todos = self.todo_repository.search(**filters.model_dump())
        return [TodoOut.model_validate(todo).model_dump() for todo in todos]

    def delete_todo(self, id: int) -> None:
        todo = self.todo_repository.get_by_id(id)

        if todo is None:
            raise AppException(
                status_code=HTTPStatus.NOT_FOUND,
                code="TODO_NOT_FOUND",
                message=f"Todo with id '{id}' not found.",
            )

        self.todo_repository.delete(todo)

    def update_todo_put(self, todo_id, data: TodoCreate) -> TodoOut:
        todo = self.todo_repository.get_by_id(todo_id)

        if todo is None:
            raise AppException(
                status_code=HTTPStatus.NOT_FOUND,
                code="TODO_NOT_FOUND",
                message=f"Todo with id '{todo_id}' not found.",
            )

        if todo.title != data.title and self.is_exist_by_title(data.title):
            raise AppException(
                status_code=HTTPStatus.CONFLICT,
                code="TODO_ALREADY_EXISTS",
                message=f"Todo with title '{data.title}' already exists.",
            )

        updated_todo = self.todo_repository.update(todo, data.model_dump())
        return TodoOut.model_validate(updated_todo)

    def update_todo_patch(self, todo_id, data: TodoUpdate) -> TodoOut:
        todo = self.todo_repository.get_by_id(todo_id)

        if not todo:
            raise AppException(
                status_code=HTTPStatus.NOT_FOUND,
                code="TODO_NOT_FOUND",
                message=f"Todo with id '{todo_id}' not found.",
            )

        if (
                data.title
                and todo.title != data.title
                and self.is_exist_by_title(data.title)
        ):
            raise AppException(
                status_code=HTTPStatus.CONFLICT,
                code="TODO_ALREADY_EXISTS",
                message=f"Todo with title '{data.title}' already exists.",
            )

        updated_todo = self.todo_repository.update(
            todo, data.model_dump(exclude_unset=True)
        )
        return TodoOut.model_validate(updated_todo)

    def is_exist_by_title(self, title: str) -> bool:
        existed_todo = self.todo_repository.get_by_title(title)
        return existed_todo is not None

