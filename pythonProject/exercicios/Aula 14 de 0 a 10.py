import random
cont = 1
choise = int(input("Escolha um número de 0 a 10 para iniciarmos o jogo\n"))
enimy = random.randint(0, 10)
while choise != enimy:
    print(f"Você errou, nâo desista, os maiores campeões jogam ate vencer\n o bot escolheu {enimy}, você escolh"
          f"eu {choise}")
    choise = int(input("Escolha um número de 0 a 10 para iniciarmos o jogo\n"))
    enimy = random.randint(0, 10)
    cont += 1
print(f"\033[33mParabéns, você ganhou!!!!\nVocê escolheu {choise} e o bot escolheu {enimy}. Depois de "
      f"{cont} tentativas você acertou\033[m")