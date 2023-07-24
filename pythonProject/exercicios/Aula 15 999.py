soma = cont = 0
while True:
    num = int(input('Qual o número de sua escolha para soma? [999] para sair\n'))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Todos os números somados tirando a flag deu {soma} e você colocou {cont} vezes um valor')