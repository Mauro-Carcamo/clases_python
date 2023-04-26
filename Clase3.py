#TRABAJO CON STRING

first_name = "Mauricio"
last_name = "Carcamo"

print(first_name, last_name)

mensaje3 = ("hola") * 3
print(mensaje3)
mensaje3 += "," #+= añade 
print(mensaje3)

#Funcion propia, OWN Function -> busca la coincidencia en una cadena.

cadena = "esto es una oracion por ucrania"
posicion = cadena.find("pelo") # se crea una variable que tenga .find para buscar en otra variable
print("pelo se encuentra en:", posicion) # pelo se encuentra en -1 , pelo no existe
posicion = cadena.find("ucrania")
print("ucrania se encuentra entra en:",posicion) #ucrania esta en la posicion 24

# concatenar: unir dos o mas string simbolo + 
# multiplicar : * multiplicacion de cadenas
# añadir: +=
# Funcion [buil in]: len ->
# funcion replace, remplaza el primer parametro por el segundo en la cadena

ejemplo = "OYE JAVO PARA LA WEA PO HOMBRE"
fun_minuscula = ejemplo.lower() 
print(fun_minuscula) 

ejemplo2 = "esto se va a convertir en miniscula"
fun_mayuscula = ejemplo2.upper() # agregar () al final para que funcione
print(fun_mayuscula)

ejemplo3 = "esto es un ejemplo"
fun_reemplazar = ejemplo3.replace("ejemplo", "CASA")#reemplazo de la cadena ejemplo por casa
print(fun_reemplazar)
print(fun_reemplazar.replace("ejemplo", "CASA"))# sirve tambien , no es necesario siempre crear una 
#variable para hacer funcionar la funcion. Se puede print y dentro la funcion con la variable que tiene le valor o atributo 


#LISTAS
#Estructuras de datos mas complejos, no primitivos.
#(parecido a los array en js)

empty_list = []
print (empty_list)

full_list = [1,2,3, 1.5 , ["hola", 2] , {"mauro", "Carcamo"} , (1,2,3) ]
print(full_list)

segunda_lista = list() # si declaro una lista vacia es mejor con []
print(segunda_lista)

#Range 
print (list("concurso"))
rango_one = range (10)
print(list(rango_one))

print("=============listas=========")
# Agregar item a la lista --> append
# Seleccionar o extraer un item de la lista: con la posicion ->lista [posicion]
# 
numeros = [1 , 2, 3, 4, 5]
print(numeros)
numeros.append (10)
print(numeros)
# Seleccion un item de una lista , con la posicion
print(numeros[2])
#eliminar valores de una lista REMOVE, DEL, POP.
numeros.remove(3) # saco valor 3 !
print(numeros)
del numeros[2] #elimino posicion 2 
print(numeros) #otra forma de eliminar valor

#recorer la lista con for y range
for i in range(len(numeros)):
    print(numeros[i])

#Tupla, es con parentesis y es inmodificable

tupla1 = (1, "mauro" , 500.678)
print(tupla1)
print(type(tupla1))

#funacion en tuplas
#reverse()
#append()
#remove()
#clear()
#sort()








