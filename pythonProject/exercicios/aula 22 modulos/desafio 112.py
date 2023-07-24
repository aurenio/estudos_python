from utilidadescev import moeda
from utilidadescev import dados


num = dados.leia.dinheiro("Digite algo\n")
porcd = float(input("Digite uma porcentagem para diminuir\n"))
porca = float(input("Digite uma porcentagem para aumentar\n"))
form = False
while True:
    info = input("Deseja formatar?\n")[0].lower()
    if info == "s":
        form = True
    if info in "sn":
        break
moeda.exe110.resumo(num, aume=porca, dim=porcd, fo=form)



