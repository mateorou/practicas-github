# 27. Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla.
respuesta=input("Introduce una letra: ")
if respuesta.isnumeric()==False:
    if respuesta.isupper():
        print("Es mayúscula")
    else:
        print("Es minúscula")
else:
    print("El valor introducido no es una letra")