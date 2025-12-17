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
