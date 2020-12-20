from views.ParkingView import *
from repository.ParkingRepository import ParkingRepository


class ParkingService:
    def __init__(self, parking_repositorio):
        self.__repositorio = [parking_repositorio]

    @property
    def repositorio(self):
        return self.__repositorio

    @repositorio.setter
    def repositorio(self, value):
        self.__repositorio = value

    # Devuelve True si hay plazas disponibles para el tipo de vehículo especificado, False en caso contrario
    def limite_plazas(self, tipo_vehiculo):
        control = True
        while control:
            if tipo_vehiculo == "Turismo":
                if self.repositorio[0].parking.limite_turismos >= len(self.repositorio[0].parking.plazas_turismos):
                    return True
                else:
                    return False
            elif tipo_vehiculo == "Motocicletas":
                if self.repositorio[0].parking.limite_motocicletas >= len(self.repositorio[0].parking.plazas_motocicletas):
                    return True
                else:
                    return False
            elif tipo_vehiculo == "PMR":
                if self.repositorio[0].parking.limite_pmr >= len(self.repositorio[0].parking.plazas_pmr):
                    return True
                else:
                    return False

    # Muestra por consola la ocupación de plazas, así como el límite de plazas
    def informar_plazas_libres(self):
        print(self.__repositorio[0].parking)


    def generar_ticket(self):
        pass


    def ocupar_plaza(self):
        pass


    def liberar_plaza(self):
        pass


    # Guarda en el repositorio el ingreso por tickets. ¿?
    def anotar_cobro(self):
        pass


    def elegir_vehiculo(self):
        control = True
        select = ""
        vehiculo = {
            1: "Turismo",
            2: "Motocicleta",
            3: "VPMR"
        }
        while control:
            try:
                vista.elegir_vehiculo_print()
                option = int(input())
                if option not in range(0, 3):
                    print("Por favor, introduzca uno de los valores indicados")
                elif option == 0:
                    control = False
                else:
                    select = vehiculo.get(option)
                    return select
            except ValueError:
                print("Valor introducido erróneo, por favor, introduzca un valor de los indicados.")

if __name__ == "__main__":
    repositorio_parking = ParkingRepository()
    servicio = ParkingService(repositorio_parking)
    servicio.informar_plazas_libres()
    print(servicio.limite_plazas("Turismo"))