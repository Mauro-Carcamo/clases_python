#ERRORES PERSONALIZADOS !!! 


class NoPuedeEscribirDosException(Exception):
    def __init__(self, _message):
        self.mesagge = _message

try:
    number = input("introduce un numero")
    if number == "2":
        raise NoPuedeEscribirDosException("Introdujo un numero 2 y este no es valido")
    else:
        print("Numero introducido correctamente")
except Exception as error:
    print(type(error))
    print(error.args)
