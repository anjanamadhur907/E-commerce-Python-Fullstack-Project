from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError
from starlette.staticfiles import StaticFiles

from src.routes.user_router import router as user_router
from src.routes.category_router import router as category_router

from src.exception.global_exception_handler import resource_not_found_exception_handler, sqlalchemy_error_handler, \
    unknown_exception_handler
from src.exception.resource_not_found_exception import ResourceNotFoundException

app = FastAPI()

app.add_exception_handler(ResourceNotFoundException, resource_not_found_exception_handler)
app.add_exception_handler(SQLAlchemyError, sqlalchemy_error_handler)
app.add_exception_handler(Exception, unknown_exception_handler)

app.mount("/public",StaticFiles(directory="src/public"),name="public")

app.include_router(user_router)
app.include_router(category_router)