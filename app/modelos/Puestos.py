# app/MODELOS/models.py

from sqlalchemy import Column, Integer, String
from app.database import Base

class Puesto(Base):
    __tablename__ = "puestos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"<Puesto(nombre='{self.nombre}')>"
