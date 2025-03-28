from sqlalchemy import Column, Integer, String
from app.database.database import Base
from app.modelos.EmpleadoPuestos import empleado_puestos
from app.modelos.Puestos import Puesto  

from sqlalchemy import Boolean
from sqlalchemy.orm import relationship


# ... Puesto ya definido arriba

class Empleado(Base):
    __tablename__ = "empleados"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellidos = Column(String(150), nullable=False)
    vacaciones_disponibles = Column(Integer, default=0)
    de_baja = Column(Boolean, default=False)

    puestos = relationship(
        "Puesto",
        secondary=empleado_puestos,
        backref="empleados"
    )

    def __repr__(self):
        return f"<Empleado(nombre='{self.nombre}', apellidos='{self.apellidos}')>"
