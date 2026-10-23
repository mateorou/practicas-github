# 20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10.

num1=int(input("Introduce un número: "))
num2=int(input("Introduce otro número: "))

if num1 and num2 in [1,2,3,4,5,6,7,8,9,10]:
    
    if num1 > num2:
        print(f"El número {num1} es mayor que el número {num2}")

    elif num1 == num2:
        print(f"Ambos números son iguales.")

    elif num1 < num2:
        print(f"El número {num1} es menor que el número {num2}")
else:
    print(f"El número no está dentro del rango.")