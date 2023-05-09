puntos = float(input("Que puntaje Obtuviste ?: "))
dinero = 2400.0


if puntos >= 0.0 and puntos < 0.4 :
    print(f'NIVEL INACEPTABLE, conseguiste ${puntos*dinero}')
elif puntos >= 0.4 and puntos < 0.6 :
    print(f'NIVEL ACEPTABLE , conseguiste ${puntos*dinero}')
elif puntos >= 0.6 :
    print(f'NIVEL MERITORIO , conseguiste ${puntos*dinero}')
else:
    print("INGRESA UN PUNTAJE VALIDO")