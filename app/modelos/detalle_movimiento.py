from base import Base
from sqlalchemy import BigInteger, Numeric, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column


class Detalle_Movimiento(Base):
    __tablename__ = "detalle_movimiento"
    __table_args__ = {"schema": "BazarStereo"}
    id_movimiento: Mapped[int] = mapped_column(BigInteger)
    id_disco: Mapped[int] = mapped_column(SmallInteger)
    cantidad: Mapped[int] = mapped_column(SmallInteger)
    precio_unario: Mapped[float] = mapped_column(Numeric)
    total_producto: Mapped[float] = mapped_column(Numeric)
    id_detalle_movimiento: Mapped[int] = mapped_column(BigInteger, primary_key=True)
