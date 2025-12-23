from typing import Any

from starlette.responses import JSONResponse


def response_success(data: Any, status_code: int = 200) -> JSONResponse:
    return JSONResponse(
        status_code=status_code, content={"success": True, "data": data}
    )