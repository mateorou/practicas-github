#7 OPERACIONES MATEMÁTICAS
import math

var1= float(input("Introduce un número: "))
var2= float(input("Introduce otro número: "))
result= var1+var2

print(f"La suma de los números es {var1+var2:.0f}")
print(f"La resta de los números es {var1-var2:.0f}")
print(f"La multiplicación de los números es {var1*var2:.0f}")
print(f"La división de los números es {var1/var2:.0f}")
print(f"La división entera de los números es {var1//var2:.1f}")
print(f"El módulo de los números es {var1%var2:.1f}")
print(f"La potencia de los números es {var1**var2:.1f}")

#MÉTODOS DE REDONDEO
print(f"La suma es ", round(result,2))

print(f"La suma es {result:.2f})

print(f"La suma es ", math.ceil(result,2))

print(f"La suma es ", math.floor(result,2))
