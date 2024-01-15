valores = input().split()

if not valores:
    print("Lista vazia")
else:
    valores = [int(valor) for valor in valores]
    menor = valores[0]

    for valor in valores:
        if valor < menor:
            menor = valor

    print(menor)
