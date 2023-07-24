import exe108

num = float(input("Digite um número\n"))
porc = float(input("Digite uma porcentagem\n"))
print(f"O dobro de {exe108.moeda(exe108.moeda(num))} é {exe108.moeda(exe108.dobro(num))}"
      f"\nA metade é {exe108.moeda(exe108.metade(num))}"
      f"\nAumentando {exe108.moeda(num)} em {porc}% vai dar {exe108.moeda(exe108.aumentar(porc,num))}"
      f"\nDiminuindo {exe108.moeda(num)} em {porc}% vai dar {exe108.moeda(exe108.diminuir(porc,num))}")