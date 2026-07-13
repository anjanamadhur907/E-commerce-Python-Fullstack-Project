from urllib.request import Request

from sqlalchemy.exc import SQLAlchemyError
from starlette.responses import JSONResponse

from src.exception.resource_not_found_exception import ResourceNotFoundException


def sqlalchemy_error_handler(request:Request, exc:SQLAlchemyError):
    return JSONResponse(status_code=500,
                        content={
                            "error":"Database error",
                            "message":str(exc)
                        })

def resource_not_found_exception_handler(request:Request, exc:ResourceNotFoundException):
    return JSONResponse(status_code=404,
                        content={
                            "error":"Resource not found",
                            "message":exc.message
                        })

def unknown_exception_handler(request:Request, exc:Exception):
    return JSONResponse(status_code=500,
                        content={
                            "error":"Unknown error",
                            "message":str(exc)
                        })