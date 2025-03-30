# scripts/registrar_ausencia.py

from app.database.database import SessionLocal
from app.modelos.Ausencias import Ausencia
from app.modelos.Empleados import Empleado
from app.modelos.Dia import Dia

def registrar_ausencia():
    db = SessionLocal()

    empleados = db.query(Empleado).all()
    print("\nEmpleados:")
    for emp in empleados:
        print(f"{emp.id}: {emp.nombre} {emp.apellidos}")

    empleado_id = int(input("\nID del empleado: "))
    dia_id = int(input("ID del día (consulta en tabla 'dias'): "))
    tipo = input("Tipo de ausencia (baja | vacaciones | descanso_manual): ").strip().lower()

    if tipo not in ["baja", "vacaciones", "descanso_manual"]:
        print("Tipo de ausencia inválido.")
        return

    ausencia = Ausencia(empleado_id=empleado_id, dia_id=dia_id, tipo=tipo)
    db.add(ausencia)
    db.commit()
    db.close()
    print("Ausencia registrada correctamente.")

if __name__ == "__main__":
    registrar_ausencia()
