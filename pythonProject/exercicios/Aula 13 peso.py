namemaior, namemenor = "---", "---"
kgmaior, kgmenor = 0, 9999999
for peso in range(0, 5):
    name = str(input("Qual é o seu nome? "))
    kg = float(input("Qual é o seu peso? "))
    if kg < kgmenor :
        namemenor = name
        kgmenor = kg
    if kg > kgmaior:
        namemaior = name
        kgmaior = kg
print(f"O {namemaior} é o mais pesado, com {kgmaior} kg")
print(f"O {namemenor} é o menos pesado, com {kgmenor} kg")