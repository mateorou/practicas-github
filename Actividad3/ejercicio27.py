# 27. Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla.
letra = input("Introduce una letra: ")
if letra.isalpha():
    if letra.isupper():
        print(f"La letra es mayúscula.")
    else:
        print(f"La letra es minúscula.")
else:
    if letra.isdigit():
        print(f"El valor introducido es un número.")
    else:
        print(f"La letra es mayúscula ¿?")