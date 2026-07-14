from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.model import Product


class ProductRepository:
    def __init__(self, session:AsyncSession):
        self.session = session

    async def create_product(self, product:Product):
        self.session.add(product)
        await self.session.flush()
        await self.session.refresh(product)
        return product

    async def fetch_all(self):
        stmt = select(Product).options(selectinload(Product.category))
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def fetch_by_id(self,id:int):
        return await self.session.get(Product, id)

    async def delete_product(self, product:Product):
        await self.session.delete(product)
        await self.session.flush()