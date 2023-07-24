pessoas = list()
banco = []
namex = list()
namem = list()
while True:
    pessoas.append(str(input("Digite o nome do Cliente? ")))
    pessoas.append(int(input("Digite a sua idade? ")))
    sn = str(input("Deseja continuar? "))[0].lower()
    banco.append(pessoas[:])
    pessoas.clear()
    while sn not in "sn":
        sn = str(input("Deseja continuar? Digite s para sim ou n para não"))[0].lower()
    if sn in "n":
        print("Processando dados")
        break
minimo = min(banco)
maximo = max(banco)
for p in banco:
    if p[1] == maximo[1]:
        namex.append(p[0])
    if p[1] == minimo[1]:
        namem.append(p[0])

print(f"O cliente que tem mais idade é o {namex} com {maximo[1]} enquanto o que tem menos é {namem} com {minimo[1]}")
print(f"O número de pessoas que foram entrevistada foi: {len(banco)}")