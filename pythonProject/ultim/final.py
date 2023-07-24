import exe23

a = True
while a:
    exe23.menu()
    resp = exe23.escolha()
    exe23.analise(resp)
    if resp == "3":
        break