from datetime import date

# lendo a data atual
atual = input().split()
dia_atual, mes_atual, ano_atual = int(atual[0]), int(atual[1]), int(atual[2])

# lendo a data de validade do remédio
validade = input().split()
dia_validade, mes_validade, ano_validade = int(validade[0]), int(validade[1]), int(validade[2])

# criando objetos date com as datas informadas
hoje = date(ano_atual, mes_atual, dia_atual)
validade_remedio = date(ano_validade, mes_validade, dia_validade)

# calculando a diferença de dias entre as datas
dias_restantes = (validade_remedio - hoje).days

if dias_restantes < 0:
    print("vencido!")
elif dias_restantes < 31:
    print("vence este mês")
elif dias_restantes < 365:
    print("vence este ano")
else:
    print("na validade")
