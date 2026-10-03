# 18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.
numero_menores = int(input("Introduce el número de menores: "))
numero_adultos = int(input("Introduce el número de adultos: "))
precio_entrada = 12
descuento_menores = 0.5
descuento_adultos = 0.1

precio_menores = numero_menores * precio_entrada * (1 - descuento_menores)
precio_adultos = numero_adultos * precio_entrada * (1 - descuento_adultos)
total_pagar = precio_menores + precio_adultos

print(f"El precio del cine para {numero_menores} menor/es es: {precio_menores:.1f}")
print(f"El precio del cine para {numero_adultos} adulto/s es: {precio_adultos:.1f}")
print(f"El total a pagar es: {total_pagar:.1f}")