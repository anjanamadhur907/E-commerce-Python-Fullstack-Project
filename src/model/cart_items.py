from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.dbConfig import Base


class CartItems(Base):
    __tablename__ = "cart_items"
    cart_id:Mapped[int] = mapped_column(ForeignKey("cart.id"),primary_key=True)
    product_id:Mapped[int] = mapped_column(ForeignKey("product.id"),primary_key=True)
    quantity:Mapped[int] = mapped_column(Integer, default=1)

    cart:Mapped["Cart"] = relationship("Cart", back_populates="cart_items")

    product:Mapped["Product"] = relationship("Product", back_populates="cart_items")
