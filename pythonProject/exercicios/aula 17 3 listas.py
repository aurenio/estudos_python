bone = []
while True:
    one = int(input("Digite uma valor: "))
    sn = str(input("Deseja continuar? "))[0]
    bone.append(one)
    print(bone)
    two = [par for par in bone if par % 2 == 0]
    three = [impar for impar in bone if impar % 2 != 0]
    while sn not in "snSN":
        sn = str(input("Deseja continuar? Digite s ou n\n"))[0]
    if sn in "nN":
        break
print(f"A lista completa é {bone}, os pares dela são {two} e os impares são {three}")