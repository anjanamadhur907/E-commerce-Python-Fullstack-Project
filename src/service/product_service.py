from fastapi import UploadFile
from pathlib import Path

from src.model import Product
from src.repository.product_repository import ProductRepository
import shutil
BASE_DIR = Path(__file__).resolve().parent.parent
class ProductService:
    def __init__(self, product_repo:ProductRepository):
        self.product_repo = product_repo

    async def create_product(self, title:str,price:float,description:str,rating:str,product_image:UploadFile,category_id:int):
        filepath = BASE_DIR.joinpath("public","images",product_image.filename)
        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(product_image.file, buffer)
        await product_image.close()
        product = Product(title=title,price=price,description=description,rating=rating,product_image="/public/images/"+product_image.filename,category_id=category_id)
        return await self.product_repo.create_product(product)

    async def fetch_all(self):
        return await self.product_repo.fetch_all()