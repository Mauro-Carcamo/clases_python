renta_actual = int(input("Cual es tu Renta? :  "))

if renta_actual < 10000 :
    print("Tipo Impositivo 5%")
elif renta_actual >= 10000 and renta_actual < 20000 :
    print("Tipo Impositivo 15%")
elif renta_actual >= 20000 and renta_actual < 35000 :
    print("Tipo Impositivo 20%")
elif renta_actual >= 35000 and renta_actual < 60000 :
    print("Tipo Impositivo 30%")
elif renta_actual >= 60000  :
    print("Tipo Impositivo 45%")
