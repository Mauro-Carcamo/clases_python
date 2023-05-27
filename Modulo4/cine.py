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
    def __init__(self, _nombre_pelicula, _horario):
        self.pelicula = _nombre_pelicula
        self.horario = _horario


class Cartelera:
    def __init__(self):
        self.funcion = []

    def crear_funcion (self, dia,pelicula,horario,sala):
        if dia not in self.funcion:
            self.funcion[dia] = []
            cartelera = {
            "dia":dia,
            "pelicula":pelicula,
            "horariro":horario,
            "sala":sala
        }
        self.funcion[dia].append(cartelera)



class Boleto:
    def __init__(self, _asiento, _horario, _nombre_pelicula):
        self.asiento = _asiento
        self.horario = _horario
        self.pelicula =  _nombre_pelicula

class Boleteria: 
        #contar boletos vendidos 
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



#cine1 = Cine("Cinepolis", "111111111.1", "Av.cine 90")
#sala1 = Sala(1, ["A1", "A2", "A3", "B1", "B2", "B3"], ["9:00", "12:00", "15:00"])
#sala2 = Sala(2, ["A1", "A2", "A3", "B1", "B2", "B3"], ["9:00", "12:00", "15:00"])
#pelicula1 = Pelicula("Inception")
#pelicula2 = Pelicula("Whiplash")

#cartelera = Cartelera()
#cartelera.crear_funcion("lunes",pelicula1,"9:00",sala1)
#print(cartelera)


boleteria_cine= Boleteria()
boleteria_cine.vender_boletos("A1","StarWars","9:00")
boleteria_cine.vender_boletos("A1","StarWars","9:00")



#boletos_pelicula1.vender_boleto("A1")
#boletos_pelicula1.vender_boleto("A2")  
#boletos_pelicula1.vender_boleto("A1")
#boletos_pelicula1.vender_boleto("A2")   