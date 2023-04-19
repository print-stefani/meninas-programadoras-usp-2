#coordenada de X,Y do plano
coord1 = [int(i) for i in input().split()]
coord2 = [int(i) for i in input().split()]

#calculo Pitágoras
distancia = ((coord2[0]-coord1[0])**2 + (coord2[1]-coord1[1])**2)**0.5

#retorno da distancia de dois pontos
print("{:.1f}".format(distancia))
