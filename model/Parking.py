import math


class Parking:
    def __init__(self, num_plazas):
        self.__num_plazas = num_plazas
        self.__plazas_turismos = list()
        self.__plazas_motocicletas = list()
        self.__plazas_pmr = list()
        self.__limite_turismos = math.ceil(num_plazas*0.7)
        self.__limite_motocicletas = math.floor(num_plazas*0.15)
        self.__limite_pmr = math.floor(num_plazas*0.15)

    @property
    def num_plazas(self):
        return self.__num_plazas

    @num_plazas.setter
    def num_plazas(self, value):
        self.__num_plazas = value

    @property
    def plazas_turismos(self):
        return self.__plazas_turismos

    @plazas_turismos.setter
    def plazas_turismos(self, value):
        self.__plazas_turismos = value

    @property
    def plazas_motocicletas(self):
        return self.__plazas_motocicletas

    @plazas_motocicletas.setter
    def plazas_motocicletas(self, value):
        self.__plazas_motocicletas = value

    @property
    def plazas_pmr(self):
        return self.__plazas_pmr

    @plazas_pmr.setter
    def plazas_pmr(self, value):
        self.__plazas_pmr = value

    @property
    def limite_turismos(self):
        return self.__limite_turismos

    @limite_turismos.setter
    def limite_turismos(self, value):
        self.__limite_turismos = value

    @property
    def limite_motocicletas(self):
        return self.__limite_motocicletas

    @limite_motocicletas.setter
    def limite_motocicletas(self, value):
        self.__limite_motocicletas = value

    @property
    def limite_pmr(self):
        return self.__limite_pmr

    @limite_pmr.setter
    def limite_pmr(self, value):
        self.__limite_pmr = value

    def __str__(self):
        return "Capacidad total: " + str(self.__num_plazas) + "\nOcupación Turismos: " + str(len(self.__plazas_turismos))\
        + "\nOcupación Motocicletas: " + str(len(self.__plazas_motocicletas)) + "\nOcupación PMR: "\
        + str(len(self.__plazas_pmr)) + "\n\nCupo Turismo: " + str(self.__limite_turismos) + "\nCupo Motocicletas: "\
        + str(self.__limite_motocicletas) + "\nCupo PMR: " + str(self.__limite_pmr)

# Testing
# if __name__ == "__main__":
#     parking = Parking()