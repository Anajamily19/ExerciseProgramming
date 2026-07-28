numero = int(input("Digite um número: "))
#pede que o usuário digite um valor de entrada

print(f"\nTabuada do {numero}:")
#apresenta o valor de entrada

for i in range(1, 11): #monta a tabela de números os quais a variável será multiplicada
    resultado = numero * i
#variável multiplicado pelo número da lista 
   
    print(f"{numero} x {i} = {resultado}")
#saída da tabela.