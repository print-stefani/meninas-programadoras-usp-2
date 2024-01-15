#Escreva um programa que solicite ao usuário uma frase e, em seguida, monte um dicionário que registra o número de ocorrências de cada palavra na frase, desconsiderando pontuações como vírgulas, ponto final, ponto e vírgula, aspas, barra inclinada e dois pontos.
frase = input()

pontuacao = "',.;:\"\\/"
for c in pontuacao:
    frase = frase.replace(c, "")

palavras = frase.split()
contagem = {}

for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

print(contagem)
