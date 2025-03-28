from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from app.database.database import Base
from app.modelos.Mes import Mes

class Dia(Base):
    __tablename__ = "dias"

    id = Column(Integer, primary_key=True, index=True)
    numero_dia = Column(Integer, nullable=False)  # 1 a 31
    mes_id = Column(Integer, ForeignKey("meses.id", ondelete="CASCADE"), nullable=False)

    mes = relationship("Mes", backref="dias")

    def __repr__(self):
        return f"<Día({self.numero_dia} del mes_id={self.mes_id})>"
