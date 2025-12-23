from fastapi import APIRouter

from controller.todo_controler import todo_router

router = APIRouter(prefix="/api/v1")
router.include_router(todo_router)