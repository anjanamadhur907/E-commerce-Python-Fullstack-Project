from pydantic import BaseModel


class OrderRequest(BaseModel):
    user_id: int
    receiver_name:str
    receiver_mobile:str
    delivery_address:str