num = 0
cont2 = 0
cont = int(input('Coloque um número inteiro\n'))
while cont != 999 :
    num += 1
    cont2 += cont
    cont = int(input('Coloque um número inteiro\n'))
print(f'A quantidade de números digitados foi:{num}\nE a soma deu {cont2} ')