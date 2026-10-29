import math

radio= float(input("Introduce el radio:"))
area= math.pi*radio**2
longitud= 2*radio*math.pi

print(f"El área del círculo es de {area:.2f}")
print(f"La longitud del círculo es de {longitud:.2f}")

#Cuatro métodos de redondeo
print("El área del círculo es de ",round(area,2))
print(f"La longitud del círculo es de {longitud:.2f}")
print(math.ceil(area))
print(math.floor(area))