import moeda

num = float(input("Digite um número\n"))
porc = float(input("Digite uma porcentagem\n"))
print(f"O dobro do número {num} é {moeda.dobro(num)}"
      f"\nA metade é {moeda.metade(num)}"
      f"\nAumentando o {num} em {porc}% vai dar {moeda.aumentar(porc,num)}"
      f"\nDiminuindo o {num} em {porc}% vai dar {moeda.diminuir(porc,num)}")