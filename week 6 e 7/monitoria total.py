#Dadas as horas de monitorias feitas por um grupo de alunas, calcule a soma total de horas trabalhadas pelas alunas.

num_alunas = int(input()) 
horas_alunas = []  

for _ in range(num_alunas):
    horas = int(input())
    horas_alunas.append(horas)

soma_horas = sum(horas_alunas)

print(soma_horas)
