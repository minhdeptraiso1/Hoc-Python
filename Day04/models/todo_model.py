from typing import Optional

from pydantic import BaseModel, Field


class Task(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=3, max_length=200, description="Task title")
    description: str = Field("", max_length=1000, description="Task description")
    priority: int = Field(1, ge=1, le=5, description="Priority from 1-5")
    done: bool = Field(False, description="Done : true/false")

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Buy groceries",
                "description": "Milk, eggs, bread",
                "priority": 2,
                "done": False
            }
        }
