def num(numb):
    print("=-" * 10)
    print(f"O maior número é o {max(numb)}")
    print("=-" * 10)


pacote = []
while True:
    info = input("quer continuar?[s/n]\n")[0]
    if info in "nN":
        break
    pacote.append(int((input("Digite um número\n"))))
num(numb=pacote)
