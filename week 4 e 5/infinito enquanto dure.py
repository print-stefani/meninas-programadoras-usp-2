#Seu programa deve consumir a sua própria condição de parada e, depois, 
#consumir linhas da entrada até que seja fornecida a condição de parada lida originariamente, contando o número de linhas consumidas

condicao_parada = input()
linhas_consumidas = 0

while True:
    linha = input()
    linhas_consumidas += 1
    if linha == condicao_parada:
        break

print(linhas_consumidas - 1)
