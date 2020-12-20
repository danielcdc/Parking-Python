from views.AdminView import *
from datetime import *


class AdminService:
    def __init__(self, plaza_repository, ticket_repository, abono_repository):
        self.__repositorios = [plaza_repository, ticket_repository, abono_repository]

    @property
    def repositorios(self):
        return self.__repositorios

    @repositorios.setter
    def repositorios(self, value):
        self.__repositorios = value

    # Devuelve un diccionario con el estado de todas las plazas que existen en el parking
    def comprobar_parking(self):
        listado_plazas = self.repositorios[0].find_all()
        resultado = dict()
        position = 1
        for x in listado_plazas:
            if x.ocupada:
                if x.abonado is not None:
                    estado = "Ocupada por un Abonado"
                else:
                    estado = "Ocupada"
            elif x.abonado is not None:
                estado = "Reservada"
            else:
                estado = "Libre"
            resultado.update({str(position): estado})
            position += 1
        comprobar_parking_print(resultado)

    # Devuelve la facturación por tickets (NO Abonados) en un intervalo de tiempo.
    def facturacion(self, fecha1, fecha2):
        facturado = 0
        for x in self.repositorios[1].find_all():
            if x.facturado is not None:
                if fecha1 <= x.fecha_salida <= fecha2:
                    facturado += x.facturado
        return facturado

    # Devuelve por consola aquellos abonados suscritos a un abono Anual.
    def consulta_abonados_anuales(self):
        abonados = list()
        for x in self.repositorios[2].find_all():
            if x.tipo_abono == "Anual":
                abonados.append(x)
                print(x)

    # Devuelve la facturación histórica de los abonos anuales.
    def cobro_abonos_anuales(self):
        total = 0
        for x in self.repositorios[2].cobros:
            if x.get("Anual") is not None:
                total += x.get("Anual")
        return total

    # Crea un nuevo abono. El id del abono se genera automáticamente.
    def alta_abonado(self, tipo_abono, id_plaza):
        id_abono = len(self.repositorios[2].abonos) + 1
        self.__repositorios[2].create_abono(id_abono, tipo_abono, id_plaza)

    # Incompleto
    def modificar_abonado(self, id_abono):
        abonado_a_modificar = self.repositorios[2].find_by_id(id_abono)
        if not abonado_a_modificar:
            print("Abonado no encontrado")
        else:
            pass

    # Renueva un abono por el período de tiempo especificado. Se cobra automáticamente una vez realizada la
    # renovación.
    def renovar_abono(self, id_abono):
        abono_a_renovar = self.repositorios[2].find_by_id(id_abono)
        if abono_a_renovar:
            try:
                op = int(input(elegir_abono_print()))
                if op == 1:
                    abono_a_renovar.tipo_abono = "Mes"
                    abono_a_renovar.establecer_caducidad()
                    abono_a_renovar.establecer_precio()
                elif op == 2:
                    abono_a_renovar.tipo_abono = "Trimestral"
                    abono_a_renovar.establecer_caducidad()
                    abono_a_renovar.establecer_precio()
                elif op == 3:
                    abono_a_renovar.tipo_abono = "Semestral"
                    abono_a_renovar.establecer_caducidad()
                    abono_a_renovar.establecer_precio()
                elif op == 4:
                    abono_a_renovar.tipo_abono = "Anual"
                    abono_a_renovar.establecer_caducidad()
                    abono_a_renovar.establecer_precio()
                else:
                    print("Operación abortada.")
            except ValueError:
                print("Error: Valor introducido inválido.")
        self.repositorios[2].cobros.append(dict([(abono_a_renovar.tipo_abono, abono_a_renovar.precio)]))

    # Elimina un abono.
    def borrar_abonado(self, id_abonado):
        abonado_a_modificar = self.repositorios[2].find_by_id(id_abonado)
        if not abonado_a_modificar:
            print("Abonado no encontrado")
        else:
            self.repositorios[2].delete_abono(id_abonado)
            print("Borrado con éxito.")

    # Devuelve por consola el id de aquellos abonos que caduquen en los próximos 30 días.
    def consultar_caducidad_mensual(self):
        fecha_actual = date.today()
        mes_siguiente = fecha_actual + timedelta(days=30)
        listado_abonos = []
        for x in self.repositorios[2].abonos:
            if fecha_actual <= x.fecha_fin <= mes_siguiente:
                listado_abonos.append(x.id_abono)
        for x in listado_abonos:
            print("El abono con ID " + str(x) + " caducará este mes.")

    # Devuelve por consola el id de aquellos abonos que caduquen en los próximos 10 días.
    def consultar_caducidad_10_dias(self):
        fecha_actual = date.today()
        mes_siguiente = fecha_actual + timedelta(days=10)
        listado_abonos = []
        for x in self.repositorios[2].abonos:
            if fecha_actual <= x.fecha_fin <= mes_siguiente:
                listado_abonos.append(x.id_abono)
        for x in listado_abonos:
            print("El abono con ID " + str(x) + " caducará este mes.")



# Testeo
# if __name__ == "__main__":
#     repository = PlazaRepository()
#     repository_tickets = TicketRepository()
    # repository_tickets.load_tickets()
    # repository_abono = AbonoRepository()
    # service = AdminService(repository, repository_tickets, repository_abono)
    # service.alta_abonado("Anual", 1)
    # service.alta_abonado("Anual", 2)
    # service.alta_abonado("Anual", 3)
    # service.alta_abonado("Mensual", 4)
    # service.alta_abonado("Mensual", 5)
    # service.alta_abonado("Trimestral", 6)
    # service.consulta_abonados_anuales()
    # print(service.modificar_abonado(3))
    # print(service.borrar_abonado(1))
    # for x in repository_abono.abonos:
    #     print(x)
    # service.renovar_abono(1)
    # for x in repository_abono.abonos:
    #     print(x)
    # print(repository_abono.cobros)
    # print(service.cobro_abonos_anuales())
    # service.comprobar_parking()



