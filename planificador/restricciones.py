# planificador/restricciones.py
from app.modelos.Turno import Turno
from app.modelos.Ausencias import Ausencia

class Restricciones:
    def __init__(self, db):
        self.db = db

    def es_valido(self, empleado, dia, turno_tipo):
        # Regla 1: el empleado no debe estar de baja
        if empleado.de_baja:
            return False

        # Regla 2: no puede tener una ausencia registrada ese día
        if self._tiene_ausencia(empleado.id, dia.id):
            return False

        # Regla 3: no puede tener turno de mañana si el día anterior trabajó de tarde
        if self._turno_dia_anterior(empleado.id, dia.id) == "tarde" and turno_tipo == "mañana":
            return False

        # Regla 4: no puede trabajar más de 7 días consecutivos
        if self._dias_trabajados_consecutivos(empleado.id, dia.id) >= 7:
            return False

        return True

    def _tiene_ausencia(self, empleado_id, dia_id):
        return self.db.query(Ausencia).filter_by(empleado_id=empleado_id, dia_id=dia_id).first() is not None

    def _turno_dia_anterior(self, empleado_id, dia_id):
        dia_anterior = dia_id - 1
        if dia_anterior < 1:
            return None
        turno = self.db.query(Turno).filter_by(dia_id=dia_anterior, empleado_id=empleado_id).first()
        return turno.turno if turno else None

    def _dias_trabajados_consecutivos(self, empleado_id, dia_id):
        dias = 0
        for i in range(1, 8):
            d = dia_id - i
            if d < 1:
                break
            turno = self.db.query(Turno).filter_by(dia_id=d, empleado_id=empleado_id).first()
            if turno:
                dias += 1
            else:
                break
        return dias
