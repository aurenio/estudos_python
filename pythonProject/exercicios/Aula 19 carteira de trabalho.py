import datetime
funcionario = {}
ano = datetime.datetime.now().year
funcionario['nome'] = input("Qual é o seu nome ?\n")
funcionario['idade'] = int(input('Quando você nasceu?\n'))
funcionario['carteira de trabalho'] = input("Qual a sua carteira de trabalho?(caso não tenha, digite 0)\n")
if int(funcionario['carteira de trabalho']) == 0:
    print(f'O nome do funcionário é {funcionario["nome"]}\n'
          f'Com {ano - funcionario["idade"]} anos de idade\n'
          f'E com o valor {funcionario["carteira de trabalho"]} na carteira de trabalho\n')
else:
    funcionario['contratacao'] = int(input("Qual o seu ano de contratação?\n"))
    funcionario['salario'] = int(input("Qual o seu sálario?\n"))
    print(f'O nome do funcionário é {funcionario["nome"]}\n'
          f'Com {ano - funcionario["idade"]} anos de idade\n'
          f'E com o valor {funcionario["carteira de trabalho"]} na carteira de trabalho\n'
          f'Foi contratano no ano {funcionario["contratacao"]}\n'
          f'Com um salario de {funcionario["salario"]} reais\n'
          f'E você vai se aposentar em {30 - (ano - funcionario["contratacao"])} anos'
          f'E você vai se aposentar com {(ano - funcionario["idade"]) + (30 - (ano - funcionario["contratacao"]))}')


