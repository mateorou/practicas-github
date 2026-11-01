# 31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice. Tendría que salir algo así: madruga Dios dios La palabra está en la frase y está en el índice 8 La palabra está en la frase y está en el índice 16 La palabra no está en la frase. La palabras son: madruga, Dios, dios. Hay que hacerlo con condicionales diciendo qué palabras salen y cuales no.
    
frase = "A quién madruga Dios ayuda."
print(f"La palabra 'madruga' está en la frase y está en el índice {frase.find('madruga')}")
print(f"La palabra 'Dios' está en la frase y está en el índice {frase.find('Dios')}")
print(f"La palabra 'dios' está en la frase y está en el índice {frase.find('dios')}")