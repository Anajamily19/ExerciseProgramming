codigo_1, num_1, valor_1 = (input("")).split() 
codigo_1 = int(codigo_1)
num_1 = int(num_1)
valor_1 = float(valor_1)

codigo_2, num_2, valor_2 = (input("")).split()
codigo_2 = int(codigo_2)
num_2 = int(num_2)
valor_2 = float(valor_2)

total = (num_1 * valor_1) + (num_2 * + valor_2)

print(f"VALOR A PAGAR: R$ {total:.2f}")
