from typing import Optional

from pydantic import BaseModel, Field


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
