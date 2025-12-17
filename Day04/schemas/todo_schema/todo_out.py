from typing import Optional

from pydantic import Field, BaseModel


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
