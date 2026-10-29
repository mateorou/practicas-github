import random

random=random.randint(1,5)
usuario=int(input("Introduce un número del 1 al 5: "))

if usuario in [1,2,3,4,5]:
    if int(usuario)==random:
        print("Acertaste")
    else:
        print("Fallaste")
else:
    print("No has introducido el rango correcto.")