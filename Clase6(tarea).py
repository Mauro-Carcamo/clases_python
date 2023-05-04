# Escriba una clase MobilePhone que represente un telefono movil.
# Atributos
# manufacturer ( cadena de texto)
# screen_size (flotante)
# apps (lista de cadenas de texto)
# status (false: apagado, True: encendido)
# Metodos
# _init_(self, manufacturer, screen_size, num:cores)
#power_on(self)
#power_off(self)
# install_app(self, app)
#uninstall_app(sels, app)


class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps =[]
        self.status = False

    def power_on(self):
        self.status = True
        print("Bienvenido")
        

    def power_off(self):
        self.status = False
        print ("Adios")

    def install_app(self,app):
        self.apps.append
        
##REVISAR COMIENZO CLASE 8

#iphone = MobilePhone ('chinese', 60.9 , 2 , "Whatsapp")
#huawei = MobilePhone ('australian', 100.6 , 4, "Whatsapp")
#nokia = MobilePhone ('finlandia', 600.8 , 7, "Whatsapp" )