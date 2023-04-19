#entradas 
a = float (input())
b = float (input())
c = float (input())

#calculo delta
delta = b ** 2 - 4 * a * c

#condição para saber as raizes ou não
if delta == 0:
    print (1)
else:
    if delta >= 0:
        print (2)
    else:
        print (0)
