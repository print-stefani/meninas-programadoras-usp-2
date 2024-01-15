# Dadas três cartas distribuídas em uma rodada de truco na versão manilha velha, verificar quantas delas são manilhas fixas, representadas por 4Paus, 7Copas, AEspadas, 7Ouros

carta_1 = input ()
carta_2 = input ()
carta_3 = input ()

manilhas = ["4Paus", "7Copas", "AEspadas", "7Ouros"]

count = 0

if carta_1 in manilhas:
    count += 1

if carta_2 in manilhas:
    count += 1

if carta_3 in manilhas:
    count += 1

print(count)
