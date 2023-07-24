lista = []
cont = 0
while True:
    request= str(input("Você deseja prosseguir com a aplicação?\n")) [0].lower()
    if request not in "sn":
        while request not in "sn":
            request = str(input("Você deseja continuar? Digite sim ou não\n"))[0].lower()
    if request in "n":
        break
    else:
        lista.append([str(input("Digite o nome do aluno\n")), input("digite a primeira nota\n"), input("digite a segunda nota\n")])
print(f"Escolha qual estudante você quer ver a média completa")
for media in range(0,len(lista)):
    print(f"{cont} para {lista[cont][0]} com media de {(int(lista[cont][1]) + int(lista[cont][2])) / 2}")
    cont += 1
while True:
    perso = int(input("Escolha um número:\n"))
    print(f"O {lista[perso][0]} teve a primeira nota {lista[perso][1]}, a segunda nota {lista[perso][2]} e a média de "
          f"{(int(lista[perso][1]) + int(lista[perso][2])) / 2}")
    request= input("Deseja continuar?\n")[0]
    while request not in "sn":
        request = input("Deseja continuar?\n")[0]
    if request in "n":
        break