import exe110
num = float(input("Digite um número\n"))
porcd = float(input("Digite uma porcentagem para diminuir\n"))
porca = float(input("Digite uma porcentagem para aumentar\n"))
form = False
while True:
    info = input("Deseja formatar?\n")[0].lower()
    if info == "s":
        form = True
    if info in "sn":
        break
exe110.resumo(num, aume=porca, dim=porcd, fo=form)
