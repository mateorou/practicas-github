# 26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
letra = input("Introduce una letra: ")
if letra.isupper():
    print(f"La letra es mayúscula.")
if not letra.isupper():
    print(f"La letra es minúscula.")
else:
    print(f"La letra es mayúscula ¿?")