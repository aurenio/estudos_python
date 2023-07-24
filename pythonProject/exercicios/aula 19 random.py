import random
game = {}
cont = 1
while cont <= 4:
    play = int(random.randint(1,6))
    game[f'jogador {cont}'] = play
    cont += 1

jogadores = sorted(list(zip(game.values(), game.keys())), reverse= True)

for i in enumerate(jogadores):
    print(f'O {i[1][1]} ficou na posição {i[0]+1} com {i[1][0]} no dado')