import random
aposta = []
app = []
cont = 0
jogos = int(input("Quantos jogos você vai apostar? "))
for j in range(0, jogos):
    while True:
        add = random.randint(0, 60)
        while add not in aposta:
            aposta.append(add)
            cont += 1
        if cont >= 6:
            cont = 0
            app.append(sorted(aposta[:]))
            aposta.clear()
            break
for p in app:
    print(f"Os números apostados são {p}")