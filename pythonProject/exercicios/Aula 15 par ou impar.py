import random
win = 0
while True:
    robot = random.randint(0, 10)
    num = int(input('Digite um número para iniciarmos o jogo\n'))
    escolha = str(input('Prefere par ou impar? ')).strip().upper()[0]
    soma = robot + num
    print(escolha)
    if escolha == 'I':
        if soma % 2 != 0:
            print(f'Você ganhou parabens, você jogou {num} e escolheu impar, o robô escolheu par e jogo {robot}')
            win += 1
        else:
            print(f'Você perdeu :(, você jogou {num} e escolheu impar, o robô escolheu par e jogo {robot}')
            break
    elif escolha == 'P':
        if soma % 2 == 0:
            print(f'Você ganhou, parabéns!!, você jogou par e escolheu {num} e o robô impar e jogou {robot} ')
            win += 1
        else:
            print(f'Você perdeu :(, você jogou par e escolheu {num} e o robô impar e jogou {robot}')
            break
    else:
        print(f'Opçâo invalida, tente novamente')
        break
print(f'Bom jogo :D, você ganhou {win} vezes')
