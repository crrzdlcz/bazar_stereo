from datetime import datetime

from base import Base
from sqlalchemy import DateTime, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column


class Carrito(Base):
    __tablename__ = "carrito"
    __table_args__ = {"schema": "BazarStereo"}
    id_carrito: Mapped[int] = mapped_column(Integer, primary_key=True)
    total: Mapped[float] = mapped_column(Numeric)
    fecha_creacion: Mapped[datetime] = mapped_column(DateTime)
    fecha_actualizacion: Mapped[datetime] = mapped_column(DateTime)
    id_usuario: Mapped[int] = mapped_column(Integer)
