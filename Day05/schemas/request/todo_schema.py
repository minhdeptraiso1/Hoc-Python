
from typing import Optional
from pydantic import BaseModel, Field


class SearchTodo(BaseModel):
    done: Optional[bool] = Field(None, description="Status todo: true/false")
    keyword: Optional[str] = Field(None, description="Keyword to search")
    offset: int = Field(default=0, ge=0)
    limit: int = Field(default=100, ge=1)

    class Config:
        json_schema_extra = {
            "example": {
                "done": True,
                "keyword": "go to"
            }
        }

class TodoCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=200, description="title todo")
    description: Optional[str] = Field(None, max_length=1000, description="description todo")
    priority: int = Field(None, ge=1, le=5, description="lv todo 1 - 5")
    done: bool = Field(False, description="done : true/false")

    class Config:
        json_schema_extra = {
            "title": "go to techzen",
            "description": "go to techzen at 8:30 am",
            "priority": 3,
            "done": False,
        }

class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=200, description="title todo")
    description: Optional[str] = Field(None, max_length=1000, description="description todo")
    priority: Optional[int] = Field(None, ge=1, le=5, description="lv todo 1 - 5")
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