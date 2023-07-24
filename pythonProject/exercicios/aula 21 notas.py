


def notas(*nt, sit=True):
    """
    função para analisar as notas e a situação de vários alunos
    :param nt:Recebe as notas dos alunos
    :param sit:sit=False vai mostrar a situação da média dos alunos
    :return:Um dicionário com a situação da turma
    """
    alunos = {}
    media = 0
    alunos["quantidades"] = len(nt)
    alunos["maior"] = max(nt)
    alunos["min"] = min(nt)
    for num in nt:
        media += num
    alunos["media"] = media / alunos["quantidades"]

    if not sit:
        if 6 <= alunos["media"] <= 7:
            alunos["situação"] = "Razoável"
        elif alunos["media"] < 6:
            alunos["situação"] = "Ruim"
        else:
            alunos["situação"] = "MUITO BOA PARABENS"
    return alunos


print(notas(6, 6, 6))
help(notas)
