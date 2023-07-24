def vol(*cont):
    cont = list(cont)
    print("contagem de 1 em 1 até 10")
    print("-=" * 10)
    for um in range(1, 11):
        print(um, end=" ")
    print()
    print("Contagem de 10 até 1 de 2 em 2")
    print("-=" * 10)
    for ten in range(10, -1, -2):
        print(ten, end=" ")
    print()
    print("-=" * 10)
    print(f"Contagem de {cont[0]} a {cont[1]} de {cont[2]} em {cont[2]}")
    if cont[2] == 0:
        if cont[0] < cont[1]:
            for esc in range(cont[0], cont[1] + 1):
                print(esc, end=" ")
        elif cont[0] > cont[1]:
            for esc in range(cont[0], cont[1] - 1, -1):
                print(esc, end=" ")
    else:
        if cont[2] <= -1:
            for esc in range(cont[0], cont[1] - 1, cont[2]):
                print(esc, end=" ")
        else:
            for esc in range(cont[0], cont[1] + 1, cont[2]):
                print(esc, end=" ")


vol(int(input("digite o inicio\n")), int(input("digite o fim\n")), int(input("Quais passos?\n")))
