#primeira linha: numero do qual queremos calcular a tabuada (valor entre 1 e 99)
#segunda linha: primeiro valor da tabuada a ser gerado (valor entre 1 e 999)
#terceira linha: último valor da tabuada a ser gerado (valor entre 1 e 999)

valor_calcular = int(input())
valor_tabuada = int(input())
valor_final = int(input())

print("Tabuada do {} de {} até {}".format(valor_calcular, valor_tabuada,valor_final))

for valor_tabuada in range (valor_tabuada,valor_final+1):
  valor_final = valor_calcular * valor_tabuada
  print ("{} x {} = {}".format (valor_calcular, valor_tabuada,valor_final))
