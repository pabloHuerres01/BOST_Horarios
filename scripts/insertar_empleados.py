from app.database.database import SessionLocal
from app.modelos.Empleados import Empleado

def insertar_empleado():
    nombre = input("Nombre: ").strip()
    apellidos = input("Apellidos: ").strip()
    vacaciones = input("Vacaciones disponibles (número): ").strip()

    if not vacaciones.isdigit():
        print("Vacaciones debe ser un número.")
        return

    db = SessionLocal()
    nuevo = Empleado(
        nombre=nombre,
        apellidos=apellidos,
        vacaciones_disponibles=int(vacaciones)
    )
    db.add(nuevo)
    db.commit()
    db.close()
    print("Empleado insertado correctamente.")

if __name__ == "__main__":
    insertar_empleado()
