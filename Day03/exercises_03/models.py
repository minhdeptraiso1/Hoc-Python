from datetime import datetime

class Task:
    def __init__(self, description: str, due_date: datetime, status: str = "todo"):
        self.description = description
        self.due_date = due_date
        self.status = status

    def is_overdue(self, now: datetime) -> bool:
        return self.due_date.date() < now.date() and self.status == "todo"

    def mark_as_done(self):
        self.status = "done"

    def __str__(self) -> str:
        status_text = "DONE" if self.status == "done" else "TODO"
        date_str = self.due_date.strftime("%Y-%m-%d")
        return f"[{status_text}] {self.description} (Hạn: {date_str})"