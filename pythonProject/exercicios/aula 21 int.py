def leiaint(m):
    while True:
        numb = input(f"{m}\n")
        if numb.strip() == "":
            print("\033[31m erro, espaçamento")
        if not numb.isdigit():
            print("\033[31m Digite apenas números\033[m")
        if numb.isdigit():
            print(f"O seu número é o número {numb}")
            break

leiaint("Digite algo ")
