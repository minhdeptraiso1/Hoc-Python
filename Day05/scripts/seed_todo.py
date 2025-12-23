from configs.database import SessionLocal
from models import Todo


def seed_todos():
    db = SessionLocal()
    try:
        # Only seed when no todos exist to avoid duplicates
        if db.query(Todo).count() == 0:
            todos = [
                Todo(
                    title="Complete Python basics",
                    description="Finish the official Python tutorial and practice exercises (variables, control flow, functions).",
                    priority=1,
                    done=False,
                ),
                Todo(
                    title="Read about SQLAlchemy ORM",
                    description="Study SQLAlchemy ORM mappings, sessions, and relationships; convert a small app to use models.",
                    priority=2,
                    done=False,
                ),
                Todo(
                    title="Build a REST API with FastAPI",
                    description="Create endpoints for CRUD on todos, add validation with Pydantic, and document with OpenAPI.",
                    priority=3,
                    done=False,
                ),
                Todo(
                    title="Write unit tests for services",
                    description="Add pytest tests for service layer and repository functions (happy path and error cases).",
                    priority=4,
                    done=False,
                ),
                Todo(
                    title="Implement database migrations",
                    description="Learn Alembic basics and add a migration for the todos table if needed.",
                    priority=5,
                    done=False,
                ),
                Todo(
                    title="Refactor codebase for readability",
                    description="Apply small refactors, add type hints and docstrings, and improve logging.",
                    priority=2,
                    done=False,
                ),
                Todo(
                    title="Prepare a small portfolio project",
                    description="Combine learned concepts into a small project to showcase: API, DB, tests, and README.",
                    priority=2,
                    done=False,
                ),
                Todo(
                    title="Practice algorithms for interviews",
                    description="Solve 30 algorithmic problems (arrays, strings, dynamic programming) on a coding site.",
                    priority=3,
                    done=False,
                ),
            ]

            db.bulk_save_objects(todos)
            db.commit()
            print(f"Seeded {len(todos)} todos.")
        else:
            print("Todos already present; skipping seeding.")
    finally:
        db.close()


if __name__ == "__main__":
    seed_todos()