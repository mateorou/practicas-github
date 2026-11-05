# 23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.
nota = float(input("Introduce tu nota: "))

if nota < 5:
    print(f"Tu nota es {nota}, has sacado un insuficiente.")
elif nota < 6.5:
    print(f"Tu nota es {nota}, has sacado un satisfactorio.")
elif nota < 8.5:
    print(f"Tu nota es {nota}, has sacado un notable.")
else:
    print(f"Tu nota es {nota}, has sacado un excelente.")