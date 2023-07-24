lista = []
cont = 0
for num in range(0,3):
    lista.append(input(f"lista 0, {cont}\n"))
    cont = cont + 1
cont = 0
for num in range(0,3):
    lista.append(input(f"lista 1, {cont}\n"))
cont = 0
for num in range(0,3):
    lista.append(input(f"lista 2, {cont}\n"))
lista = [lista[0:3], lista[3:6], lista[6:9]]
print(f'''
{lista[0][0]} {lista[0][1]} {lista[0][2]}
{lista[1][0]} {lista[1][1]} {lista[1][2]}
{lista[2][0]} {lista[2][1]} {lista[0][2]}''')