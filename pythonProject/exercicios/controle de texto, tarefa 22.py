a = str(input("Digite o seu nome completo: ")).strip()
print(f"Seu nome é : {a}")
print(f"Seu nome em maisculo é: {a.upper()}")
print(f"Seu nome em minusculo é {a.lower()}")
print(f"A quantidade de letras em seu nome: {len(' '.join(a).split())}")
b = a.split()[0]
print(f"O seu primeiro nome é {b} e tem essa quantidade de letras: {len(' '.join(b).split())}")
c = int(input("Digite qualquer numero de 0 a 9999 em quatro  ou não, a vida é tua: "))
u = c // 1 % 10
d = c // 10 % 10
ce = c // 100 % 10
m= c // 1000 % 10
print(f"Sua unidade é {u}\n sua dezena é {d}\n sua centena é {c}\n sua milhar é {m}")
