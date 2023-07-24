lista = {}
feminino = []
idade = 0
while True:
    nome = input("Qual é o seu nome?\n")
    sexo = input("Qual o seu sexo? [M]/[F]\n")[0].lower()
    while sexo not in "fm":
        sexo = input("Qual o seu sexo? [M]/[F]\n")[0].lower()
    if sexo == 'f':
        feminino.append(nome)
    lista[f'{nome}'] = int(input("Qual sua idade\n"))
    info = input("Quer continuar? [S]/[N]\n")[0].lower()
    while info not in "sn":
        info = input("Quer continuar? [S]/[N]\n")[0].lower()
    if info == "n":
        break
print(lista)
for i in lista:
    idade += lista[i]
media = idade / len(lista)
print(f"O grupo tem {len(lista)} pessoas\n"
      f"A media de idade é {media}\n"
      f"E as garotas são {feminino}")
for p in lista:
    if lista[p] > media:
        print(f'{p} esta com a idade acima da media com {lista[p]} anos')