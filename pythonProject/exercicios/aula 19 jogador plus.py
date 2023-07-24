jogador = {}
gol = []
ma = 0
mal = 0
cod = 0
while True:
    jogad= input("Qual o nome do jogador?\n")
    total = int(input("Qual foi o total de partidas dele?\n"))

    for f in range(1, total+1):
        gol.append(int(input(f"Quantos gols o {jogad} fez na {f}º partida?\n")))
    jogador[f"{jogad}"] = gol[:]
    gol.clear()
    info = input('quer continuar [s]/[n]?\n')[0]
    while info not in 'sn':
        info = input('quer continuar [s]/[n]?\n')[0].lower()
    if info in 'n':
        break
print("-="*20)
print(f"cod     jogador        gols         total")
for jg in jogador:
    for m in jogador[jg]:
        ma += m
    print(f'{cod:^5}    {jg:^5}-       -{jogador[jg]}-      -{ma:^5}')
    ma = 0
    cod += 1
while True:
    esc = int(input('Qual jogador você quer analisar?\n'))
    if esc == 999:
        break
    while esc > cod:
        esc = int(input('jogador não encontrado\nQual jogador você quer analisar?\n'))
    for p in enumerate(jogador):
        if int(p[0]) == esc:
            print(f'Iniciando o processo do jogador {esc}')
            for f in range(1, len(jogador[f'{p[1]}']) + 1):
                print(f'Na {f}º partida o {p[1]} fez {int(jogador[p[1]][f-1])} gol')
                ma += 1
