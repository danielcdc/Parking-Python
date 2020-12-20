class Plaza:
    def __init__(self, id_plaza, tipo):
        self.__idPlaza = id_plaza
        self.__tipo = tipo
        self.__ocupada = False
        self.__abonado = None
        self.__fechaOcup = None
        self.__horaOcup = None

    @property
    def idPlaza(self):
        return self.__idPlaza

    @idPlaza.setter
    def idPlaza(self, value):
        self.__idPlaza = value

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, value):
        self.__tipo = value

    @property
    def ocupada(self):
        return self.__ocupada

    @ocupada.setter
    def ocupada(self, value):
        self.__ocupada = value

    @property
    def abonado(self):
        return self.__abonado

    @abonado.setter
    def abonado(self, value):
        self.__abonado = value

    @property
    def fechaOcup(self):
        return self.__fechaOcup

    @fechaOcup.setter
    def fechaOcup(self, value):
        self.__fechaOcup = value

    @property
    def horaOcup(self):
        return self.__horaOcup

    @horaOcup.setter
    def horaOcup(self, value):
        self.__horaOcup = value

    def __str__(self):
        return "ID: " + str(self.idPlaza) + "\n" + "Tipo de vehículo: " + self.tipo