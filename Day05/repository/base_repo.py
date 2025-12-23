from typing import TypeVar, Generic, Type, Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from configs import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db

    def get_by_id(self, entity_id: Any) -> ModelType | None:
        stmt = select(self.model).where(self.model.id == entity_id)  # type: ignore[attr-defined]
        return self.db.execute(stmt).scalars().first()

    def get_all(self, *, offset: int = 0, limit: int = 100) -> list[ModelType]:
        stmt = select(self.model).offset(offset).limit(limit)
        return list(self.db.execute(stmt).scalars().all())

    def create(self, obj: ModelType) -> ModelType:
        self.db.add(obj)
        self.db.flush()
        self.db.refresh(obj)
        return obj

    def update(self, obj: ModelType, data: dict[str, Any]) -> ModelType:
        for key, value in data.items():
            setattr(obj, key, value)

        self.db.flush()
        self.db.refresh(obj)
        return obj

    def delete(self, obj: ModelType) -> None:
        self.db.delete(obj)
        self.db.flush()