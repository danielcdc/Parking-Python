def comprobar_parking_print(dicc):
    for x, y in dicc.items():
        print("Plaza " + x + " : " + y)


def elegir_abono_print():
    print('''Introduzca la opción deseada: 
    1. Mensual
    2. Trimestral
    3. Semestral
    4. Anual
    Otro número: Cancelar''')