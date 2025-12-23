from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Todo
from repository import BaseRepository


class TodoRepository(BaseRepository[Todo]):
    def __init__(self, db: Session):
        super().__init__(Todo, db)

    def get_by_title(self, title: str) -> Todo | None:
        return self.db.query(self.model).filter(self.model.title.ilike(title)).first()

    def search(
        self, done: bool | None, keyword: str | None, offset: int = 0, limit: int = 100
    ) -> list[Todo]:
        stmt = select(Todo)

        if keyword:
            stmt = stmt.where(self.model.title.ilike(f"%{keyword}%"))

        if done is not None:
            stmt = stmt.where(self.model.done.is_(done))

        stmt = stmt.offset(offset).limit(limit)

        return list(self.db.execute(stmt).scalars().all())