from model import Plaza
import pickle

# Hay que regular el cupo del parking (70/15/15)
#  ¿Una colección por cada tipo de parking?


class PlazaRepository:
    def __init__(self):
        self.__directorio = "../DataBase/Plazas.pckl"
        self.__fichero = None
        self.__plazas = list()

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
    def plazas(self):
        return self.__plazas

    @plazas.setter
    def plazas(self, value):
        self.__plazas = value

    # Métodos CRUD
    def create_plaza(self, id, tipo):
        self.plazas.append(Plaza.Plaza(id, tipo))

    def delete_plaza(self, id):
        try:
            self.plazas.remove(self.find_by_id(id))
        except ValueError:
            print("No se ha encontrado el elemento.")

    # Métodos que manejan los ficheros pickle
    def load_plaza(self):
        try:
            self.fichero = open(self.directorio, "rb")
            self.plazas = pickle.load(self.fichero)
            self.fichero.close()
        except EOFError:
            print("El fichero está vacío.")

    def save_plaza(self):
        self.fichero = open(self.directorio, "wb")
        pickle.dump(self.plazas, self.fichero)
        self.fichero.close()

    # Métodos de búsqueda
    def find_by_id(self, id):
        for x in self.plazas:
            if x.Plaza.idPlaza == id:
                return x
        return False

    def find_all(self):
        return self.plazas

# Testing
# if __name__ == "__main__":
#     parking = PlazaRepository()
#     parking.create_plaza(2, "Caravana")
#     parking.save_plaza()
#     for x in parking.plazas:
#         print(x)