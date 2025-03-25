from sqlalchemy import Column, Integer, String
from app.database.database import Base

# ... Puesto ya definido arriba

class Empleado(Base):
    __tablename__ = "empleados"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellidos = Column(String(150), nullable=False)
    vacaciones_disponibles = Column(Integer, default=0)

    def __repr__(self):
        return f"<Empleado(nombre='{self.nombre}', apellidos='{self.apellidos}')>"
