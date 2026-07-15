from fastapi import APIRouter, Form, UploadFile, File, Depends

from src.dependency.service_dependency import get_category_service
from src.service.category_service import CategoryService

router = APIRouter(prefix="/category", tags=["Category"])

@router.post("/", status_code=201)
async def create_category(category_name:str=Form(...),
                          category_image:UploadFile=File(...),
                          category_service:CategoryService=Depends(get_category_service)):
    return await category_service.create_category(category_name, category_image)

@router.delete("/{id}", status_code=200)
async def delete_category(id:int, category_service:CategoryService=Depends(get_category_service)):
    return await category_service.delete_category(id)

@router.get("/", status_code=200)
async def fetch_all_category(category_service:CategoryService=Depends(get_category_service)):
    return await category_service.fetch_all_category()

@router.put("/{id}", status_code=200)
async def update_category(id:int,
                          category_name:str=Form(...),
                          category_image:UploadFile=File(...),
                          category_service:CategoryService=Depends(get_category_service)):
    return await category_service.update_category(id, category_name, category_image)