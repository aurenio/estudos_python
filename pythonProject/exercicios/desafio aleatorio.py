from random import randint

b = int(input("Digite uma letra de 0 a 5, caso acerte um numero, você vai ganhar um parabens :D "));
a = randint(0, 5);
print(f"O numero sorteado foi {a}");
print(f"seu numero foi {b}");
if (a == b) :
    print("Parabens garaio");
else:
    print("Ado ado ado você errou e é abobaiado");
