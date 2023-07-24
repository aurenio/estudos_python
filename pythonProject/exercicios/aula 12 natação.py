import datetime
year = int(input("Qual ano você nasceu ? \n"))
date= datetime.datetime.now().year
if date - year <= 9:
    print(f"\033[35mVocê se encaixa na categoria mirim")
elif date - year <= 14 and date - year > 9 :
    print(f"\033[34mVocê se encaixa na categoria infatil")
elif date - year > 14 and date - year <= 19:
    print(f"\033[33mVocê se encaixa na categoria junior")
elif date - year > 19 and date - year <= 20:
    print(f"\033[31mVocê se encaixa na categoria senior")
elif date - year > 20 :
    print(f"\033[30mVocê se encaixa na categoria master")




