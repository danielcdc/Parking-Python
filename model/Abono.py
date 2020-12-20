from datetime import *
from utilities.Utils import *


class Abono:
    def __init__(self, id_abono, tipo_abono, id_plaza):
        self.__id_abono = id_abono
        self.__tipo_abono = tipo_abono
        self.__id_plaza = id_plaza
        self.__pin = generar_pin()
        self.__dni = generar_dni()
        self.__fecha_inicio = date.today()
        self.__fechaFin = None
        self.__precio = self.establecer_precio()
        self.__isActivo = True
        self.establecer_caducidad()

    @property
    def id_abono(self):
        return self.__id_abono

    @id_abono.setter
    def id_abono(self, value):
        self.__id_abono = value

    @property
    def tipo_abono(self):
        return self.__tipo_abono

    @tipo_abono.setter
    def tipo_abono(self, value):
        self.__tipo_abono = value

    @property
    def id_plaza(self):
        return self.__id_plaza

    @id_plaza.setter
    def id_plaza(self, value):
        self.__id_plaza = value

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        self.__pin = value

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, value):
        self.__dni = value

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value):
        self.__fecha_inicio = value

    @property
    def fecha_fin(self):
        return self.__fechaFin

    @fecha_fin.setter
    def fecha_fin(self, value):
        self.__fechaFin = value

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, value):
        self.__precio = value

    @property
    def is_activo(self):
        return self.__isActivo

    @is_activo.setter
    def is_activo(self, value):
        self.__isActivo = value

    def __str__(self):
        return "ID Abono: " + str(self.id_abono) + "\nID Plaza: " + str(self.id_plaza) + \
               "\nTipo de Abono: " + str(self.tipo_abono) + "\n"

    def establecer_caducidad(self):
        self.fecha_fin = self.fecha_inicio
        if self.tipo_abono == "Mensual":
            self.fecha_fin += timedelta(days=30)
        elif self.tipo_abono == "Trimestral":
            self.fecha_fin += timedelta(days=90)
        elif self.tipo_abono == "Semestral":
            self.fecha_fin += timedelta(days=180)
        else:
            self.fecha_fin += timedelta(days=360)

    def establecer_precio(self):
        if self.tipo_abono == "Mensual":
            precio_abono = 25
        elif self.tipo_abono == "Trimestral":
            precio_abono = 70
        elif self.tipo_abono == "Semestral":
            precio_abono = 130
        else:
            precio_abono = 200
        return precio_abono
