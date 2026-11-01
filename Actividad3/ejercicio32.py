# 32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas.
frase = "A quién madruga Dios ayuda."
frase_lower = frase.lower()

madruga_index = frase_lower.find('madruga')
Dios_index = frase_lower.find('dios')
dios_index = frase_lower.find('dios')

if madruga_index != -1:
    print(f"La palabra 'madruga' está en la frase y está en el índice {madruga_index}")
else:
    print("La palabra 'madruga' no está en la frase")

if Dios_index != -1:
    print(f"La palabra 'Dios' está en la frase y está en el índice {Dios_index}")
else:
    print("La palabra 'Dios' no está en la frase")

if dios_index != -1:
    print(f"La palabra 'dios' está en la frase y está en el índice {dios_index}")
else:
    print("La palabra 'dios' no está en la frase")