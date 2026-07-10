from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.dbConfig import Base


class CartItems(Base):
    __tablename__ = "cart_items"
    cart_id:Mapped[int] = mapped_column(ForeignKey("cart.id"),primary_key=True)
    product_id:Mapped[int] = mapped_column(ForeignKey("product.id"),primary_key=True)

    cart:Mapped["Cart"] = relationship("Cart", lazy="selectin")

    product:Mapped["Product"] = relationship("Product", lazy="selectin")
