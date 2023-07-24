banco = list("")
while True:
    valor = [input("Digite um valor:\n")]
    if valor not in banco:
        banco.append(valor)
        print("Valor adicionado com sucesso")
    else:
        print("Valor duplicado, então ele não vai ser adicionado")
    sn = str(input("Deseja continuar?\n")).lower()[0]
    if sn not in "sn":
        while sn not in "sn":
            sn = str(input("Digite um valor válido\n")).lower()[0]
    if sn in "n":
        break
    elif sn in "s":
        print("Se lembre que valores repetidos não são adicionados")
print(f"Os valores válidos que você adicionou em ordem crescente foi {sorted(banco)}")