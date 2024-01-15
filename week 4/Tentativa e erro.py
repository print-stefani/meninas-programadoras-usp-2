#Para passar o tempo, você programou um jogo no qual você "escolhe" um valor e depois deixa uma colega chutar valores até acertar o valor que você "escolheu". As regras são
#primeiro você digita o número-alvo a ser encontrado
#depois você deixa sua amiga chutar um valor até que ela acerte
numero_alvo = int(input())

while True:
    palpite = int(input())
    if palpite < numero_alvo:
        print("maior")
    elif palpite > numero_alvo:
        print("menor")
    else:
        print("igual")
        break
