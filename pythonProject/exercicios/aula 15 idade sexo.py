idade = man = mu = old = 0
while True:
    print(f"{'FORMULARIO':-^20}")
    idade = int(input('Qual a sua idade?\n '))
    sexo = str(input('Qual o seu sexo? \n[m]Masculino [f]Feminino\n '))[0].strip().upper()
    while sexo not in 'FM':
        sexo = str(input('Qual o seu sexo? \n[m]Masculino [f]Feminino\n '))[0].strip().upper()
    quest = str(input('Quer continuar?\n[sim] [não]\n '))[0].strip().upper()
    while quest not in 'SN':
        quest = str(input('Quer continuar?\n[sim] [não]\n '))[0].strip().upper()
    if idade > 18:
        old += 1
    if sexo in 'M':
        man += 1
    if sexo in 'F' and idade < 20:
        mu += 1
    if 'N' in quest:
        break
print(f'Tem {old} pessoas com mais de 18, {man} homens foram cadastrados e {mu} mulheres com menos de 20 anos foram '
      f'cadastradas')
print(f"{'Fim':-^20}")
