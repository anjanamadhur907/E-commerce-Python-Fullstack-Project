from fastapi import APIRouter, Form, UploadFile, File, Depends

from src.dependency.service_dependency import get_category_service
from src.service.category_service import CategoryService

router = APIRouter(prefix="/category", tags=["Category"])

@router.post("/", status_code=201)
async def create_category(category_name:str=Form(...),
                          category_image:UploadFile=File(...),
                          category_service:CategoryService=Depends(get_category_service)):
    return await category_service.create_category(category_name, category_image)
