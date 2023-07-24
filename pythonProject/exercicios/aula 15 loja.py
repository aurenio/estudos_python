print('-='*20)
print('Loja de produtos')
print('-='*20)
pre = cont = menos = 0
while True:
    nome = str(input('Nome do produto\n'))
    money = float(input('Preço do produto\n'))
    pre += money
    if money > 1000:
        cont += 1
    if money == 0:
        print('Opção invalida, tente novamente')
        while money == 0:
            money = float(input('Preço do produto\n'))
    if menos == 0 or menos > money:
        prb = nome
        menos = money
    quest = str(input('Quer continuar?\n[s] para sim [n] para não\n'))[0].strip().upper()
    if quest == 'N':
        break
    while quest not in "SN":
        quest = str(input('Quer continuar?\n[s] para sim [n] para não\n'))[0].strip().upper()
    if quest == 'N':
        break
    else:
        print('Escolha os seus produtos: ')

print(f'O total de gasto é {pre}\nExistem {cont} produto que são mais de 1000\nO nome do produto mais barato'
    f' é {prb} no valor de {menos}')