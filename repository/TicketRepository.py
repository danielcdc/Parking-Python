from model.Ticket import Ticket
import pickle


class TicketRepository:
    def __init__(self):
        self.__directorio = "../DataBase/Tickets.pckl"
        self.__fichero = None
        self.__tickets = list()

    @property
    def directorio(self):
        return self.__directorio

    @directorio.setter
    def directorio(self, value):
        self.__directorio = value

    @property
    def fichero(self):
        return self.__fichero

    @fichero.setter
    def fichero(self, value):
        self.__fichero = value

    @property
    def tickets(self):
        return self.__tickets

    @tickets.setter
    def tickets(self, value):
        self.__tickets = value

    # Métodos CRUD
    def create_ticket(self, id_plaza, tipo_vehiculo):
        self.tickets.append(Ticket.Ticket(id_plaza, tipo_vehiculo))

    # Para instanciar tickets con datos específicados por el usuario.
    def create_ticket_prueba(self, id_plaza, fecha_deposito, fecha_salida, facturado):
        self.tickets.append(Ticket(id_plaza, fecha_deposito, fecha_salida, facturado))

    def delete_ticket(self, id):
        try:
            self.tickets.remove(self.find_by_id(id))
        except ValueError:
            print("No se ha encontrado el elemento.")

    # Métodos que manejan los ficheros pickle
    def load_tickets(self):
        try:
            self.fichero = open(self.directorio, "rb")
            self.tickets = pickle.load(self.fichero)
            self.fichero.close()
        except EOFError:
            print("El fichero está vacío.")

    def save_tickets(self):
        self.fichero = open(self.directorio, "wb")
        pickle.dump(self.tickets, self.fichero)
        self.fichero.close()

    # Métodos de búsqueda
    def find_by_pin(self, pin):
        for x in self.tickets:
            if x.Ticket.pin == pin:
                return x
        return False

    def find_all(self):
        return self.tickets
