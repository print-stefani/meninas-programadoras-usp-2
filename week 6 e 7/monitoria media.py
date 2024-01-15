#Dadas as horas de monitorias feitas por um grupo de alunas, calcule a média aritmética das horas trabalhadas pelas alunas. Use uma casa decimal.

num_alunas = int(input())  # Número de alunas no grupo
horas_alunas = []  # Lista para armazenar as horas de cada aluna

# Lê as horas de cada aluna
for _ in range(num_alunas):
    horas = int(input())
    horas_alunas.append(horas)

# Calcula a média das horas
media_horas = sum(horas_alunas) / num_alunas

# Imprime o resultado com uma casa decimal
print("{:.1f}".format(media_horas))
