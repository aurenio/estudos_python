sort = []
for num in range(0,5):
    variavel= int(input("Digite um valor\n"))
    if num == 0 or variavel > sort[len(sort)-1]:
        sort.append(variavel)
    else:
        pos = 0
        while pos < len(sort):
            if variavel <= sort[pos]:
                sort.insert(pos, variavel)
                print(f"Adicionado na posição {pos}")
                break
            pos += 1
print(f"Os números estão ordenados em {sort}")