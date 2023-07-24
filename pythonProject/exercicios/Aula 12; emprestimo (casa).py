print("Hello World")
house = float(input("Qual é o valor da casa que você vai comprar ?\n"))
wage = float(input("Qual é o seu salário ?\n"))
month = float(input("Em quanto meses você quer quitar a divida ?\n"))
value = (wage * 30) / 100
price = house / (month * 12)
print(value)
print(price)
if price >= value:
    print("Infelizmente sua proposta nâo é concistente, teremos que recusar o pedido")
else:
    print("vai la comprar vai")

