resp = ''
num1 = float(input("Digite o primeiro termo\n"))
reason = float(input("Digite a razão\n"))
pa = num1 + (reason * 10)
while num1 != pa:
    print(f"{num1:.0f}", end='')
    num1 = num1 + reason
    print('-' if num1 != pa else ' Fim', end='')


