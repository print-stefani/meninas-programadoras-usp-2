#inteiro positivo com o número de movimentações financeiras a serem processadas
n_financeiro = int(input("Digite o numero de movimentações financeiras: "))

c_alimentacao = c_moradia = c_transporte = c_saude = c_lazer = salario = pres_servico = 0
total_renda = total_gastos = 0

print("\n Para efetuar o Balanço Financeiro - Siga as instruções \n \n Caso coloque despesas insira valores NEGATIVOS \n Caso seja obtenção de recursos insira valores POSITIVOS \n \n Despesas aceitas pelo programa: \n A (alimentação) \n M (moradia)\n T (transporte) \n S (saúde) \n L (lazer) \n \n Recursos aceitos: \n S (salário) \n P (prestação de serviços) \n \n ATENÇÃO: Insira apenas as inicias de despesas e recursos \n")
  

for i in range(n_financeiro):
  #apos saber quantas movimentações, categorizar
    valor = float(input("Informe o valor: ")) 
    # letra com a origem da despesa: A (alimentação), M (moradia), T (transporte), S (saúde) e L (lazer)
    tipo = str(input("Informe o tipo: ")) #valor for positivo, uma letra com a origem do recurso: S (salário), P (prestação de serviços)
    if valor < 0:
        total_gastos += valor
        if tipo == 'A':
            c_alimentacao += valor
        elif tipo == 'M':
            c_moradia += valor
        elif tipo == 'T':
            c_transporte += valor
        elif tipo == 'S':
            c_saude += valor
        else:
            c_lazer += valor
    else:
        total_renda += valor
        if tipo == 'S':
            salario += valor
        else:
            pres_servico += valor

print('\nMovimentações Fnanceiras \n\nDESPESAS \n')
if c_alimentacao != 0:
  print('Alimentação: ','%.2f'% (c_alimentacao))


if c_moradia != 0:
  print('Moradia: ','%.2f'% (c_moradia))

if c_transporte != 0:
  print('Transporte: ','%.2f'% (c_transporte))

if c_saude != 0:
  print('Saúde: ','%.2f'% (c_saude))

if c_lazer != 0:
  print('Lazer: ','%.2f'% (c_lazer))

print ("\n\nRECURSOS \n")
if salario != 0:
  print('Salário: ','%.2f'% (salario))

if pres_servico != 0:
  print('Prestação de serviços: ','%.2f'% (pres_servico))


print('\nTotal de Renda: ','%.2f'% (total_renda))
print('Total de Gastos: ','%.2f'% (total_gastos))

balanco = total_renda + total_gastos

print('\nBalanço: ','%.2f'% (balanco))
