peso_payasos = 112
peso_munecas = 75
n_payasos = int(input("Cuantos payasos llevas?: "))
n_munecas = int(input("Cuantas Muñecas llevas?: "))

peso_paquete = ((peso_payasos*n_payasos)+(n_munecas*peso_munecas))
print(f'El peso de tu paquete para enviar es:{peso_paquete} gramos ')

