def e_simbolo(ca):
    if ca.isalpha() or ca.isdigit():
        return False
    else:
        return True
caractere = input()
print(e_simbolo(caractere))
