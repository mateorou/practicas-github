var_grados=float(input("Introduce los grados: "))
# F=c*9/5+32

calculo=var_grados *9/5 +32
print("Temperatura: ", calculo, "ºF")

# Otra manera de presentar la información con print:

print(f"Temperatura: {calculo} ºF")

# Primer método de redondeo:
print(round(calculo,2))

# Segundo método de redondeo:
print(f"Temperatura: {calculo:.2f} ºF")