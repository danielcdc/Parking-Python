from model import Usuario
import pickle


class UsuarioRepository:
    def __init__(self):
        self.__directorio = "../DataBase/Abonado.pckl"
        self.__fichero = None
        self.__usuarios = list()

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
    def usuarios(self):
        return self.__usuarios

    @usuarios.setter
    def usuarios(self, value):
        self.__usuarios = value

    # Métodos CRUD
    def create_abonado(self, dni, nombre, apellidos,num_tarjeta, email, vehiculo, abono):
        self.usuarios.append(Usuario.Abonado(dni, nombre, apellidos,num_tarjeta, email, vehiculo, abono))

    def delete_abonado(self, id):
        try:
            self.usuarios.remove(self.find_by_id(id))
        except ValueError:
            print("No se ha encontrado el elemento.")

    # Métodos que manejan los ficheros pickle
    def load_usuarios(self):
        try:
            self.fichero = open(self.directorio, "rb")
            self.usuarios = pickle.load(self.fichero)
            self.fichero.close()
        except EOFError:
            print("El fichero está vacío.")

    def save_usuarios(self):
        self.fichero = open(self.directorio, "wb")
        pickle.dump(self.usuarios, self.fichero)
        self.fichero.close()

    # Métodos de búsqueda
    def find_by_id(self, id):
        for x in self.usuarios:
            if x.Plaza.idPlaza == id:
                return x
        return False

    def find_all(self):
        return self.usuarios