pizza_veggie = "Pimiento y Tofu"
pizza_carnivora = "Peperoni, Jamon y Salmon"
Base_pizza = "Mozarella y Tomante"

pizza_deliveri = input((f'Que pizza quieres? Vegetariana con {pizza_veggie} o Carnivora con {pizza_carnivora} : '))
if pizza_deliveri =="Vegetariana":
    print(f'Tu pizza es Vegetaria y tendra los siguientes ingredientes: {Base_pizza}, {pizza_veggie}')
elif pizza_deliveri == "Carnivora":
        print(f'Tu pizza es Carnivora y tendra los siguientes ingredientes: Base {Base_pizza},  {pizza_carnivora}')
else:
    print("Ingresa una pizza valida y recuerda las mayusculas")
