from app.database.database import SessionLocal
from app.modelos.Empleados import Empleado
from app.modelos.Dia import Dia
from app.modelos.Turno import Turno
from app.modelos.Puestos import Puesto
from app.modelos.Mes import Mes
from app.modelos.Ausencias import Ausencia

from planificador.restricciones import Restricciones
from planificador.asignador_empleados import AsignadorEmpleados
from planificador.balanceador import Balanceador
from planificador.compensador import CompensadorHoras

import calendar


class TurnoManager:
    def __init__(self):
        self.db = SessionLocal()
        self.restricciones = Restricciones(self.db)
        self.asignador = AsignadorEmpleados(self.db)
        self.balanceador = Balanceador(self.db)
        self.compensador = CompensadorHoras(self.db)

    def planificar_mes(self, anio: int, mes: int):
        print(f"Generando turnos para {anio}-{mes:02}")
        self._generar_mes_y_dias_si_no_existen(anio, mes)

        dias_mes = self._obtener_dias_del_mes(anio, mes)

        for dia in dias_mes:
            empleados_disponibles = self._obtener_empleados_disponibles_en_dia(dia.id)

            for turno_tipo in ["mañana", "tarde"]:
                empleados_turno = self.asignador.asignar_empleados(dia, turno_tipo, empleados_disponibles)

                for empleado, puesto in empleados_turno:
                    if self.restricciones.es_valido(empleado, dia, turno_tipo):
                        nuevo_turno = Turno(
                            dia_id=dia.id,
                            empleado_id=empleado.id,
                            puesto_id=puesto.id,
                            turno=turno_tipo
                        )
                        self.db.add(nuevo_turno)

        self.db.commit()
        self.compensador.compensar_horas(anio, mes)
        print("Turnos generados correctamente.")

    def _generar_mes_y_dias_si_no_existen(self, anio, mes):
        mes_obj = self.db.query(Mes).filter_by(anio=anio, mes=mes).first()
        if not mes_obj:
            mes_obj = Mes(anio=anio, mes=mes)
            self.db.add(mes_obj)
            self.db.commit()
            self.db.refresh(mes_obj)

        dias_existentes = self.db.query(Dia).filter_by(mes_id=mes_obj.id).count()
        if dias_existentes == 0:
            total_dias = calendar.monthrange(anio, mes)[1]
            for dia in range(1, total_dias + 1):
                self.db.add(Dia(numero_dia=dia, mes_id=mes_obj.id))
            self.db.commit()
            print(f"Días generados para {anio}-{mes:02}")

    def _obtener_dias_del_mes(self, anio, mes):
        return self.db.query(Dia).join(Mes).filter(Mes.anio == anio, Mes.mes == mes).all()

    def _obtener_empleados_disponibles_en_dia(self, dia_id):
        subquery = self.db.query(Ausencia.empleado_id).filter_by(dia_id=dia_id).subquery()
        return self.db.query(Empleado).filter(~Empleado.id.in_(subquery)).all()
