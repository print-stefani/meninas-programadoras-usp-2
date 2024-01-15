entrada = int(input())

if entrada < 0:
    print()
else:
    fatorial = 1
    for i in range(1, entrada + 1):
        fatorial *= i

    fatorial_str = str(fatorial)
    dez_primeiros_digitos = fatorial_str[:10]
    num_caracteres = len(fatorial_str)

    print(num_caracteres, dez_primeiros_digitos)
