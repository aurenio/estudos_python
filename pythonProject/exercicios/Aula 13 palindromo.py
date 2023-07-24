inverso = ''
pali = str(input("Verifique se é um palidromo:\n")).replace(" ","").lower()
for c in range(len(pali) -1, -1, -1):
    inverso += pali[c]
print(pali)
print(inverso)
if pali == inverso :
    print("Sua palavra é um palindromo")
else:
    print("Sua palavra não é um palindromo")