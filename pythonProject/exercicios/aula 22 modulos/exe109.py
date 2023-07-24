def moeda(n, valor=False):
    if valor:
        n = f"R${n}"
    return f"{n}"


def metade(n=1, valor=False):
    resp = n / 2
    if valor:
        resp = f"R${resp}"
    return resp


def dobro(n=0, valor=False):
    resp = n + n
    if valor:
        resp = f"R${resp}"
    return resp


def aumentar(porct=0, n=0, valor=False):
    cal = (porct * n) / 100
    resp = n + cal
    if valor:
        resp = f"R${resp}"
    return resp


def diminuir(porct=0, n=0, valor=False):
    cal = (porct * n) / 100
    resp = n - cal
    if valor:
        resp = f"R${resp}"
    return resp

