from sqlalchemy.ext.asyncio import AsyncSession

from src.model import User


class UserRepository:
    def __init__(self, session:AsyncSession):
        self.session = session

    async def create_user(self, user:User):
        self.session.add(user)
        await self.session.flush()
        await self.session.refresh(user)
        return user