from datetime import datetime
from sqlalchemy import ForeignKey, Numeric, String, DateTime
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.db.dbConfig import Base


class Order(Base):
    __tablename__ = 'order'
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('user.id'))
    total_price:Mapped[float] = mapped_column(Numeric(10,2), default=0)
    receiver_name:Mapped[str] = mapped_column(String(100))
    receiver_mobile:Mapped[str] = mapped_column(String(10))
    delivery_address:Mapped[str] = mapped_column(String(500))
    order_date:Mapped[datetime] = mapped_column(DateTime, default=datetime.now, nullable=True)

    user:Mapped["User"] = relationship("User", back_populates="orders")

    order_items:Mapped[list["OrderItems"]] = relationship("OrderItems", back_populates="order", cascade="all, delete-orphan")
