from pydantic import BaseModel, EmailStr


class UserRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class SignInRequest(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id:int
    name:str
    email:EmailStr
    token:str