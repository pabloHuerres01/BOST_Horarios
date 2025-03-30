from app.database.database import SessionLocal
from app.modelos.Ausencias import Ausencia
from app.modelos.Empleados import Empleado
from app.modelos.Dia import Dia
from app.modelos.Mes import Mes

def consultar_ausencias():
    db = SessionLocal()

    print("Listado de empleados:")
    empleados = db.query(Empleado).all()
    for e in empleados:
        print(f"{e.id}: {e.nombre} {e.apellidos}")

    empleado_id = int(input("\nID del empleado a consultar: "))
    anio = int(input("Año: "))
    mes = int(input("Mes (1-12): "))

    ausencias = (
        db.query(Ausencia)
        .join(Dia)
        .join(Mes)
        .filter(
            Ausencia.empleado_id == empleado_id,
            Mes.anio == anio,
            Mes.mes == mes
        )
        .all()
    )

    if not ausencias:
        print("No hay ausencias registradas para ese empleado en ese mes.")
    else:
        print(f"\nAusencias de {empleado_id} en {anio}-{mes:02}:")
        for a in ausencias:
            print(f"Día ID {a.dia_id} - Tipo: {a.tipo}")

    db.close()

if __name__ == "__main__":
    consultar_ausencias()
