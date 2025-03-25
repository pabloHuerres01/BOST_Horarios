from app.database.database import SessionLocal
from app.modelos.Empleados import Empleado
from app.modelos.Dia import Dia
from app.modelos.Turno import Turno
from app.modelos.Puestos import Puesto
from app.modelos.Mes import Mes

from planificador.restricciones import Restricciones
from planificador.asignador_empleados import AsignadorEmpleados
from planificador.balanceador import Balanceador
from planificador.compensador import CompensadorHoras


class TurnoManager:
    def __init__(self):
        self.db = SessionLocal()
        self.restricciones = Restricciones(self.db)
        self.asignador = AsignadorEmpleados(self.db)
        self.balanceador = Balanceador(self.db)
        self.compensador = CompensadorHoras(self.db)

    def planificar_mes(self, anio: int, mes: int):
        print(f"Generando turnos para {anio}-{mes:02}")
        
        dias_mes = self._obtener_dias_del_mes(anio, mes)
        empleados = self._obtener_empleados()

        for dia in dias_mes:
            for turno_tipo in ["mañana", "tarde"]:
                empleados_turno = self.asignador.asignar_empleados(dia, turno_tipo, empleados)

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

    def _obtener_dias_del_mes(self, anio, mes):
        return self.db.query(Dia).join(Mes).filter(Mes.anio == anio, Mes.mes == mes).all()

    def _obtener_empleados(self):
        return self.db.query(Empleado).all()
