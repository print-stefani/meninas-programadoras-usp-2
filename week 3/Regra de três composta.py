#dados os valores iniciais de meninas, dias e monitores,  e os valores da demanda de alunas e dias, 
#seu programa deve informar quantos monitores são necessários para atender a demanda.  

meninas = int(input())
dias = int(input())
monitores = int(input())

demanda_alunas = int(input())
demanda_dias = int(input())

demanda_monitores = (monitores * demanda_alunas * demanda_dias) / (meninas * dias)

print(int(demanda_monitores))
