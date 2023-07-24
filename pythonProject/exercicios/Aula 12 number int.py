numberone=int(input("Qual é o primeiro número de sua escolha?\n"))
numbertwo=int(input("Qual é o segundo número de sua escolha?\n"))
if numberone > numbertwo:
    print(f"O primeiro número que você colocou, {numberone} é maior que o segundo, {numbertwo}")
elif numbertwo > numberone:
    print(f"O segundo número, {numbertwo}, é maior que o primeiro, {numberone}")
elif numbertwo == numberone:
    print (f"O primeiro número, {numberone}, é igual ao segundo, {numbertwo}")
else:
    print("Algo deu errado")