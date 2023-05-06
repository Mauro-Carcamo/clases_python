#INSTRUCCIONES
#Lee con atención cada uno de los requerimientos que se presentan a continuación, y desarrolla la
#prueba de acuerdo con lo solicitado.
#DESCRIPCIÓN
#Dada la siguiente lista de nombres:
#• Harry Houdini
#• Newton
#• David Blaine
#• Hawking
#• Messi
#• Teller
#• Einstein
#• Pele
#• Juanes
#Y sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton, Hawking y
#Einstein son científicos. Debemos separar los nombres en tres grupos: magos, científicos y otros; y
#escribir una función llamada hacer_grandioso(), que modifique la lista de magos añadiendo la
#frase ‘El gran‘ antes del nombre de cada mago.
#Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de la
#lista.
#Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados; luego
#imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes.



lista= (
"Harry Houdini",
"Newton",
"David Blaine",
"Hawking",
"Messi",
"Teller",
"Einstein",
"Pele",
"Juanes"
)

magos = [lista[0],lista[2],lista[5]]
print(magos)

cientificos = [lista[1],lista[3],lista[6]]
print(cientificos)

otros = [lista[5],lista[7],lista[8]]
print(otros)

def hacer_grandioso ():
    for i in magos:
        print(f'El Gran {i}')

def imprimir_nombre ():
        for name in lista:
            print(name)

hacer_grandioso()#llamo funcion
imprimir_nombre()