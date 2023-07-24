a=int(input("Digite um ano para ver se ele é bixesto "))
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print("Seu numero é bixesto pow, parabens")
else:
    print("Seu ano não é bixesto :(")