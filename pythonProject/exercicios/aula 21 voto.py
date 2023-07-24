import datetime


def voto(m=2000):
    ano = datetime.datetime.now().year
    idade = ano - m
    if 18 < idade < 65:
        return f"com {idade} o voto é obrigatorio"
    elif idade < 18:
        return f"Com {idade} o voto não é obrigatorio"
    else:
        return f"Com {idade} o voto é opcional"


vt = int(input("Digite o ano de seu nascimento para analisarmos seu estado de voto\n"))
print(voto(vt))
