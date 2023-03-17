def valor_bool(caractere):
    return caractere in "AEIOU"
palavra = input()
print(valor_bool(palavra.upper()))
