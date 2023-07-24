primov = 0
primo = int(input("Digite um número inteiro;\n"))
for tio in range(2, primo):
    if primo % tio == 0:
        primov += 1
if primov == 0:
    print("Seu número é primo")
else:
    print("seu número n é primo")