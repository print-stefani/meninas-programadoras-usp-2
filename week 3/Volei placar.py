#Seu programa deve atualizar o placar de um jogo de volei, considerando a pontuação de um set entre 0 e 23 pontos

time_1 = input()
time_2 = input()
pontuacao = [int(i) for i in input().split()]

p_time_1 = int(pontuacao[0])
p_time_2 = int(pontuacao[1])
ponto = int(pontuacao[2])

if ponto == 1:
    p_time_1 += 1
elif ponto == 2:
    p_time_2 += 1

print(time_1, p_time_1)
print(time_2, p_time_2)

