#Dada uma mensagem , você precisa trocar todas as ocorrências de um caractere específico por outro. 

caractere_orig = input()
caractere_subs = input()
mensagem = input()

mensagem_cripto = ""

for letra in mensagem:
    if letra == caractere_orig:
        mensagem_cripto += caractere_subs
    else:
        mensagem_cripto += letra

print(mensagem_cripto)
