import random


def c():
    print("\033[35mVamos jogar jokenpo!! escolha entre pedra, papel ou tesoura\033[m")
    choice = str(input("O que você vai jogar? \n")).lower().strip()
    jogo = ["pedra", "papel", "tesoura"]
    bot = random.choice(jogo)
    if "papel" in bot and "tesoura" in choice or "pedra" in bot and "papel" in choice or "tesoura" in bot and "pedra" in choice:
        print(f"Parabêns, você ganhou o jogo {name}, você jogou {choice} e o bot {bot}")
    elif "papel" in bot and "papel" in choice or "pedra" in bot and "pedra" in choice or "tesoura" in bot and "tesoura" in choice:
        print(f"O jogo empatou {name}, você jogou {choice} e o bot {bot}")
    elif "papel" in bot and "pedra" in choice or "pedra" in bot and "tesoura" in choice or "tesoura" in bot and "papel" in choice:
        print(f"Você acaba de perder o jogo {name}, você jogou {choice} e o bot {bot}")
    else:
        print("Sua opção não é válida")


name = str(input("Qual o seu nome? \n"))
c()
while True:
    try:
        quest = int(input("Você vai querer continuar jogando?\n [1]Sim [2]Não\n"))
        if quest == 1:
            print("\033[34mVamos continuar a nos divertir\033[m")
            c()
        elif quest == 2:
            break
        else:
            print("Essa opção não existe")
    except ValueError:
        print("Essa opção não existe")
print("Foi muito bom jogar com você")
