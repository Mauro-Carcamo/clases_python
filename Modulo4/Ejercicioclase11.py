#2.- se requiere realizar un programa para vender que sirva para controlar la operación diaria de un cine

#- Registrar un cine (nombre, rut y dirección)
#- Registrar las salas y sus asientos (numeración)
#- Se puedan registar la cartelera de cada día, las películas de ese día y los respectivos horarios, registrar las salas de cada película
#- Colocar un valor estándar por tipo de entrada, normal o vip, 
#- Poder vender la boletería de cada dia y asignar asientos por ticket, verificar que el asiento escogido ya no este vendido
#- Reportar las entradas totales vendidas por cada dia
#- Reportar las entradas vendidas por cada función
#- Reportar las entradas totales vendidas por películas
#- Reportar las entradas totales vendidas por cada dia, película y funcion


#NOTA: debe considerar diagramar las clases que interactuaran en el programa, así como manejar las excepciones, y hacer un menu de seleccion de las opciones


class Cine:
    def __init__(self, nombre, rut, direccion):
        self.nombre = nombre
        self.rut = rut
        self.direccion = direccion

class Sala:
    def __init__(self, numero, asientos, horarios):
        self.numero = numero
        self.asientos = asientos
        self.horarios = horarios

class Pelicula:
    def __init__(self, nombre, salas, horarios):
        self.nombre = nombre
        self.salas = salas
        self.horarios = horarios

class Boletos:
    def __init__(self, tipo, asientos_vendidos):
        self.tipo = tipo
        self.asientos_vendidos = asientos_vendidos
venta_normal = 0
venta_vip = 0

def vender_boletos(pelicula, sala, horario, tipo_boleto, asiento):
    # Verificar que el asiento no esté vendido
    if asiento in boletos.asientos_vendidos:
        print("Lo sentimos, ese asiento ya fue vendido.")
    else:
        # Asignar el asiento
        boletos.asientos_vendidos.append(asiento)

        # Registar la venta de boletos
        if tipo_boleto == "normal":
            venta_normal = venta_normal + 1
        else:
            venta_vip = venta_vip + 1

def reporte_diario():
    # Obtener la cantidad de boletos vendidos por día
    for dia in range(1, 31): # Suponiendo que el cine está abierto los 30 días del mes
        boletos_vendidos = 0
        for pelicula in cartelera[dia]:
            for sala in pelicula.salas:
                for horario in sala.horarios:
                    for boleto in horario.boletos:
                        boletos_vendidos = boletos_vendidos + len(boleto.asientos_vendidos)
            print("El día", dia, "se vendieron", boletos_vendidos, "entradas")

def reporte_entradas_funcion(pelicula, sala, horario):
    # Obtener la cantidad de boletos vendidos para una función específica
    boletos_vendidos = 0
    for boleto in horario.boletos:
        boletos_vendidos = boletos_vendidos + len(boleto.asientos_vendidos)
    print("Para la función de la película", pelicula, "en la sala", sala, "a las", horario, "se vendieron", boletos_vendidos, "entradas")

def reporte_entradas_pelicula(pelicula):
    # Obtener la cantidad de boletos vendidos para una película específica
    boletos_vendidos = 0
    for dia in range(1, 31):
        for horario in pelicula.horarios:
            for sala in pelicula.salas:
                for boleto in horario.boletos:
                    boletos_vendidos = boletos_vendidos + len(boleto.asientos_vendidos)
    print("Para la película", pelicula, "se vendieron", boletos_vendidos, "boletos en total")

def reporte_entradas_dia(dia):
    # Obtener la cantidad de boletos vendidos para todas las películas en un día específico
    boletos_vendidos = 0
    for pelicula in cartelera[dia]:
        for horario in pelicula.horarios:
            for sala in pelicula.salas:
                for boleto in horario.boletos:
                    boletos_vendidos = boletos_vendidos + len(boleto.asientos_vendidos)
        print("Para el día", dia, "la película", pelicula.nombre, "se vendieron", boletos_vendidos, "boletos")

# Ejemplo de uso
cine = Cine("Cinepolis", "11111111-1", "Av. Ejemplo #123")
sala1 = Sala(1, ["A1", "A2", "B1", "B2", "C1", "C2"], ["12:00", "15:00", "18:00"])
sala2 = Sala(2, ["A1", "A2", "B1", "B2", "C1", "C2"], ["13:00", "16:00", "19:00"])
pelicula1 = Pelicula("Avengers: Endgame", [sala1, sala2], ["12:00", "13:00", "15:00", "16:00", "18:00", "19:00"])
pelicula2 = Pelicula("Toy Story 4", [sala1], ["14:00", "17:00"])
cartelera = {
    1: [pelicula1],
    2: [pelicula1, pelicula2],
    3: [pelicula2]
}
venta_normal = 0
venta_vip = 0
boletos = Boletos("normal", [])
vender_boletos(pelicula1, sala2, "19:00", "normal", "A1")
vender_boletos(pelicula2, sala1, "14:00", "vip", "B1")
reporte_diario()
reporte_entradas_funcion(pelicula1, sala2, "19:00")
reporte_entradas_pelicula(pelicula1)
reporte_entradas_dia(2)