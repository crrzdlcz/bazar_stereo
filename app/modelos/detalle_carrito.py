from base import Base
from sqlalchemy import BigInteger, Integer, Numeric, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column


class Detalle_Carrito(Base):
    __tablename__ = "detalle_carrito"
    __table_args__ = {"schema": "BazarStereo"}
    id_carrito: Mapped[int] = mapped_column(Integer)
    id_disco: Mapped[int] = mapped_column(Integer)
    cantidad: Mapped[int] = mapped_column(SmallInteger)
    total_producto: Mapped[float] = mapped_column(Numeric)
    precio_unitario: Mapped[float] = mapped_column(Numeric)
    id_detalle_carrito: Mapped[int] = mapped_column(BigInteger, primary_key=True)
