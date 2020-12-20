import random


def generar_pin():
    return random.randrange(1, 1000000)


def generar_matricula():
    matricula = ""
    control = 0
    while control < 4:
        matricula += str(random.randint(0, 9))
        control += 1
    matricula += "-"
    while control < 7:
        matricula += chr(random.randint(65, 91))
        control += 1
    return matricula


def generar_dni():
    chain = "TRWAGMYFPDXBNJZSQVHLCKET"
    dni = ""
    control = 0
    while control < 8:
        dni += str(random.randint(0, 9))
        control += 1
    letra = chain[int(dni) % 23]
    dni += "-" + letra
    return dni
