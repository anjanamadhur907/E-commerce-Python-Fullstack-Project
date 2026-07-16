from fastapi import APIRouter, Depends

from src.dependency.service_dependency import get_user_service
from src.schema.user_schema import UserRequest, SignInRequest, UserResponse
from src.service.user_service import UserService
from src.utils.jwt_util import generate_token

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/", status_code=201)
async def create_user(request:UserRequest, user_service: UserService = Depends(get_user_service)):
    return await user_service.create_user(request)

@router.post("/signin", status_code=200, response_model=UserResponse)
async def signin(request:SignInRequest, user_service: UserService = Depends(get_user_service)):
    db_user = await user_service.signin(request)
    return UserResponse(id=db_user.id,
                        name = db_user.name,
                        email = db_user.email,
                        token = generate_token({"id":db_user.id, "name":db_user.name, "email":db_user.email}))