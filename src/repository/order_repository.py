from sqlalchemy.ext.asyncio import AsyncSession

from src.model import Order


class OrderRepository:
    def __init__(self, session:AsyncSession):
        self.session = session

    async def create_order(self, order:Order):
        self.session.add(order)
        await self.session.flush()
        await self.session.refresh(order)
        return order

    async def fetch_order_by_id(self, id:int):
        return await self.session.get(Order, id)