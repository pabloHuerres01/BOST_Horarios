from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database.database import Base

empleado_puestos = Table(
    "empleado_puestos",
    Base.metadata,
    Column("empleado_id", Integer, ForeignKey("empleados.id", ondelete="CASCADE")),
    Column("puesto_id", Integer, ForeignKey("puestos.id", ondelete="CASCADE"))
)
