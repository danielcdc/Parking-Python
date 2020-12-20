class Usuario:
    def __init__(self, dni, nombre, apellidos):
        self.__id;
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, value):
        self.__dni = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value


class Abonado(Usuario):
    def __init__(self, dni, nombre, apellidos, num_tarjeta, email, vehiculo, abono):
        super().__init__(dni, nombre, apellidos)
        self.__num_tarjeta = num_tarjeta
        self.__email = email
        self.__vehiculo = vehiculo
        self.__abono = abono

    @property
    def num_tarjeta(self):
        return self.__num_tarjeta

    @num_tarjeta.setter
    def num_tarjeta(self, value):
        self.__num_tarjeta = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, value):
        self.__vehiculo = value

    @property
    def abono(self):
        return self.__abono

    @abono.setter
    def abono(self, value):
        self.__abono = value


class Administrador(Usuario):
    def __init__(self, dni, nombre, apellidos, usuario, password):
        super().__init__(dni, nombre, apellidos)
        self.__usuario = usuario
        self.__password = password

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, value):
        self.__usuario = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value
