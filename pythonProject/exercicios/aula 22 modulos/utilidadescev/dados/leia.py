def dinheiro(digit="Coloque um valor\n"):
    while True:
        n = str(input(digit))
        veria = n.replace(",", "")
        veri = veria.replace(".", "")
        if "," in n:
            n = n.replace(",", ".")
        if n.strip == "":
            print('ERRP, "" não é um valor')
        if not veri.isnumeric():
            print(f"Erro {veri} não é um valor")
        else:
            return n
