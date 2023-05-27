class Cine:
    def __init__(self, _nombre, _rut, _direccion):
        self.nombre = _nombre
        self.rut = _rut
        self.direccion = _direccion


class Sala:
    def __init__(self, _n_sala, _n_asientos, _horario):
        self.sala = _n_sala
        self.asientos = _n_asientos
        self.horario = _horario


class Pelicula:
    def __init__(self, _nombre_pelicula):
        self.pelicula = _nombre_pelicula



class Cartelera:
    def __init__(self):
        self.funcion = {}

    def crear_funcion (self, dia, _pelicula, horario,sala):
        if dia in self.funcion:
            print("funcion ya creada")
        else:
            self.funcion[dia] = []
            cartelera = {
            "dia":dia,
            "pelicula":_pelicula,
            "horariro":horario,
            "sala":sala
        }
        self.funcion[dia].append(cartelera)
        print("Se ha creado una funcion de cine")


class Boleto:
    def __init__(self, _asiento, _horario, _nombre_pelicula):
        self.asiento = _asiento
        self.horario = _horario
        self.pelicula =  _nombre_pelicula

class Boleteria: 
    def __init__(self) -> None:
        self.boletos = []

    def vender_boletos(self, asiento, nombre_pelicula, horario):
        if len(self.boletos) == 0:
            boleto_temporal = Boleto(asiento,horario,nombre_pelicula)
            self.boletos.append(boleto_temporal)
            print("Boleto Vendido")
        else:    
            for boleto in self.boletos:
                if boleto.pelicula == nombre_pelicula and boleto.horario == horario:
                    if boleto.asiento != asiento:
                        boleto_temporal = Boleto(asiento,horario,nombre_pelicula)
                        self.boletos.append(boleto_temporal)
                        print("Boleto Vendido")
                    else:
                        print("Boleto ya Vendido")

sala1 = Sala(1, ["A1", "A2", "B1", "B2", "C1", "C2"], ["12:00", "15:00", "18:00"])
sala2 = Sala(2, ["A1", "A2", "B1", "B2", "C1", "C2"], ["13:00", "16:00", "19:00"])


pelicula1 = Pelicula("inception")
pelicula2 = Pelicula("Jurasick Park")
pelicula3 = Pelicula ("StarWArs")


boleteria_cine= Boleteria()
boleteria_cine.vender_boletos("A1",pelicula3,"9:00")
boleteria_cine.vender_boletos("A1", pelicula3,"9:00")



cartelera1 = Cartelera()
cartelera1.crear_funcion("lunes",pelicula1, "9:00",sala1)
cartelera2 = Cartelera()
cartelera2.crear_funcion("Martes",pelicula2,"10:00",sala2)
cartelera3 = Cartelera()
cartelera3.crear_funcion("Miercoles",pelicula3,"12:00",sala1)
