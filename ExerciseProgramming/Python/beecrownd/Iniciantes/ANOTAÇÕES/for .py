contador = 0

for i in range(1, 21):

#verifica se o número é par:
    
     if i % 2 == 0:  

 #se o número de fato for par, então ele agrupa com o resto da divisão e soma +1.
       
        contador += 1
#fazendo assim, um exemplo prático: se o contador for 1, então ele soma por mais 1, apresentando assim os números pares.

print(f"Números pares de 1 a 20: {contador}")