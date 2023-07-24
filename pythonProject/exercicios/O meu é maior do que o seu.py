a = float(input("Qual é o primeiro número? "))
b = float(input("Qual é o segundo número? "))
c = float(input("Qual é o terceiro número? "))
maior = a
if (b > c) and (b > a):
    maior = b
if (c > a) and (c > b):
    maior = c
print(f"O maior número é: {maior}")
# ///////////////////
menor = a
if (b < c) and (b < a):
    menor = b
if (c < a) and (c < b):
    menor = c
print(f"O menor número é: {menor}")
