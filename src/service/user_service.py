from fastapi import HTTPException

from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model import User
from src.repository.user_repository import UserRepository
from src.schema.user_schema import UserRequest, SignInRequest
from src.utils.password import hash_password, verify_password


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def create_user(self, request:UserRequest):
        user = User(
            name=request.name,
            email=request.email,
            password=hash_password(request.password)
        )
        return await self.user_repo.create_user(user)

    async def signin(self, request:SignInRequest):
        user = await self.user_repo.fetch_by_email(request.email)
        if not user:
            raise ResourceNotFoundException(f"User with email {request.email} not found")
        status = verify_password(request.password, user.password)
        if not status:
            raise HTTPException(status_code=401, detail="Incorrect password")
        return user