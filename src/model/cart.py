from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.dbConfig import Base


class Cart(Base):
    __tablename__ = 'cart'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("user.id"), unique=True)

    user:Mapped["User"] = relationship("Cart", back_populates="user", lazy="selectin")

    cart_items:Mapped[list["CartItems"]] = relationship("CartItem", back_populates="cart",
                                                        cascade="all, delete-orphan")