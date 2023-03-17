def valor_bool(caractere):
    return caractere in "BCDFGHJKLMNPQRSTVWXYZ"
palavra = input()
print(valor_bool(palavra.upper()))
