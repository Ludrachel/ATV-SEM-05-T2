def valor_bool(caractere):
    return caractere in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
palavra = input()
print(valor_bool(palavra.upper()))
