# Seu programa deve ler o valor mínimo esperado e, a seguir, um conjuntos de valores. 
#Quanto o valor mínimo for atingido, você imprime o mínimo, o total e quanto sobrou além do mínimo. 

minimo = int(input())
total = 0

while True:
    valor = int(input())
    total += valor
    if total >= minimo:
        sobra = total - minimo
        print("minimo", minimo)
        print("total", total)
        print("sobra", sobra)
        break
