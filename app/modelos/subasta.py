from datetime import datetime

from base import Base
from sqlalchemy import DateTime, Numeric, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column


class Subasta(Base):
    __tablename__ = "Subasta"
    __table_args__ = {"schema": "BazarStereo"}
    id_subasta: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    precio: Mapped[float] = mapped_column(Numeric)
    precio_minimo: Mapped[float] = mapped_column(Numeric)
    fecha_inicio: Mapped[datetime] = mapped_column(DateTime)
    fecha_fin: Mapped[datetime] = mapped_column(DateTime)
    estado: Mapped[int] = mapped_column(SmallInteger)
    id_disco: Mapped[int] = mapped_column(SmallInteger)
