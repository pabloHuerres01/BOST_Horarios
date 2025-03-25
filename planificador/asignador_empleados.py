# planificador/asignador_empleados.py
from random import sample
from app.modelos.Puestos import Puesto

class AsignadorEmpleados:
    def __init__(self, db):
        self.db = db
        self.puestos = {p.nombre: p for p in self.db.query(Puesto).all()}

    def asignar_empleados(self, dia, turno_tipo, empleados):
        asignaciones = []
        # ejemplo simple: seleccionar 1 L2 + 2 L1 para cada turno
        l2 = [e for e in empleados if self._tiene_puesto(e, "L2")]
        l1 = [e for e in empleados if self._tiene_puesto(e, "L1")]

        if l2:
            asignaciones.append((sample(l2, 1)[0], self.puestos["L2"]))
        if len(l1) >= 2:
            asignaciones += [(e, self.puestos["L1"]) for e in sample(l1, 2)]

        return asignaciones

    def _tiene_puesto(self, empleado, puesto_nombre):
        # Aquí deberías comprobar si el empleado puede trabajar en ese puesto
        return True
