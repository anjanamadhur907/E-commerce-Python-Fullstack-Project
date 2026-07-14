from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.model import Category


class CategoryRepository:
    def __init__(self, session:AsyncSession):
        self.session = session

    async def create_category(self, category:Category):
        self.session.add(category)
        await self.session.flush()
        await self.session.refresh(category)
        return category

    async def fetch_category_by_id(self, id:int):
        return await self.session.get(Category, id)

    async def delete_category(self, category:Category):
        await self.session.delete(category)
        await self.session.flush()

    async def fetch_all_category(self):
        stmt = select(Category).options(selectinload(Category.products))
        result = await self.session.execute(stmt)
        return result.scalars().all()