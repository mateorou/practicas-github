# 15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math

radio = float(input("Introduce el radio del cilindro: "))
altura = float(input("Introduce la altura del cilindro: "))

area = 2 * math.pi * radio ** 2 + 2 * math.pi * radio * altura
volumen = math.pi * radio ** 2 * altura

print(f"El área de un cilindro es: {area:.2f}")
print(f"El volumen de un cilindro es: {volumen:.2f}")