from datetime import datetime

from base import Base
from sqlalchemy import BigInteger, DateTime, Integer, Numeric, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column


class Movimiento(Base):
    __tablename__ = "movimiento"
    __table_args__ = {"schema": "BazarStereo"}
    id_movimiento: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    tipo: Mapped[int] = mapped_column(SmallInteger)
    fecha: Mapped[datetime] = mapped_column(DateTime)
    total: Mapped[float] = mapped_column(Numeric)
    id_usuario: Mapped[int] = mapped_column(Integer)
