banco = []
while True:
    valor = int(input("Digite um valor\n"))
    banco.append(valor)
    sn = input("Deseja continuar?\n")[0]
    while sn not in "sSnN":
        sn = input("Deseja continuar? coloque s ou n\n")
    if sn in "nN":
        break
    elif sn in "sS":
        print("Digite um novo valor")
banco.sort(reverse=True)
print(f"A quantidade de números digitado foi {len(banco)}, Em descrecente os valores ficam: {banco}")
if 5 in banco:
    print("Existe o número 5")
else:
    print("Não existe o número 5")

