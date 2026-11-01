# 33. Programa un código que permita contar el número de vocales de la siguiente frase: No hay mal que dure cien años.
frase = "No hay mal que dure cien años."
vocales = "aeiouAEIOU"
contador = 0
for letra in frase:
    if letra in vocales:
        contador += 1
print(f"El número de a es: {frase.count('a')}, el número de e es: {frase.count('e')}, el número de i es: {frase.count('i')}, el número de o es: {frase.count('o')}, el número de u es: {frase.count('u')}.")