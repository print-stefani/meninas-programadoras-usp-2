#Vamos desenhar um histograma? Seu programa deve ler uma linha que contém um algaritsmo entre 1 e 9, e imprimir uma sequência de asteriscos correspondente ao valor lido.
valor = int(input())

resultado = ""
for i in range(valor):
    resultado += "*"

print(resultado)
  
