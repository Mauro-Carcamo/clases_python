interes = 0.04
monto_incial = float(input("Monto inicial $: "))

ano1 = round(((monto_incial*interes) + monto_incial), 3)
ano2 = round(((ano1*interes) + ano1), 3)
ano3 = round(((ano2*interes) + ano2), 3)

print(f'Año 1 = {ano1}')
print(f'Año 2 = {ano2}')
print(f'Año 3 = {ano3}')

