nota1 = float(input("Qual foi a primeira nota do aluno?\n"))
nota2 = float(input("Qual foi a segunda nota do seu aluno?\n"))
media = (nota1 + nota2) / 2
if media < 5:
    print(f"\033[31m Sua media foi muito baixa, você foi reprovado, sua nota foi {media}")
elif media >= 5 and media < 7:
    print(f"\033[33mSua nota foi boa, você não reprovou porém ficou de recuperação, sua nota foi {media}")
elif media > 7:
    print(f"\033[32mSua nota foi muito boa, você passou, sua nota foi {media}")