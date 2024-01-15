#Um PIN é menos inseguro quando é formado pela soma de um conjunto de valores. 

nr_vezes = int (input())
soma = 0

for i in range(nr_vezes):
    pin = int (input())
    soma += pin
print (soma)
