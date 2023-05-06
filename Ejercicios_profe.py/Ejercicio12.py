nombre =  input("Cual es tu nonmbre: ")
sexo =  input("Cual es tu sexo (M/F): ")

if sexo == "F" and nombre[0]> "M" and sexo == "M" and nombre[0]>"N":
    print("Grupo A")
else:
    print("Grupo B")
