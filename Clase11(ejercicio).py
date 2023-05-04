#se necesita realizar un programa basado en clases que permita automatizar el torniquete (control de acceso)
# de una micro, de la siguiente manera
#    1 Las personas que aboradan la micro son, mujeres, hombres, niños y aduto mayor, de los cuales los niños no pagan y lso adultos mayores pagan la tarifa
#      el 50%
#    2 el cobro actual de la micro es de 730 pesos
#    3 por lo que necesitamos un reporte de operacion por dia donde, por micro (cada micro se reguistra por patente), se listen los tipos de usuario y la cantidad total recaudad por 
#      cada, anexar a este reporte el total por dia
#    4. seria interesante que apart6e del reporte anterior que estotal, tener uno filtrado por dia y otro filtrado por persona


class TorniqueteMicro:
    
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
    
    def reporte_operacion_dia(self):
        print("Reporte de operación por día - Patente:", self.patente)
        for tipo_usuario, cantidad in self.usuarios.items():
            print(f"{tipo_usuario}: {cantidad}")
        
        print(f"Total recaudado: {self.total_recaudado}")
    
    def reporte_filtrado_dia(self, fecha):
        print(f"Reporte filtrado por día - Patente: {self.patente} - Fecha: {fecha}")
        for tipo_usuario, cantidad in self.usuarios.items():
            print(f"{tipo_usuario}: {cantidad}")
        
        print(f"Total recaudado: {self.total_recaudado}")
    
    def reporte_filtrado_persona(self, tipo_usuario):
        print(f"Reporte filtrado por persona - Patente: {self.patente} - Tipo de usuario: {tipo_usuario}")
        print(f"Cantidad: {self.usuarios[tipo_usuario]}")
        print(f"Total recaudado: {self.usuarios[tipo_usuario]*730}")
