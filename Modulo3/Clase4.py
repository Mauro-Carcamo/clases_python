# Estructura de datos llamada Diccionario , palabras y cada palabra un significado especifico
# Tienen un orden
# Son mutables
# Calves deben ser univas
# Son de muy rapido acceso
# deben tener una KEY "D"  y un valor "1" , "d1"
print("====Trabajando con diccionarios=====")

empty_dict = {}
fullfiled_dict = {
    "id": 1,
    "name": "Mauricio"
}

lista_1 = ['a1', 'b2']
print(lista_1)
dict_converted = dict(lista_1)  # convierte la lista en diccionario
# separa los caracteres y los guarda independeinte
print(lista_1, dict_converted)

tupla_1 = ('a1', 'b2')
print(lista_1, dict(tupla_1))

lista_dimensional = [['a', 1], ['b', 2]]
print(lista_dimensional, dict(lista_dimensional))

diccionario_prueba = {'d1', 'd2', 'd3', 'd4'}
print(diccionario_prueba)

# obtener elemento varible["clave"]
# añador un elemento varible["clave"]
# modificar un elementno: varible["clave"] = valor nuevo
# elminiar elemento: del varible["clave"]

full_dict_2 = dict(
    genero="M",
    nacionalidad="E"
)
print(full_dict_2)

# itetar diccionarios por clave o valor
empleado = {
    "name": "Mauricio",
    "apellido": "Carcamo",
    "edad": 33,
    "rut": "17402232-3"
}
print(empleado)
for variablex in empleado.values():
    print(variablex)

for a, b in empleado.items():
    print(a, b)
    # agarra la key el valor de el diccionario


# Condicionales
# if condicion :
edad = 30
if edad > 10:
    print("hola")
    print("hola desde dentro del if")


temperatura = 35
pais = "Chile"
if temperatura >= 37:
    print("alerta temp alta")
else:
    print("la temperatura normal")


if temperatura < 10:
    if pais == 'Chile':
        print('imprime aca')
    else:
        print("cualquier cosa")
else:
    if pais == 'Chile':
        print('1111')
    else:
        print("2222")


vuela = ""
humano = "no"
usa_mascara = "no"


#if vuela == "si" and humano == "si" and usa_mascara == "si":
 #   print("No existe")
#else:
 #   print("Groot")
#elif vuela == "si" and humano == "no" and usa_mascara == "si":
 #   print("Super no humano vuela usa mascara")
#elif print("Spiderman")


#Trabajo con While y ciclos
# mientras se ejecuta cierta funcion ejecuta este codigo
# While condicion : (importante la identacion para que esten dentro del while)

want_exit = "n"
while want_exit == "n":
    print("hola como estas")
    want_exit = input("quieres salir s/n")


want_exit = "n"
num_questions = 0
while want_exit == "n":
    print("Hola como estas")
    want_exit = input("Quieres salir S/N ? ")
    num_questions += 1
    if num_questions == 4:
        print("Alcansaste el maximo posible")
        break
print("Se acabo el while")


