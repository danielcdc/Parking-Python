from datetime import *
import math


class ParkingService:
    def __init__(self, parking_repositorio, ticket_repositorio):
        self.__repositorio = [parking_repositorio, ticket_repositorio]
        self.__precios = [{"Turismo" : 0.12}, {"Motocicletas" : 0.08}, {"PMR" : 0.10}]

    @property
    def repositorio(self):
        return self.__repositorio

    @repositorio.setter
    def repositorio(self, value):
        self.__repositorio = value

    @property
    def precios(self):
        return self.__precios

    @precios.setter
    def precios(self, value):
        self.__precios == value

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

    # Comprueba si no se ha excedido el límite de plazas y si hay plazas libres, de haberlas,
    # asigna una plaza y devuelve el Ticket al usuario. En caso contrario, informa al usuario.
    def ocupar_plaza(self, tipo_vehiculo):
        if self.limite_plazas(tipo_vehiculo):
            if self.asignar_plaza_libre(tipo_vehiculo):
                self.repositorio[1].create_ticket(self.asignar_plaza_libre(tipo_vehiculo).idPlaza)
                self.generar_ticket(tipo_vehiculo)
        else:
            print("Lo sentimos, no hay plazas disponibles para su vehículo.")

    def liberar_plaza(self, pin):
        if self.repositorio[1].find_by_pin(pin):
            ticket_a_cobrar = self.repositorio[1].find_by_pin(pin)
            self.anotar_cobro(ticket_a_cobrar)

    def asignar_plaza_libre(self, tipo_vehiculo):
        if tipo_vehiculo == "Turismo":
            for x in self.repositorio[0].lista_turismos:
                if x.ocupada is False and x.abonado is None:
                    return x
                else:
                    return False

        if tipo_vehiculo == "Motocicletas":
            for x in self.repositorio[0].lista_motocicletas:
                if x.ocupada is False and x.abonado is None:
                    return x
                else:
                    return False

        if tipo_vehiculo == "PMR":
            for x in self.repositorio[0].lista_pmr:
                if x.ocupada is False and x.abonado is None:
                    return x
                else:
                    return False

    # Calcula la cuantía a cobrar al ticket y la contabiliza.
    def anotar_cobro(self, ticket_a_cobrar):
        tiempo_aparcado = datetime.today() - ticket_a_cobrar.fecha_deposito
        tiempo_aparcado_en_min = math.floor(tiempo_aparcado.days*(24*60) + tiempo_aparcado.seconds/60)
        precio = 0
        if ticket_a_cobrar.tipo_vehiculo == "Turismo":
            precio = tiempo_aparcado*self.precios.get("Turismo")


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

# Testing
if __name__ == "__main__":
#     repositorio_parking = ParkingRepository()
#     servicio = ParkingService(repositorio_parking)
#     servicio.informar_plazas_libres()
#     print(servicio.limite_plazas("Turismo"))