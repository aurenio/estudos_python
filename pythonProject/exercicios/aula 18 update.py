lista = []
cont = 0
for num in range(0,3):
    lista.append(input(f"lista 0, {cont}\n"))
    cont = cont + 1
cont = 0
for num in range(0,3):
    lista.append(input(f"lista 1, {cont}\n"))
    cont = cont + 1
cont = 0
for num in range(0,3):
    lista.append(input(f"lista 2, {cont}\n"))
    cont = cont + 1
lista = [lista[0:3], lista[3:6], lista[6:9]]
print(f'''
{lista[0][0]} {lista[0][1]} {lista[0][2]}
{lista[1][0]} {lista[1][1]} {lista[1][2]}
{lista[2][0]} {lista[2][1]} {lista[0][2]}''')
cont = 0
soma2 = 0
som = 0
pa = [ par for par in lista[0] + lista[1] + lista [2] if int(par) % 2 == 0]
for num in pa:
    som += int(num)
for add in lista[2]:
    soma2 += int(add)
print(f"A soma de todos os valores digitados pares são {som}\nA soma dos valores da terceira coluna é {soma2}"
      f" e o maior número da segunda linha é {max(lista[1])}")