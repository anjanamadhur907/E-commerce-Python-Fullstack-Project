from fastapi import APIRouter, Depends

from src.dependency.service_dependency import get_order_service, authentication
from src.schema.order_schema import OrderRequest
from src.service.OrderService import OrderService

router = APIRouter(prefix="/order", tags=["Order"])

@router.post("/", status_code=201)
async def checkout(request:OrderRequest,payload:dict=Depends(authentication), order_service: OrderService = Depends(get_order_service)):
    return await order_service.checkout(request)

