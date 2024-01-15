silabas = input().split()
combinacoes = [s1 + s2 for s1 in silabas for s2 in silabas]
palavras_selecionadas = []

for combinacao in combinacoes:
    print(combinacao)
    resposta = input().upper()
    if resposta == 'S':
        palavras_selecionadas.append(combinacao)

print(palavras_selecionadas)
