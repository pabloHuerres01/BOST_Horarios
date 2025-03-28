from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class Ausencia(Base):
    __tablename__ = "ausencias"

    id = Column(Integer, primary_key=True)
    empleado_id = Column(Integer, ForeignKey("empleados.id", ondelete="CASCADE"))
    dia_id = Column(Integer, ForeignKey("dias.id", ondelete="CASCADE"))
    tipo = Column(String(50), nullable=False)  # "baja", "vacaciones", "descanso_manual"

    empleado = relationship("Empleado", backref="ausencias")
    dia = relationship("Dia", backref="ausencias")
