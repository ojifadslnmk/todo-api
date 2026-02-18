from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import Request, HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from app.db.base import Base
from app.db.session import engine
from app.api.routes import todos

app = FastAPI()
app.include_router(todos.router)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Todo API is running"}

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.detail
        },
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    formatted_errors = {}

    for error in exc.errors():
        field = error["loc"][-1]
        message = error["msg"]

        if field not in formatted_errors:
            formatted_errors[field] = []

        formatted_errors[field].append(message)

    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "error": "Validation failed",
            "errors": formatted_errors
        },
    )
