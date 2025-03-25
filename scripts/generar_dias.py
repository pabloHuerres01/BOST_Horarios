from app.database.database import SessionLocal
from app.modelos.Mes import Mes
from app.modelos.Dia import Dia
import calendar

def generar_dias(anio, mes):
    db = SessionLocal()

    mes_existente = db.query(Mes).filter_by(anio=anio, mes=mes).first()
    if not mes_existente:
        mes_existente = Mes(anio=anio, mes=mes)
        db.add(mes_existente)
        db.commit()
        db.refresh(mes_existente)

    dias_en_mes = calendar.monthrange(anio, mes)[1]

    dias_existentes = db.query(Dia).filter_by(mes_id=mes_existente.id).count()
    if dias_existentes == 0:
        for dia in range(1, dias_en_mes + 1):
            db.add(Dia(numero_dia=dia, mes_id=mes_existente.id))
        db.commit()
        print("Días generados correctamente.")
    else:
        print("Los días ya estaban generados.")

    db.close()

if __name__ == "__main__":
    anio = int(input("Año: "))
    mes = int(input("Mes: "))
    generar_dias(anio, mes)

