
peso = int(input ("Cual es tu peso?: "))

comidas_60_70 = {
    "desayuno":"Pan con queso",
    "snack1" :"Papa",
    "almuerzo" : "Fideos con Salsa",
    "snack2": "Pan con jamon",
    "cena": "arroz con pan",
}
menu:[
    "desayuno":"Platano con avena",
    "almuerzo" : "Carne con verduras y porotos",
    "snack2": "fruta y te",
    "cena": "Pollo con carne y ensalada",
]

comidas_mayor_80 = {
    "desayuno":"Avena con suplemento de fibra",
    "almuerzo" : "Sopa de suplemento de fibra",
    "cena": "Pan con fibra",
}

if peso >= 60 and peso <=70:
    print(f'Tu dieta consiste en : {comidas_60_70}')
elif peso >=70 and peso <=80:
    print(f'Tu dieta consiste en : {comidas_70_80}')
elif peso > 80:
    print(f'Tu dieta consiste en : {comidas_mayor_80}')
