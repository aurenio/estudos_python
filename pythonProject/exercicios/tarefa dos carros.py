print("NÃO ULTRAPASSE 80 KM/H SE NÃO VAI SER MUTADO");
a = float(input("Quantos km o seu carro está ? \n > "));
if a >= 81 :
    print(f"Você recebeu uma multa de {(a-80)*7 } R$, eu avisei ");
else :
    print("Continue respeitando a lei uwu");