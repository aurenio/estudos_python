def hp():
    while True:
        print("\033[42m-"*(len("SISTEMA DE AJUDA PYHELP") + 4))
        print("  SISTEMA DE AJUDA PYHELP")
        print("-" * (len("SISTEMA DE AJUDA PYHELP") + 4))
        print("\033[m")

        a = input("Qual a variavel da biblioteca? \n")
        if a == "fim":
            print("\033[41m-" * (len(f"Ate logo") + 4))
            print(f"  Ate logo")
            print("-" * (len(f"Ate logo") + 4))
            print("\033[m")
            break

        print("\033[44m-" * (len(f"Acessando o manual do {a}") + 4))
        print(f"  Acessando o manual do {a}")
        print("-" * (len(f"Acessando o manual do {a}") + 4))
        print("\033[m")

        print("\033[47m")
        help(a)
        print(f"\033[m")


hp()