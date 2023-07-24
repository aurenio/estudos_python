banco = [input("Digite o 1ª valor\n"),input("Digite o 2ª valor\n"),input("Digite o 3ª valor\n"),input
("Digite o 4ª valor\n"),input("Digite o 5ª valor\n")]
banco2 = banco[:]
banco3 = banco[:]
print("=-" * 20)
print(f"Os valores são {banco})")
print("=-" * 20)
max = max(banco)
idxa = [banco.index(max) + 1]
min = min(banco)
idxi = [banco.index(min) + 1]
cont = 0
while True:
    bancotest = int(banco[cont])
    max2 = banco2.count(max)
    min2 = banco3.count(min)
    cont += 1
    if max2 > 1:
        banco2.remove(max)
        add = banco2.index(max) + cont + 1
        idxa.append(add)
    if min2 > 1:
        banco3.remove(min)
        addm = banco3.index(min) + cont + 1
        idxi.append(addm)
    if cont >= 5:
        break
print(f"O maior número é o {max} e se encontra na posição {idxa} e o menor é o {min} se encontra na posiçâo {idxi} ")