def fatorial(n, show=False):
    """
    Calcular o fatorial de um número

    :param n: Usado para indicar de qual número você quer a fatorial
    :param show: True caso você queira mostrar os calculos ou False/nada se não desejar mostra
    :return: o valor de um fatorial
    """
    som = 1
    cont = 0
    if not show:
        for numb in range(n, 0, -1):
            som *= numb
        return f"{som}"
    if show:
        for numb in range(n, 0, -1):
            print(numb, end="")
            if cont >= 0 and numb != 1:
                print("x", end="")
            som *= numb
            cont += 1
        return f"={som}"


while True:
    quest = input("Deseja que o calculo apareça [s/n]?\n")[0].lower()
    if quest in "sn":
        break
if quest == "s":
    quest = True
else:
    quest = False
p = int(input("Digite um número para fazer a fatorial\n"))
f = fatorial(p, show=quest)
print(f)
help(fatorial)
