from sqlalchemy import UniqueConstraint, Column, Integer
from sqlalchemy import Column, Integer, String
from app.database.database import Base
# ... Puesto y Empleado ya definidos arriba

class Mes(Base):
    __tablename__ = "meses"

    id = Column(Integer, primary_key=True, index=True)
    anio = Column(Integer, nullable=False)
    mes = Column(Integer, nullable=False)  # 1 a 12

    __table_args__ = (
        UniqueConstraint("anio", "mes", name="unique_anio_mes"),
    )

    def __repr__(self):
        return f"<Mes({self.anio}-{self.mes:02})>"
