#Dadas strings que indicam a evolução de pontos em sets de um jogo de volei, seu programa deve imprimir o placar com os pontos em cada set e a soma de pontos de cada time. 

time_1 = input ()
time_2 = input ()

rodada = input ()

total_1 = 0
total_2 = 0

p1 = []
p2 = []


while (rodada != 'fim'):
  pontos_1 = rodada .count ('1')
  total_1 = total_1 + pontos_1
  p1 .append (pontos_1)
  pontos_2 = rodada .count ('2')
  total_2 = total_2 + pontos_2
  p2 .append (pontos_2)

  rodada = input ()

print (time_1, end=" ")

for i in p1:
  print (i, end= " ")
print ('(', total_1, ')')

print (time_2, end=" ") 

for i in p2:
  print (i, end= " ")
print ('(', total_2, ')')
