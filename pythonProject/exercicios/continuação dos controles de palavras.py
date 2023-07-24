a = str(input("Digite o nome de uma cidade: ")).strip()
b = a.split()[0].lower()
if b == "santo":
    print("O seu pais tem santo no nome inicial")
else:
   print("O seu pais não tem santo no nome inicial")
c = str(input("Digite o seu nome completo ")).strip().lower()
c = c.split()
if "silva" in c :
    print("O seu nome tem silva")
else:
    print("seu nome não tem silva")