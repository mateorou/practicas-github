# 28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.
letra = input("Introduce una letra: ")
if letra.isalpha():
    if letra.isupper():
        print(f"La letra es mayúscula.")
    else:
        print(f"La letra es minúscula.")
elif letra.isdigit():
    print(f"El valor introducido es un número.")
else:
    print(f"El valor introducido es un símbolo.")