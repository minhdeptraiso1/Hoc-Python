from typing import List, Optional

from fastapi import HTTPException

from models.todo_model import Task


def exists_title(title: str, _todos: List[Task], exclude_id: Optional[int] = None) -> None:
    """
    Kiểm tra title đã tồn tại trong _todos hay chưa.

    Args:
        title (str): title cần check
        _todos (List[dict]): danh sách todo hiện tại
        exclude_id (Optional[int]): nếu truyền, bỏ qua item có id này (dùng khi update)

    Raises:
        HTTPException: status 409 nếu title đã tồn tại
    """
    for t in _todos:
        if t.title == title:
            if exclude_id is None or t.id != exclude_id:
                raise HTTPException(status_code=409, detail="Title already exists")


def id_is_exists(id: int, _todos: list[Task]) -> Task:
    """
    Kiểm tra id có tồn tại trong _todos hay chưa và lấy ra todo.

    Args:
        id (int): id cần check
        _todos (list[dict]): danh sách todo hiện tại
    Raises:
        HTTPException: status 400 nếu ko tìm thấy id
    """
    for t in _todos:
        if t.id == id:
            return t
    raise HTTPException(status_code=404, detail="Id does not found")
