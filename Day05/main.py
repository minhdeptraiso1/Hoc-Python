from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from configs.app_logging import setup_logging
from configs.env import settings_config
from exception.app_exception import AppException
from exception.handler_exception import app_exception_handler, validation_exception_handler
from middleware.db_middle import DBSessionMiddleware
from middleware.trace_middle import TraceIdMiddleware
from router.todo_router import router

settings = settings_config()
setup_logging(sql_echo=settings.environment.lower() == "dev")

app = FastAPI()
app.include_router(router)

__MIDDLEWARES__ = [DBSessionMiddleware, TraceIdMiddleware]
for middleware in __MIDDLEWARES__:
    app.add_middleware(middleware)

__EXCEPTION_HANDLERS__ = [
    (AppException, app_exception_handler),
    (RequestValidationError, validation_exception_handler),
]

for exc, handler in __EXCEPTION_HANDLERS__:
    app.add_exception_handler(exc, handler)