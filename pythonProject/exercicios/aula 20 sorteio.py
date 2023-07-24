from time import sleep
import random

sorteio = []


def sorte():
    print("Soretando os novos números")
    for ran in range(0, 5):
        sorteado = random.randint(0, 10)
        sorteio.append(sorteado)
        print(sorteado, end=" ")
        sleep(1)


def soma():
    som = 0
    for n in sorteio:
        if n % 2 == 0:
            som += n
    print()
    print(f"A soma de todos os números parés são {som}")


sorte()

soma()
