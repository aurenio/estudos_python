def funcao(nome="<Desconhecido>", gols=0):
    print(f"O jogador {nome}, fez {gols}")


n = input("Digite o nome do jogador\n")
g = input(f"Digite a quantidade de gols que o {n} fez\n")
if n.strip() == "":
    n = "<Desconhecido>"
if not g.isnumeric():
    g = 0
else:
    g = int(g)
funcao(n, g)
