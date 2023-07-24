boletim = {'aluno': str(input("Digite o nome do aluno\n")), 'nota1': int(input("Digite a primeira nota do aluno\n")),
           'nota2': int(input("Digite a segunda nota do Aluno\n"))}
if (boletim['nota1'] + boletim['nota2']) / 2 >= 7:
    boletim['situação'] = "aprovado"
else:
    boletim['situação'] = 'reprovado'
print(f"o {boletim['aluno']}, que tirou {boletim['nota1']} na primeira prova e {boletim['nota2']} na segunda prova"
      f" foi {boletim['situação']} com {(boletim['nota1'] + boletim['nota2']) / 2}")
