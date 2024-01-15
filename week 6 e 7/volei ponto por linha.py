#Seu programa recebe os pontos de um set, um por linha: o valor 1 indica ponto do time 1, e o valor dois indica ponto do time 2.

soma_1 = 0
soma_2 = 0

diferenca = 0

while ((soma_1 < 25 and soma_2 < 25) or diferenca < 2):

  entrada = int(input())
  if(entrada == 1):
    soma_1 += 1
  elif(entrada == 2):
    soma_2 += 1

  if(soma_1 > soma_2):
    diferenca = soma_1 - soma_2

  else:
    diferenca = soma_2 - soma_1

print (soma_1,'x',soma_2)
