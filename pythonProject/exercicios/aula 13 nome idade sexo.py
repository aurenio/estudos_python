om, nameom = 0, "---"
date, dateom, wy = 0, 0, 0
nome = "---"
mediaacumulada = 0
sexo = "---"
for info in range(1, 5):
    print(f"{'-=' * 5} {info}ª Pessoa {'-+' * 5}" )
    name = str(input("Qual é o seu nome? "))
    date = int(input("Qual é sua idade? "))
    sexo = int(input("Qual é o seu sexo\n[1]Homem [2]Mulher [3]Outro\n"))
    mediaacumulada += date
    if sexo == 1 and date > dateom:
        dateom = date
        nameom = name
        om = date
    if sexo == 2 and date < 20:
        wy += 1
mediatotal = mediaacumulada / 4
print(f"A média de idade foi {mediatotal} anos")
print(f"O homem mais velho é {nameom} com a idade de {om} anos")
print(f"A quantidade de mulheres com menos de 20 são {wy}")