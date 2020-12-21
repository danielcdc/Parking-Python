from utilities import Utils
from datetime import *


class Ticket:
    # Constructor utilizado en la app
    def __init__(self, id_plaza, tipo_vehiculo):
        self.__id_plaza = id_plaza
        self.__tipo_vehiculo = tipo_vehiculo
        self.__matricula = Utils.generar_matricula()
        self.__pin = Utils.generar_pin()
        self.__fecha_deposito = datetime.now()
        self.__fecha_salida = None
        self.__facturado = None

    # Constructor para testing
    def __init__(self, id_plaza, fecha_deposito, fecha_salida, facturado):
        self.__id_plaza = id_plaza
        self.__matricula = Utils.generar_matricula()
        self.__pin = Utils.generar_pin()
        self.__fecha_deposito = fecha_deposito
        self.__fecha_salida = fecha_salida
        self.__facturado = facturado

    @property
    def id_plaza(self):
        return self.__id_plaza

    @id_plaza.setter
    def id_plaza(self, value):
        self.__id_plaza = value

    @property
    def tipo_vehiculo(self):
        return self.__tipo_vehiculo

    @tipo_vehiculo.setter
    def tipo_vehiculo(self, value):
        self.__tipo_vehiculo = value

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, value):
        self.__matricula = value

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        self.__pin = value

    @property
    def fecha_deposito(self):
        return self.__fecha_deposito

    @fecha_deposito.setter
    def fecha_deposito(self, value):
        self.__fecha_deposito = value

    @property
    def fecha_salida(self):
        return self.__fecha_salida

    @fecha_salida.setter
    def fecha_salida(self, value):
        self.__fecha_salida = value

    @property
    def facturado(self):
        return self.__facturado

    @facturado.setter
    def facturado(self, value):
        self.__facturado = value