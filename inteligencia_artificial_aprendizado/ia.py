from sklearn.svm import LinearSVC 
from sklearn.metrics import accuracy_score

#iniciando a classificacao, como por exemplo se pode ser um cachorro[0] ou porco [1] e fazer o programa aprender o que pode ser um porco ou um cachorro
#para iniciarmos precisamos dizer o que poderia ser um porco ou um cachorro ou uma compra ou nao com um conjutno de variaveis
#para esse exemplo vamos levantar as caracteristicas que com mais frequencia melhora o aprendizado como exemplo porco = pelo curto, perna curta, nao late
#porco vai ser 1 e cao vai ser 0, adicionando pocibilidades de erros para melhor adptacao a advercidade

porco_01 = [0,1,0]
porco_02 = [0,1,1] #adicionando possivel possibilidade imprevista
porco_03 = [1,1,0]

dog_01 = [0, 1, 1]
dog_02 = [1, 0, 1]
dog_03 = [1, 1, 1]

galinha = [0,0,0]

dados = [porco_01, porco_02, porco_03, dog_01, dog_02, dog_03, galinha]
#adicionando uma lista de dados
classes = [1, 1, 1, 0, 0, 0, 2]
#separando em classes
ia = LinearSVC()
#adicionando o modelo de inteligencia e apontando como ela tem que aprender
ia.fit(dados, classes)
#ajustando, colocando os dados na ia e qual a classe ja que e um aprendizado supervisionado

#testando o parametro com um animal desconhecido
animal_desconhecido = [0,0,0]
#animal desconhecido vai ser um cachorro
#pelo logo, perna longa e late

print(ia.predict([animal_desconhecido]))
#o programa tem que voltar o valor 0, variavel apotando que e um cao

#agora iremos fazer o algoritimo prever todas as variaveis desconhecidas
# cao 0, porco 1, cao 0
print('novo teste')
misterio_01 = [1, 1, 1]
misterio_02 = [1, 1, 0]
misterio_03 = [0, 1, 1]

teste = [misterio_01, misterio_02, misterio_03]

print(ia.predict(teste))

#vamos dizer agora que o algoritimo erro um das possibilidades e ficou com a taxa de 60% de acerto, vamos agora analisar as porcentagem
previsao = ia.predict(teste)
#adicionando valores verdadeiro
teste_classe = [0,1,1]
#vamos comparar agora 
print(previsao == teste_classe)
#vamos somar agora e pegar os corretos
previsao = (previsao == teste_classe).sum()
#pegaremos o total do teste
total = len(teste)
#verificar a taxa de acerto
acerto = previsao / total
print(acerto)

#utilizado a mesma ideia com a biblioteca sklearn.metrics
# Realizando previsões para o conjunto de dados de teste
previsoes = ia.predict(teste)

# Calculando a taxa de acerto do modelo em relação aos dados de teste
taxa_de_acerto = accuracy_score(teste_classe, previsoes)
print(taxa_de_acerto)  # Saída: 0.6666666666666666 (ou 66.67%)