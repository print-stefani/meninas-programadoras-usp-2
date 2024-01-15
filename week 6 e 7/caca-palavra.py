#Para construirmos um jogo de caça-palavras, precisamos saber quais palavras queremos caçar e em que matriz de letras vamos busca-las.

palavra = input ()
caca_palavra = [str (i) for i in input().split()]

if palavra in caca_palavra:
  achou = caca_palavra.index(palavra)
  print (palavra, achou)
else:
  print ("falta", palavra)
