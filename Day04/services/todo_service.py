from models.todo_model import Task
from schemas.todo_schema.todo_create import TodoCreate
from schemas.todo_schema.todo_out import TodoOut
from schemas.todo_schema.todo_search import SearchTodo
from schemas.todo_schema.todo_update import TodoUpdate
from ultils.todo_ultils import exists_title, id_is_exists, check_priority_in_1_to_5

_todos: list[Task] = []
_id_counter = 1


def create_todo(todo: TodoCreate) -> TodoOut:
    global _id_counter
    exists_title(todo.title, _todos)
    check_priority_in_1_to_5(todo.priority)
    # stored_todo = {
    #     "id": _id_counter,
    #     "title": todo.title,
    #     "description": todo.description,
    #     "priority": todo.priority,
    #     "done": todo.done,
    # }
    stored_todo = Task(
        id=_id_counter,
        title=todo.title,
        description=todo.description,
        priority=todo.priority,
        done=todo.done
    )
    _todos.append(stored_todo)
    _id_counter += 1
    return TodoOut(**stored_todo.model_dump())


def update_todo_patch(id: int, todo: TodoUpdate) -> TodoOut:
    item = id_is_exists(id, _todos)

    if todo.title is not None:
        exists_title(todo.title, _todos, exclude_id=id)
        item.title = todo.title

    if todo.description is not None:
        item.description = todo.description

    if todo.priority is not None:
        check_priority_in_1_to_5(todo.priority)
        item.priority = todo.priority

    if todo.done is not None:
        item.done = todo.done

    return TodoOut.model_validate(item)


def update_todo_put(id: int, todo: TodoCreate) -> TodoOut:
    item = id_is_exists(id, _todos)

    item.title = todo.title
    item.description = todo.description
    item.priority = todo.priority
    item.done = todo.done

    exists_title(item.title, _todos, exclude_id=id)
    check_priority_in_1_to_5(item.priority)

    return TodoOut.model_validate(item)


def delete_todo(id: int) -> None:
    _todos.remove(id_is_exists(id, _todos))


def get_todo_by_id(id: int) -> TodoOut:
    return TodoOut.model_validate(id_is_exists(id, _todos))


def get_all_by_keyword(search: SearchTodo) -> list[TodoOut]:
    results = _todos.copy()

    if search.done is not None:
        results = [t for t in results if t.done == search.done]

    if search.keyword:
        keyword_lower = search.keyword.lower()
        results = [t for t in results if keyword_lower in t.title.lower()]

    return [TodoOut.model_validate(t) for t in results[:search.limit]]
