# planificador/balanceador.py

from collections import Counter

class Balanceador:
    def __init__(self, db):
        self.db = db

    def balancear(self, turnos):
        # Este método puede analizar la distribución de turnos por empleado y tipo
        # para detectar desequilibrios. De momento solo mostramos un conteo simple.

        contador = Counter()
        for turno in turnos:
            key = (turno.empleado_id, turno.turno)
            contador[key] += 1

        # Esto es solo informativo por ahora. En el futuro se puede usar para ajustar.
        for (empleado_id, tipo_turno), cantidad in contador.items():
            print(f"Empleado {empleado_id} tiene {cantidad} turnos de {tipo_turno}")
