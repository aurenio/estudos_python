num = []
for cont in range(0, 7):
    num.append(int(input("Digite um valor\n")))

num = [ par for par in num if par % 2 == 0], [ impa for impa in num if impa % 2 == 1]

num = sorted(num[0]), sorted(num[1])
print(f"Os pares são {num[0]} em ordem crecente e os impar são {num[1]} em ordem crescente")