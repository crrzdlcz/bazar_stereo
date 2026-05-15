from datetime import datetime

from base import Base
from sqlalchemy import DateTime, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column


class Usuario(Base):
    __tablename__ = "Usuario"
    __table_args__ = {"schema": "BazarStereo"}
    id_usuario: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    correo: Mapped[str] = mapped_column(String(100))
    contraseña: Mapped[str] = mapped_column(String(64))
    tipo_usuario: Mapped[int] = mapped_column(SmallInteger)
    direccion: Mapped[str] = mapped_column(String(255))
    fecha_registro: Mapped[datetime] = mapped_column(DateTime)
