import math

radio= float(input("Introduce el radio:"))

longitud= 2*radio*math.pi
area= math.pi*radio**2

print(f"La longitud del círculo es de {longitud:.2f}")
print(f"El área del círculo es de {area:.2f}")