from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database.database import Base  # Usamos la misma Base que en el resto del proyecto

class Turno(Base):
    __tablename__ = "turnos"

    id = Column(Integer, primary_key=True, index=True)
    dia_id = Column(Integer, ForeignKey("dias.id", ondelete="CASCADE"), nullable=False)
    empleado_id = Column(Integer, ForeignKey("empleados.id", ondelete="CASCADE"), nullable=False)
    puesto_id = Column(Integer, ForeignKey("puestos.id"), nullable=False)
    turno = Column(Enum("mañana", "tarde", name="turno_enum"), nullable=False)

    dia = relationship("Dia", backref="turnos")
    empleado = relationship("Empleado", backref="turnos")
    puesto = relationship("Puesto", backref="turnos")

    def __repr__(self):
        return f"<Turno(dia_id={self.dia_id}, empleado_id={self.empleado_id}, turno={self.turno})>"
