jogador = {}
gol = []
soma = 0
mal=0
jogador['nome'] = input("Qual o nome do jogador?\n")
jogador['total'] = int(input("Qual foi o total de partidas dele?\n"))

for f in range(1, jogador['total']+1):
    futebolista = int(input(f"Quantos gols ele fez na {f}º partida?\n"))
    gol.append(futebolista)
    mal += futebolista
jogador['maxgols']= mal
jogador['gols'] = gol[:]
print("=-"*20)
print(jogador)
print("-=" * 20)
print(f"O nome do jogador é {jogador['nome']}\n"
      f"jogou um total de {jogador['total']} partidas\n"
      f"Fez {jogador['gols']} gols")
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {jogador["total"]} partidas\n')
for f in range(1, jogador['total'] + 1):
    print(f'Na {f}º partida ele fez {jogador["gols"][f-1]} gol')
    soma += int(jogador["gols"][f-1])
print(f"Um total de {soma} gols ;D")
