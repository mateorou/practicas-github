import random

random=random.randint(1,5)
usuario=int(input("Introduce un número del 1 al 5: "))

if usuario!=random:
    print("Fallaste")
else:
    print("Acertaste")
if usuario>5:
    print("El número es demasiado grande")
