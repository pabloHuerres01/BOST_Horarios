from app.database import Base, engine, SessionLocal
from app.modelos.Puestos import Puesto

def init_db():
    # Crear tablas si no existen
    print("Verificando estructura de la base de datos...")
    Base.metadata.create_all(bind=engine)

    # Insertar puestos si no existen
    db = SessionLocal()
    try:
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
            print("Puestos ya existen. No se inserta nada.")
    finally:
        db.close()
