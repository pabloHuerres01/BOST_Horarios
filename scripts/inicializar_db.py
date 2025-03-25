# scripts/inicializar_db.py

from app.database.database import Base, engine
from app.modelos.Puestos import Puesto
from app.modelos.Empleados import Empleado
from app.modelos.Mes import Mes
from app.modelos.Dia import Dia
from app.modelos.Turno import Turno
from app.database.database import SessionLocal

def init_db():
    print("Creando tablas si no existen...")
    Base.metadata.create_all(bind=engine)

    # Insertar puestos iniciales
    db = SessionLocal()
    if db.query(Puesto).count() == 0:
        print("Insertando puestos iniciales...")
        db.add_all([
            Puesto(nombre="L1"),
            Puesto(nombre="L2"),
            Puesto(nombre="L3"),
            Puesto(nombre="PROVISION")
        ])
        db.commit()
    else:
        print("Puestos ya existentes. No se insertan.")
    db.close()

if __name__ == "__main__":
    init_db()
