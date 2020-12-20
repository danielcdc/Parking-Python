from model.Parking import Parking
import pickle


class ParkingRepository:
    def __init__(self, num_plazas=100):
        self.__directorio = "../DataBase/Parking.pckl"
        self.__fichero = None
        self.__parking = Parking(num_plazas)

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
    def parking(self):
        return self.__parking

    @parking.setter
    def parking(self, value):
        self.__parking = value

    # Métodos CRUD
    def create_parking(self, num_plazas):
        self.parking = Parking(num_plazas)

    def delete_parking(self):
        self.parking = None

    # Métodos que manejan los ficheros pickle
    def load_parking(self):
        try:
            self.fichero = open(self.directorio, "rb")
            self.parking = pickle.load(self.fichero)
            self.fichero.close()
        except EOFError:
            print("El fichero está vacío.")

    def save_plaza(self):
        self.fichero = open(self.directorio, "wb")
        pickle.dump(self.parking, self.fichero)
        self.fichero.close()

if __name__ == "__main__":
    parking_repository = ParkingRepository()
    print(parking_repository.parking)