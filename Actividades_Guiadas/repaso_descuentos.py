# Una tienda aplica un 10% de descuento a un producto y después añade un 21% de IVA
precio_inicial=float(input("Introduce el precio del producto: "))

precio_descuento= precio_inicial - precio_inicial* 0.10
precio_iva=  precio_descuento + precio_descuento * 0.21

print(f"El precio con descuento son {precio_descuento}€.")
print(f"El precio con IVA son {precio_iva}€.")

precio_total= precio_inicial * (1-0.10) *(1+0.21)

# Los dos métodos de redondeo
print((round(precio_total,2)))
print(f"El precio total es {precio_total:.2f}")

# print(f"El producto con precio {precio_inicial}€ tiene un descuento de {precio_descuento}€ y un total de {precio_iva}€ con IVA.")