class Empleado:
    sueldo_base = 100.000

    def __init__(self, _name):
        self.__name = _name
        self.__color = 'Gris'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, _name):
        self.__name = _name


    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, _name):
        self.__name = _name

    @classmethod
    def obtener_sueldo_base(cls):
        return cls.sueldo_base
    
    @classmethod
    def modificar_sueldo_base(cls, _sueldo):
        cls.sueldo_base = _sueldo

print("===============================================")

class Droid:
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

arturo = Droid("Arturo")


print(arturo.name)

## Cree una clase llamada Artefacto, agreguele tres atributos y
## utilice los getter and setter para acceder a lleos


print("===============================================")