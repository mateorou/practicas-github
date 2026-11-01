# 24. Corrige los errores del siguiente código y comprueba que se ejecuta correctamente.
peso = float(input("Introduce el peso: "))
altura = float(input("Introduce la altura: "))

var_imc = peso / altura**2

print(f"Si pesas {peso} kilos y mides {altura}, tu IMC es: {var_imc}")

if var_imc > 25:
    print("Hay sobrepeso")
else:
    print("Estás dentro de los parámetros normales")