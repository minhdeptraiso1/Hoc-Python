from typing import Optional

from pydantic import BaseModel


class ErrorSchema(BaseModel):
    code: str
    message: str
    detail: Optional[str] = None