from sqlalchemy.ext.asyncio import AsyncSession

from src.model import OrderItems, CartItems


class OrderItemsRepository:
    def __init__(self, session:AsyncSession):
        self.session = session

    async def create_order_items(self, order_items:OrderItems):
        self.session.add(order_items)
        await self.session.flush()
        await self.session.refresh(order_items)
        return order_items

    async def delete_cart_items(self, cart_items:CartItems):
        await self.session.delete(cart_items)
        await self.session.flush()