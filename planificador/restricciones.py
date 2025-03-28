# planificador/restricciones.py
from datetime import timedelta
from app.modelos.Turno import Turno
from app.modelos.Ausencias import Ausencia

class Restricciones:
    def __init__(self, db):
        self.db = db

    def es_valido(self, empleado, dia, turno_tipo):
        # Regla: no puede haber turno mañana después de uno de tarde
        turno_anterior = self._turno_dia_anterior(empleado.id, dia.id)
        if turno_anterior == "tarde" and turno_tipo == "mañana":
            return False

        # Regla: no más de 7 días trabajados seguidos
        if self._dias_trabajados_consecutivos(empleado.id, dia.id) >= 7:
            return False

        # Regla: no trabajar si tiene ausencia
        if self.db.query(Ausencia).filter_by(empleado_id=empleado.id, dia_id=dia.id).first():
            return False

        # Regla: no trabajar si está de baja
        if empleado.de_baja:
            return False

        return True

    def _turno_dia_anterior(self, empleado_id, dia_id):
        dia_anterior = dia_id - 1
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
