from pydantic import BaseModel


class OrderRequest(BaseModel):
    user_id: int