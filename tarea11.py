class Micro:
    
    def __init__(self, patente):
        self.patente = patente
        self.usuarios = {"Mujer": 0, "Hombre": 0, "Niño": 0, "Adulto Mayor": 0}
        self.total_recaudado = 0
    
    def registrar_usuario(self, tipo_usuario):
        if tipo_usuario == "Niño":
            print("El niño no debe pagar")
        else:
            if tipo_usuario == "Adulto Mayor":
                tarifa = 365
            else:
                tarifa = 730
            
            self.usuarios[tipo_usuario] += 1
            self.total_recaudado += tarifa
            
            print("Acceso permitido")