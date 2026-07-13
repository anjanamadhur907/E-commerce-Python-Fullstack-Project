from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model import CartItems,Cart
from src.repository.cart_repository import CartRepository
from src.repository.product_repository import ProductRepository
from src.repository.user_repository import UserRepository
from src.schema.cart_schema import CartRequest


class CartService:
    def __init__(self, user_repo:UserRepository, product_repo:ProductRepository, cart_repo:CartRepository, cart_items_repo:CartRepository):
        self.user_repo = user_repo
        self.product_repo = product_repo
        self.cart_repo = cart_repo
        self.cart_items_repo = cart_items_repo

    async def add_to_cart(self, request:CartRequest):
        user_id = request.user_id
        product_id = request.product_id
        user = await self.user_repo.fetch_by_id(user_id)
        if not user:
            raise ResourceNotFoundException(f"User with id {user_id} is not found")

        product = await self.product_repo.fetch_by_id(product_id)
        if not product:
            raise ResourceNotFoundException(f"Product with id {product_id} is not found")

        cart = await self.cart_repo.fetch_cart_by_user_id(user_id)
        if not cart:
            cart = Cart(user_id=user_id)
            cart = await self.cart_repo.create_cart(cart)
            await self.cart_items_repo.save_product_in_cart(CartItems(product_id=product_id, cart_id=cart.id))
            return {"message":"Item successfully added to cart"}
        else:
            cart_items = await self.cart_items_repo.fetch_cart_items_by_product_id(product_id=product_id, cart_id=cart.id)
            if cart_items:
                return {"message":"Item already added to cart"}
            cart_items = CartItems(cart_id=cart.id, product_id=product_id)
            await self.cart_items_repo.save_product_in_cart(cart_items)
            return {"message": "Item successfully added to cart"}