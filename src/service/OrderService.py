from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model import Order, OrderItems
from src.repository.cart_items_repository import CartItemsRepository
from src.repository.cart_repository import CartRepository
from src.repository.order_items_repository import OrderItemsRepository
from src.repository.order_repository import OrderRepository
from src.repository.user_repository import UserRepository


class OrderService:
    def __init__(self,user_repo:UserRepository,
                 cart_repo:CartRepository,
                 cart_items_repo:CartItemsRepository,
                 order_repo:OrderRepository,
                 order_items_repo:OrderItemsRepository
                 ):
        self.user_repo = user_repo
        self.cart_repo = cart_repo
        self.cart_items_repo = cart_items_repo
        self.order_repo = order_repo
        self.order_items_repo = order_items_repo

    async def checkout(self, user_id:int):
        user = await self.user_repo.fetch_by_id(user_id)
        if not user:
            raise ResourceNotFoundException(f"Uer with id {user_id} was not found.")
        cart  = await self.cart_repo.fetch_cart_by_user_id(user_id)
        if not cart:
            raise ResourceNotFoundException(f"Cart with id {user_id} was not found.")
        if not cart.cart_items:
            return {
                "message":"Cart is empty"
            }
        order = Order(user_id=user_id, total_price=0)
        order = await self.order_repo.create_order(order)
        total_price = 0

        for cart_item in cart.cart_items:
            product = cart_item.product
            order_item = OrderItems(order_id=order.id,product_id=product.id,price=product.price)
            await self.order_items_repo.create_order_items(order_item)
            total_price+=product.price
        order.total_price = total_price

        for cart_item in cart.cart_items:
            await self.cart_items_repo.delete_cart_items(
                cart_item
            )
        return {
            "message" : "Order Placed successfully",
            "order_id": order.id,
            "total_price": order.total_price
        }
