from tkinter import Image

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.dbConfig import Base


class Category(Base):
    __tablename__ = 'category'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(100))
    category_image:Mapped[str] = mapped_column(String(200))

    products:Mapped[list["Product"]] = relationship("Product",back_populates="category",
                                                    lazy="selectin", cascade="all, delete-orphan")