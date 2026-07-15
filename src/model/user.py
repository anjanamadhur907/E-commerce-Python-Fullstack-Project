from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.dbConfig import Base


class User(Base):
    __tablename__ = 'user'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(100))
    email:Mapped[str] = mapped_column(String(100), unique=True)
    password:Mapped[str] = mapped_column(String(100))

    cart:Mapped["Cart"] = relationship("Cart",cascade="all,delete-orphan",
                                       back_populates="user", uselist=False)

    orders:Mapped[list["Order"]] = relationship("Order", cascade="all,delete-orphan", back_populates="user")