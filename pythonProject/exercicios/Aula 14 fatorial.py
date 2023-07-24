fat = int(input("Escolha um número para iniciarmos a fatorial:\n"))
c = fat
f = 1
while c > 0:
    print(f'{c}', end='')
    print(f'x' if c > 1 else '=', end='')
    f *= c
    c -= 1
print(f" O fatorial do seu número {fat} deu {f}")