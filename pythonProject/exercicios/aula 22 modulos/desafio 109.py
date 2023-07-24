import exe109
num = float(input("Digite um número\n"))
porc = float(input("Digite uma porcentagem\n"))
form = False
while True:
    info = input("Deseja formatar?\n")[0].lower()
    if info == "s":
        form = True
    if info in "sn":
        break
print(f"O dobro de {exe109.moeda(num,form)} é {exe109.dobro(num)}"
      f"\nA metade é {exe109.metade(num,form)}"
      f"\nAumentando o {exe109.moeda(num,form)} em {porc}% vai dar {exe109.aumentar(porc,num,form)}"
      f"\nDiminuindo o {exe109.moeda(num,form)} em {porc}% vai dar {exe109.diminuir(porc,num,form)}")