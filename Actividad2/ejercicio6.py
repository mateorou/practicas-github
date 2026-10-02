# 6. A partir del programa 5. Haz que se muestre por pantalla también la frase en el orden inverso en que se han introducido las palabras. 
palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")
palabra3 = input("Introduce la tercera palabra: ")
palabra4 = input("Introduce la cuarta palabra: ")
palabra5 = input("Introduce la quinta palabra: ")
frase = palabra1 + palabra2 + palabra3 + palabra4 + palabra5
frase_inversa = palabra5 + palabra4 + palabra3 + palabra2 + palabra1
print("Frase:", frase)
print("Frase en orden inverso:", frase_inversa)