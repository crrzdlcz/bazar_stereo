from sqlalchemy import Boolean, Integer, Numeric, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from app.base import Base


class Disco(Base):
    __tablename__ = "disco"
    __table_args__ = {"schema": "BazarStereo"}
    id_disco: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    estado: Mapped[int] = mapped_column(SmallInteger)
    titulo: Mapped[str] = mapped_column(String(50))
    formato: Mapped[bool] = mapped_column(Boolean)
    descripcion: Mapped[str] = mapped_column(String(200))
    precio: Mapped[float] = mapped_column(Numeric)
    artista: Mapped[str] = mapped_column(String(50))
    genero: Mapped[int] = mapped_column(SmallInteger)
    imagen: Mapped[str] = mapped_column(String(200))
    id_usuario: Mapped[int] = mapped_column(Integer)

    @property
    def formato_nombre(self):
        formatos = {0: "CD", 1: "Vinilo"}
        return formatos.get(self.formato, "Desconocido")

    @property
    def nombre_genero(self) -> str:
        generos = {0: "Rock", 1: "Pop", 2: "Pop Latino", 3: "Pop Coreano", 4: "Metal"}
        return generos.get(self.genero, "Otro")
