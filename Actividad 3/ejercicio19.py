# 19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales

num1=int(input("Introduce un número: "))
num2=int(input("Introduce otro número: "))

if num1>num2:
    print(f"El número {num1} es mayor que el número {num2}")

elif num1==num2:
    print("Ambos números son iguales.")

else:
    print(f"El número {num1} es menor que el número {num2}")
