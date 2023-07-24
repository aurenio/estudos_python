while True:
    num = float(input("Escolha 1 número\n"))
    num2 = float(input("Escolha outro número\n"))
    choice = 0
    while choice != 5:
        choice = int(input("O que você quer fazer?\n[1]somar\n[2]múltiplicar\n[3]maior\n[4]novos números\n[5]sair do "
                           "programa\n"))
        if choice == 1:
            soma = num + num2
            print(f"A soma de seus números foi {soma}")
        elif choice == 2:
            mult = num * num2
            print(f"Sua multiplicação deu {mult}")
        elif choice == 3:
            if num > num2:
                print(f"O primeiro número, {num}, é maior que o segundo, {num2}")
            elif num == num2:
                print(f"O {num2} e o {num} são iguais")
            else:
                print(f"O segundo número. {num2} é maior que o primeiro, {num}")
        elif choice == 4:
            break
        elif choice == 5:
            print('Foi bom enquanto durou, até mais')
        else:
            print('Opção errada, tente novamente')

