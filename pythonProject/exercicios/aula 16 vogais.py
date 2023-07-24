palavras = ("arroz", "praticar", "tatu", "trabalhar", "viver", "Esforço", "AeIoU")
for vogais in palavras:
    print(f"\nO {vogais}, tem as vogais: ", end="")
    vog = vogais.lower()
    for v in vog:
        if v in "aeiou":
            print(v, end="")