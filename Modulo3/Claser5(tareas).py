# 1. Cree un programa que encuentre el promedio de los tres puntajes dados y devuelva el valor de la letra
# asociada con esa calificación. con al siguiente tabla
#     0   - 2     D
#     2.1 - 5     C
#     5.1 - 6     B
#     6.1 - 7     A
print("===========================")
print("=======EJERCICIO 1==============")
print("===========================")

nota = 1

while nota == 1:
    nota1 = float(input("ingresa primera nota: "))
    nota2 = float(input("ingresa segunda nota: "))
    nota3 = float(input("ingresa tercera nota: "))

    nota = float((nota1 + nota2 + nota3)/3)

    if nota >= 0 and nota <= 2:
        print("D")
    elif nota >= 2.1 and nota <= 5:
        print("C")
    elif nota >= 5.1 and nota <= 6:
        print("B")
    elif nota >= 6.1 and nota <= 7:
        print("A")
    else:
        print("Eso esta fuera del rango de una nota")

# 2. utilizando dos while anidados, construya la tablas de mutiplicacion, ejemplo
#     Ejemplo whiole anidados:
#     while codicion1
#         while codicion2
#
print("===========================")
print("=======EJERCICIO 2==============")
print("===========================")


tabla = 0
num = 0
while tabla < 13:
    print("Tabla del", tabla)
    while num < 13:
        print(tabla, "X", num, "=", tabla*num)
        num += 1
    tabla += 1
    num -= 13

# 3. Escriba un programa que calcule el máximo común divisor entre dos números enteros.
print("===========================")
print("=======EJERCICIO 3==============")
print("===========================")

primero = int(input("Ingrese el primer número: "))
segundo = int(input("Ingrese el segundo número: "))

while segundo != 0:
    resultado = primero % segundo
    primero = segundo
    segundo = resultado

print("Tu maximo comun divisor es:", resultado)

# 4. Dado un mes como un número entero del 1 al 12, devuelva a qué trimestre del año pertenece como un número entero.
#     Por ejemplo: el mes 2 (febrero), forma parte del primer trimestre; el mes 6 (junio),
#     forma parte del segundo trimestre; y el mes 11 (noviembre), forma parte del cuarto trimestre.

print("===========================")
print("=======EJERCICIO 4==============")
print("===========================")

mes = "x"
while mes == "x":
    mes = (int(input("Ingresa numero de mes: ")))
    if mes >= 1 and mes <= 3:
        print("Primer Trimestre")
    elif mes >= 4 and mes <= 6:
        print("Segundo Trimestre")
    elif mes >= 7 and mes <= 9:
        print("Tercer Trimestre")
    elif mes >= 10 and mes <= 12:
        print("Cuarto Trimestre")


# 5. Escriba un programa que eliminar un signo de exclamación del final de una cadena.
#     puede suponer que los datos de entrada son siempre una cadena, no es necesario verificarlos.
print("===========================")
print("=======EJERCICIO 5==============")
print("===========================")

frase = 0
while frase == 0:
    frase = str(input("Frase con ! : "))
    if frase[-1] == "!":
        print(frase[:-1])
    else:
        print(frase)

# 6. Se le asignado un tarea para programar un algoritmo para una lavadora, debe investigar cuanta agua se neceita para lavar prendas
#     con las siguientes caracteriticas, algodon, nilon, poliester, debe investigar para una lavadora de xx kg cuantas prendas de cada una puede
#     lavar entendiendo, que solo se puede lavar ropa de un mismo tipo y asi poder calcular lo siguiente

#     Por ejemplo, si la carga es 10, la cantidad de agua que requiere es 5 y la cantidad de ropa a lavar es 14, entonces necesitas 5 * 1.1 ^ (14 - 10) cantidad de agua.

#     Escribe una función para calcular cuánta agua se necesita si tienes una cantidad de ropa.
#     La función aceptará 2 argumentos: - carga lavadora y ropa.

print("===========================")
print("=======EJERCICIO 6==============")
print("===========================")

print("**Hola soy una lavadora que tiene la capacidad de 10 kilos**")

prenda = 0

while prenda == 0:
    print("Que tipo de prenda quieres lavar?: ")
    print(" 1- Algodon")
    print(" 2- Nilon")
    print(" 3- Poliester")
    if prenda == 0:
        ropa = int(input("Ingresa Numero: "))
        if ropa >= 1 and ropa <= 3:
            carga = int(input("Cuantas Prendas?:"))
        else:
            print("No esta dentro de las opciones")
            break
    

    



# 7. Crele una función notaFina, que calcule la nota final de un estudiante en función de dos parámetros: una nota para el examen y una cantidad de proyectos completados.
#     Esta función debe tomar dos argumentos: examen - calificación del examen (de 0 a 100); proyectos - número de proyectos completados (de 0 en adelante);
#     Esta función debería devolver un número (calificación final). Hay cuatro tipos de calificaciones finales:

#     100, si la calificación del examen es superior a 90 o si el número de proyectos terminados es superior a 10.
#     90, si la calificación del examen es superior a 75 y si el número de proyectos completados es mínimo 5.
#     75, si la calificación del examen es superior a 50 y si el número de proyectos completados es mínimo 2.

print("===========================")
print("=======EJERCICIO 7==============")
print("===========================")

nota_examen = 0
numero_proyectos = 0

while nota_examen == 0:
    nota_examen = int(input("Ingresa Nota de Examen: "))
    numero_proyectos = int(input("Ingresa Numero de Proyectos: "))
    if nota_examen >= 90:
        nota_examen = 100
    elif nota_examen >= 75:
        nota_examen = 90
    elif nota_examen >= 50:
        nota_examen = 75
    else:
        nota_examen = 0
    if numero_proyectos >= 10:
        numero_proyectos = 100
    elif numero_proyectos >= 5:
        numero_proyectos = 90
    elif numero_proyectos >= 2:
        numero_proyectos = 75
    else:
        numero_proyectos = 0
    suma_final = nota_examen + numero_proyectos
    print("Tu Calificacion Final es:", suma_final/2)
    
