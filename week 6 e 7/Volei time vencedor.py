
T1 = input ()
T2 = input ()
pontos_T1 = [int (i) for i in input() .split ()]
pontos_T2 = [int (i) for i in input() .split ()]

numero_de_jogos = len (pontos_T1 or pontos_T2)

vitoria_T1 = 0
vitoria_T2 = 0

for i in range (numero_de_jogos):
  if (pontos_T1 [i] > pontos_T2 [i]):
    vitoria_T1 = vitoria_T1 + 1
  else:
    vitoria_T2 = vitoria_T2 + 1

if vitoria_T1 > vitoria_T2:
  print (T1, '(total', numero_de_jogos, 'sets)')
else:
    print (T2, '(total', numero_de_jogos, 'sets)')
