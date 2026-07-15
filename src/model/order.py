from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.db.dbConfig import Base


class Order(Base):
    __tablename__ = 'order'
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('user.id'))
    total_price:Mapped[float] = mapped_column(Numeric(10,2), default=0)

    user:Mapped["User"] = relationship("User", back_populates="orders")

    order_items:Mapped[list["OrderItems"]] = relationship("OrderItems", back_populates="order", cascade="all, delete-orphan")
