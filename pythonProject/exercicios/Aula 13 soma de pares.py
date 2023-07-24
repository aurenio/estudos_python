soma = 0
for c in range(0, 6):
    quest = int(input("Digite um valor: "))
    if quest % 2 == 0:
        soma += quest
print(soma)
