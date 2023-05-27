#Acceso Directo a los atributos
#Objeto.atributo #Para obtener.
#Objeto.atriburo = valor #Modificado desde afuera

class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type 

#instanciar clase
gato = Animal ("Angora","Persa")
print(gato.type)
gato.type = "Calico"
print(gato.type)      

perro = Animal ("Cachupin","Kiltro")
print(perro.type)
perro.type = "Labrador"
print(perro.type)


class Droid:
    def __init__(self, name):
        self.hidden_name = name

    @property
    def name (self)-> str:
        return self.hidden_name
    
    @name.setter
    def name(self, name: str) -> None:
        self.hidden_name = name

android = Droid("arthur")

print(android.name)
android.name = "C3PO"
print(android.name)

android.hidden_name = "rojo"
print(android.hidden_name)
print(android.name)

##  Valor Calculado
print("*****VALOR CALCULADO******")

class CalculatedValue:
    def __init__(self,_name,_height):
        self.name = _name
        self.height = _height

    @property
    def get_calculate_value(self) -> float:
        return 0.35 * self.height
        
valuex = CalculatedValue ("ratio", 10)

print(f'El {valuex.name} es: {valuex.get_calculate_value}')

class Dog:
    obeys_owner = True

    def __init__(self, _name):
        self.name = _name

dog_one = Dog("Robin")
dog_two = Dog("Panda")
dog_three = Dog("Bruno")

print(f'{dog_one.name} obedece a su dueño {dog_one.obeys_owner}')
print(f'{dog_two.name} obedece a su dueño {dog_two.obeys_owner}')
print(f'{dog_three.name} obedece a su dueño {dog_three.obeys_owner}')

Dog.obeys_owner = False
print(f'{dog_one.name} obedece a su dueño {dog_one.obeys_owner}')
print(f'{dog_two.name} obedece a su dueño {dog_two.obeys_owner}')
print(f'{dog_three.name} obedece a su dueño {dog_three.obeys_owner}')