sexo = str(input("Qual é o seu sexo? \n[F] para feminino [M] para masculino\n ")).upper()
while "M" != sexo != "F":
    sexo = str(input("Qual é o seu sexo?\nFaz direito parça\n [F] para feminino [M] para masculino\n")).upper()
if sexo == "F":
    print("Então você é uma garota")
else:
    print("Então você é um cara")
