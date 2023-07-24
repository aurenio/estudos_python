while True:
    cont = 0
    tab = int(input('Deseja ver a tabuada de qual número? Digite um número negativo para parar a operação\n'))
    if tab < 0:
        break
    print(f'Tabuada de {tab} ')
    while cont <= 10:
        print(f'{tab} x {cont} = {tab*cont}')
        cont += 1
print('Até a proxima :D')