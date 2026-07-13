from fastapi import APIRouter
from fastapi.params import Depends

from src.dependency.service_dependency import get_cart_service
from src.model import Cart
from src.schema.cart_schema import CartRequest
from src.service.cart_service import CartService

router = APIRouter(prefix="/cart", tags=["cart"])

@router.post("/", status_code=201)
async def add_to_cart(request:CartRequest, cart_service:CartService=Depends(get_cart_service)):
    return await cart_service.add_to_cart(request)

