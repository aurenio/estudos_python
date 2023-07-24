valor20 = valor50 = valor1 = 0
print(f'{"Caixa eletronico":-^50}')
valor = int(input('Digite um valor a ser sacado\n'))
while valor > 1:
    valor50 = valor // 50
    valor1 = valor % 50
    if valor1 == 0:
        print(f'O senhor vai receber {valor50} de 50')
        break
    elif valor1 % 50 != 0:
        print(f'O senhor vai receber {valor50} de 50')
        valor20 = (valor - (valor50 * 50)) // 20
        if valor20 * 20 + valor50 * 50 == valor:
            print(f'O senhor vai receber {valor20} de 20')
            break
        else:
            if valor20 != 0:
                print(f'O senhor vai receber {valor20} de 20')
        valor10 = (valor - ((valor50 * 50) + (valor20 * 20))) // 10
        if valor10 * 10 + valor50 * 50 == valor:
            print(f'O senhor vai receber {valor10} de 10')
            break
        else:
            if valor10 != 0:
                print(f'O senhor vai receber {valor10} de 10')
        valor1 = (valor - ((valor50 * 50) + (valor20 * 20) + (valor10 * 10)))
        if valor1 + valor20 * 20 + valor50 * 50 + valor10 * 10 == valor:
            print(f'O senhor vai receber {valor1} de 1')
            break
        else:
            print(f'Algo deu errado {valor1} {valor10} {valor20} {valor50} {valor}')
            break
print(f'{"FIM":=^50}')
