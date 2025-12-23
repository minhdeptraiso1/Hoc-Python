from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from exception.app_exception import AppException
from schemas.response.error_response import ErrorSchema


async def app_exception_handler(_, exc: AppException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorSchema(
            code=exc.code,
            message=exc.message,
            detail=exc.detail,
        ).model_dump(),
    )


async def validation_exception_handler(_, exc: RequestValidationError) -> JSONResponse:
    return JSONResponse(
        status_code=422,
        content=ErrorSchema(
            code="VALIDATION_ERROR",
            message="Invalid request parameters",
            detail=str(exc),
        ).model_dump(),
    )