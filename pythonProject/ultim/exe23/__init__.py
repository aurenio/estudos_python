def menu():
    print("-" * 20)
    print("menu".center(20))
    print("-" * 20)
    print("1 - ver pessoas cadastradas")
    print("2 - Cadastrar novas pessoas")
    print("3 - sair do sistema")
    print("-" * 20)


def escolha():
    while True:
        try:
            esc = input("Digite sua escolha\n")
        except Exception as erro:
            print(erro)
            esc = input("Digite sua escolha\n")
        if esc in "123":
            return esc

def analise(n="0"):
    if n == "1":
        with open("menu", "r") as txt:
            info = txt.read()
            print("="*20)
            print("PESSOAS CADASTRADAS".center(20) )
            print(info)
            print("=" * 20)
    if n == "2":
        mns = [input("Quem você quer cadastrar?\n"), input("Digite sua idade\n")]
        with open("menu", "+a") as txt:
            txt.write(f"{mns[0]} ----------- {mns[1]}\n")
    if n == "3":
        print("Até logo")
        return False