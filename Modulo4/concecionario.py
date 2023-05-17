#Vende Autos y Motos,Bicicleta
#Autos: [color, tipo_motor, ruedas, cantidad_puertas, tipo_frenos, tipo_encendido,modelo]
#Motos: [color,tipo_motor, ruedas, modelo, tipo_freno, tipo_encendido]
#Bicicletas:[color,marca,modelo,rueda,tipo_manubrio]

class Vehiculos:
    def __init__(self, _color, _ruedas, _tipo_frenos) -> None:
        self.color = _color
        self.ruedas = _ruedas
        self.tipo_freno = _tipo_frenos

##Clase herencia multipe
class VehiculosMotorizados:
    def __init__(self,_tipo_motor,_tipo_encendido) -> None:
        self.tipo_motor = _tipo_motor
        self.tipo_encendido = _tipo_encendido


class Auto(Vehiculos):
    def __init__(self, _color, _ruedas, _tipo_frenos, _tipo_motor, _tipo_encendidoo) -> None:
        super().__init__(self, _color, _ruedas, _tipo_frenos)
        VehiculosMotorizados.__init__(self, _tipo_motor,_tipo_encendidoo)


#metodo debe ser una accion

    def abrir_puerta (self, _puerta):
        print(f'abriendo la puerta { _puerta}')

class Moto(Vehiculos):
    def __init__(self, _color, _ruedas, _tipo_frenos, _tipo_motor, _tipo_encendidoo,_tipo_cadena) -> None:
        super().__init__(_color, _ruedas, _tipo_frenos)
        VehiculosMotorizados.__init__(self, _tipo_motor,_tipo_encendidoo)
        self.tipo_cadena = _tipo_cadena


class Bicicleta(Vehiculos):
    def __init__(self, _color, _ruedas, _tipo_frenos, _tipo_manubrio, _tipo_alforja) -> None:
        super().__init__(_color, _ruedas, _tipo_frenos)
        self.tipo_manubrio = _tipo_manubrio
        self.tipo_alforja = _tipo_alforja

    def pedalear (self, _pedalear):
        print (f'pedalear {_pedalear}')