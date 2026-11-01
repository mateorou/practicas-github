# 25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
nota = float(input("Introduce tu nota: "))

if nota < 5:
    print(f"Tu nota es {nota}, has sacado un insuficiente.")
elif nota >= 5 and nota < 6.5:
    print(f"Tu nota es {nota}, has sacado un satisfactorio.")
elif nota >= 6.5 and nota < 8.5:
    print(f"Tu nota es {nota}, has sacado un notable.")
else:
    print(f"Tu nota es {nota}, has sacado un excelente.")