from sqlalchemy import ForeignKey, Numeric, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.dbConfig import Base


class OrderItems(Base):
    __tablename__ = "order_items"
    id:Mapped[int] = mapped_column(primary_key=True)
    order_id:Mapped[int] = mapped_column(ForeignKey("order.id"))
    product_id:Mapped[int] = mapped_column(ForeignKey("product.id"))
    price:Mapped[float] = mapped_column(Numeric(10,2))
    quantity:Mapped[int] = mapped_column(Integer, default=1)

    order:Mapped["Order"] = relationship("Order", back_populates="order_items")
    product:Mapped["Product"] = relationship("Product", back_populates="order_items")