produtos = ("pão", 2.00, "leite", 4.00, "coxinha", 6.00, "manteiga", 7.00)
print("=" * 30)
print("Lista de produtos e preços")
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f"{produtos[item]:.<30}", end="")
    else:
        print(f"R$ {produtos[item]:>2}")