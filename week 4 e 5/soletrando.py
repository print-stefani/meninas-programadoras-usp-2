#seu programa primeiro lê a palavra que as crianças devem soletrar. 
#A seguir, a criança digita uma sequencia de letras, uma por linha, e, quando terminar, digita o ponto final. 
#Você sinaliza para a professora com True e False, respectivamente, caso a criança acerte ou não a palavra.

palavra = input()
letra = input()
linha = letra

while letra != ".":
    letra = input()
    if letra != ".":
        linha += letra

if palavra in linha:
    print("True")
else:
    print("False")
