# script/planificar.py

from planificador.turno_manager import TurnoManager

def main():
    anio = int(input("Año: "))
    mes = int(input("Mes (1-12): "))
    manager = TurnoManager()
    manager.planificar_mes(anio, mes)

if __name__ == "__main__":
    main()
