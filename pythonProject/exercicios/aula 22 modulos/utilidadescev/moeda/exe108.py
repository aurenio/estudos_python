def moeda(n):
    return f"R${n}"


def metade(n=1):
    resp = n / 2
    return (resp)


def dobro(n=0):
    resp = n + n
    return resp


def aumentar(porct=0, n=0):
    cal = (porct * n) / 100
    resp = n + cal
    return resp


def diminuir(porct=0, n=0):
    cal = (porct * n) / 100
    resp = n - cal
    return resp