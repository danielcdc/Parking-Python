from model.Abono import Abono
import pickle


class AbonoRepository:
    def __init__(self):
        self.__directorio = "../DataBase/Tickets.pckl"
        self.__fichero = None
        self.__abonos = list()
        self.__cobros = list()

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
    def abonos(self):
        return self.__abonos

    @abonos.setter
    def abonos(self, value):
        self.__abonos = value
    @property
    def cobros(self):
        return self.__cobros

    @cobros.setter
    def cobros(self, value):
        self.__cobros = value

# Métodos CRUD
    def create_abono(self, id_abono, tipo_abono, id_plaza):
        id_abono = self.check_id_abono_en_uso(id_abono)
        id_plaza = self.check_plaza_ocupada(id_plaza)
        nuevo_abono = Abono(id_abono, tipo_abono, id_plaza)
        # Al crearse un abono, se aplica el cobro correspondiente.
        self.cobros.append(dict([(tipo_abono, nuevo_abono.precio)]))
        self.abonos.append(nuevo_abono)

    def delete_abono(self, id):
        try:
            self.abonos.remove(self.find_by_id(id))
        except ValueError:
            print("No se ha encontrado el elemento.")

    # Métodos que manejan los ficheros pickle
    def load_abonos(self):
        try:
            self.fichero = open(self.directorio, "rb")
            self.abonos = pickle.load(self.fichero)
            self.fichero.close()
        except EOFError:
            print("El fichero está vacío.")

    def save_abonos(self):
        self.fichero = open(self.directorio, "wb")
        pickle.dump(self.abonos, self.fichero)
        self.fichero.close()

    # Métodos de búsqueda
    def find_by_id(self, id):
        for x in self.abonos:
            if x.id_abono == id:
                return x
        return False

    def find_all(self):
        return self.abonos

    def plaza_ocupada(self, id_plaza):
        for x in self.abonos:
            if x.id_plaza == id_plaza:
                return x
        return False

    # Métodos de control
    def check_plaza_ocupada(self, id_plaza):
        control_id_plaza = True
        while control_id_plaza:
            if self.plaza_ocupada(id_plaza):
                id_plaza = int(input("El ID_Plaza introducido ya existe, por favor, introduzca otro: "))
                return id_plaza
            else:
                return id_plaza

    def check_id_abono_en_uso(self, id_abono):
        control_id_abono = True
        while control_id_abono:
            if self.find_by_id(id_abono):
                id_abono = int(input("El ID_Abono introducido ya existe, por favor, introduzca otro: "))
                return id_abono
            else:
                return id_abono