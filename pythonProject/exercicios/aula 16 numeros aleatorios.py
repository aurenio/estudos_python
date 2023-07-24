from random import sample
num = tuple(sample(range(10), 5))
print(f'Os números gerados foram {sorted(num)}')
print(f"O maior número é {max(num)}")
print(f"O menor valor é {min(num)}")
