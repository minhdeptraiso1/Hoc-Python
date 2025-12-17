from typing import Optional

from pydantic import BaseModel, Field


class SearchTodo(BaseModel):
    done: Optional[bool] = Field(None, description="Status todo: true/false")
    keyword: Optional[str] = Field(None, description="Keyword to search")
    limit: Optional[int] = Field(10, ge=1, description="Limit of results")

    class Config:
        json_schema_extra = {
            "example": {
                "done": True,
                "keyword": "go to",
                "limit": 10
            }
        }
