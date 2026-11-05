# 7. Programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?
operando1 = float(input("Introduce el primer operando: "))
operando2 = float(input ("Introduce el segundo operando: "))

suma = operando1 + operando2
resta = operando1 - operando2
multiplicacion = operando1 * operando2
division = operando1 / operando2
division_entera = operando1 // operando2
potencia = operando1 ** operando2
modulo = operando1 % operando2

print (f"La suma de operador1 y operador2 es: {suma:.0f}")
print (f"La resta de operador1 y operador2 es: {resta:.0f}")
print (f"La multiplicación de operador1 y operador2 es: {multiplicacion:.0f}")
print (f"La división de operador1 y operador2 es: {division:.2f}")
print (f"El módulo de operador1 y operador2 es: {modulo:.0f}")
print (f"La potencia de operador1 y operador2 es: {potencia:.0f}")
print (f"La división entera de operador1 y operador2 es: {division_entera:.0f}")