#Escreva um programa que solicite ao usuário uma frase e, em seguida, conte o número de ocorrências de cada palavra na frase.
def contar_palavras(frase):
    palavras = frase.split()
    contagem = {}

    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem

frase = input()
resultado = contar_palavras(frase)
print(resultado)
