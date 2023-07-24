
five = (int(input("Digite o primeiro número\n")), int(input("Digite o segundo número\n")),
       int(input("Digite o terceiro número\n")), int(input("Digite o quarto número\n")))
if 3 not in five:
    print("Não foi encontrado nenhum valor localizado de 3")
else:
    check = five.index(3)
    print(f"O primeiro 3 foi encontrado na posição { check + 1}")
print(f"Existe {five.count(9)} números 9 na tupla")
print(f"O maior número da tupla é {max(five)}")
print("Os seguntes números da tupla são pares: ", end = "" )
for item in five:
    if int(item) % 2 == 0:
        print(item, end=" ")

