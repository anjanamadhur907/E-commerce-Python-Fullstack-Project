from fastapi import APIRouter, Depends

from src.dependency.service_dependency import get_user_service
from src.schema.user_schema import UserRequest
from src.service.user_service import UserService

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/", status_code=201)
async def create_user(request:UserRequest, user_service: UserService = Depends(get_user_service)):
    return await user_service.create_user(request)