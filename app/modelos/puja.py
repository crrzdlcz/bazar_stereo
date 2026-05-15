from datetime import datetime

from base import Base
from sqlalchemy import DateTime, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column


class Puja(Base):
    __tablename__ = "puja"
    __table_args__ = {"schema": "BazarStereo"}
    id_puja: Mapped[int] = mapped_column("id_puja", SmallInteger, primary_key=True)
    porcentaje: Mapped[int] = mapped_column(SmallInteger)
    fecha: Mapped[datetime] = mapped_column(DateTime)
    id_subasta: Mapped[int] = mapped_column(SmallInteger)
    id_usuario: Mapped[int] = mapped_column(Integer)
