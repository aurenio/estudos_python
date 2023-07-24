import datetime
date = datetime.datetime.now()
date = date.year
print(date)
year = int(input("Qual foi a data de seu nascimento? "))
if date - year < 18:
    print(f"você ainda é muito novo para se alistar, falta certa de {18-(date-year)} anos")
elif date - year == 18:
    print("Esse é o ano que você deve se alistar")
elif date - year > 18:
    print(f"Você ja passou do ano de alistamento!!!, está atrasado {(date-year)-18}")


#day
#month
#year
#30/08/2022