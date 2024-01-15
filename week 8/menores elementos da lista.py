valores = input().split()

if len(valores) < 2:
    print("lista pequena demais")
else:
    valores = [int(valor) for valor in valores]
    menor1 = valores[0]
    menor2 = valores[1]

    if menor1 > menor2:
        menor1, menor2 = menor2, menor1

    for valor in valores[2:]:
        if valor < menor1:
            menor2 = menor1
            menor1 = valor
        elif valor < menor2:
            menor2 = valor

    print(menor1, menor2)
