def caracteres_infiltrados(primer_texto, segundo_texto):
    lista_nueva = []

    if len(primer_texto) == len(segundo_texto):
        i = 0
        while i < len(primer_texto):
            if primer_texto[i] != segundo_texto[i]:
                lista_nueva += [segundo_texto[i]]                 
            i = i + 1
        return lista_nueva
    
    else:
        return "La longitud de ambos textos no son iguales."


primer_texto = input("Introduce el primer texto: ")
segundo_texto = input("Introduce el segundo texto: ")

resultado = caracteres_infiltrados(primer_texto, segundo_texto)

print(resultado)
