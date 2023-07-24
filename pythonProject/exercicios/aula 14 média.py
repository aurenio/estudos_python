maior, menor, cont, media = 0, 999999, 0, 0
while True:
    num = int(input('Digite um número\n'))
    cont += 1
    media += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    choice = int(input('Você quer continuar?\n[1] sim, [2]não\n'))
    if choice == 2:
        break
mediareal = media/cont
print(f'A média foi {mediareal}')
print(f'O maior número foi {maior} e o menor foi {menor}')