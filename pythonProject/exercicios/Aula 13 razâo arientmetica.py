first = int(input("Qual é o primeiro termo de sua escolha?\n"))
reason = int(input("Qual é a razão de sua escolha? \n"))
second = first + (10 * reason)
for pa in range(first, second, reason):
    print(pa)