respuesta=input("Introduce una letra: ")
if respuesta.isnumeric()==False:
    if respuesta.isupper():
        print("Es mayúscula")
    else:
        print("Es minúscula")
else:
    print("El valor introducido no es una letra")