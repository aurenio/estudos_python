import datetime
contador = 0
date=datetime.datetime.now()
for nome in range(0,7):
    name = str(input("Qual seu nome? "))
    year = int(input("Que ano você nasceu? "))
    if date.year - year < 21:
        print(f"você ainda é menor de idade {name}, você tem `{date.year - year} anos. ")
        contador += 1
    else:
        print(f"Você é maior de idade {name}, com {date.year - year} anos.")
print(f"Das 7 pessoas {contador} tem menos de 21 e {7 - contador} tem mais de 21")