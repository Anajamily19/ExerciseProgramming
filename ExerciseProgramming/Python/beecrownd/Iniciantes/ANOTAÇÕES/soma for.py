n = int(input("Digite N: "))
soma = 0

for i in range(1, n + 1):
    print(i)
    soma += i

print(f"\nSoma de 1 a {n}: {soma}")