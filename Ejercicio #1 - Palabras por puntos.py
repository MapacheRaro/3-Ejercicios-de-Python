def calcular_puntos(palabra):
    puntos = 0
    dicionario_letras = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
        "K": 11, "L": 12, "M": 13, "N": 14, "Ñ": 15, "O": 16, "P": 17, "Q": 18, "R": 19,
        "S": 20, "T": 21, "U": 22, "V": 23, "W": 24, "X": 25, "Y": 26, "Z": 27,
        "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
        "k": 11, "l": 12, "m": 13, "n": 14, "ñ": 15, "o": 16, "p": 17, "q": 18, "r": 19,
        "s": 20, "t": 21, "u": 22, "v": 23, "w": 24, "x": 25, "y": 26, "z": 27
    }

    for i in palabra:  
        if i in dicionario_letras: 
            puntos += dicionario_letras[i]  
        else:
            puntos += 0 

    return puntos

def jugar_Reto_Programacion():
    while True:
        palabra = input("Escribe una palabra: ")
        puntos = calcular_puntos(palabra)
        print("Tu palabra vale", puntos, "puntos")

        if puntos == 100:
            print("¡Lo lograste! Fin del juego.")
            break
        elif puntos > 100:
            print("Has superado los 100 puntos. Fin del juego.")
            break
        else:
            print("Intenta nuevamente.")

jugar_Reto_Programacion()
