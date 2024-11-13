def simulador_clima(temperatura_inicial: int, lluvia_inicial: int, dias: int):

    dias_lluviosos = 0
    temperatura_minima = temperatura_inicial
    temperatura_maxima = temperatura_inicial

    for dia in range(1, dias + 1):

        print(f"Día {dia}: {temperatura_inicial} grados y {lluvia_inicial}% de probabilidad de lluvia")

        if lluvia_inicial == 100:
            dias_lluviosos += 1

        if temperatura_inicial < temperatura_minima:
            temperatura_minima = temperatura_inicial

        if temperatura_inicial > temperatura_maxima:
            temperatura_maxima = temperatura_inicial

        if (temperatura_inicial % 10) == 1:
            if (temperatura_inicial % 2) == 1:
                temperatura_inicial += 2
            else:
                temperatura_inicial -= 2

        if temperatura_inicial > 25:
            lluvia_inicial += 20
            if lluvia_inicial > 100:
                lluvia_inicial = 100

        elif temperatura_inicial < 5:
            lluvia_inicial -= 20
            if lluvia_inicial < 0:
                lluvia_inicial = 0

        if lluvia_inicial == 100:
            temperatura_inicial -= 1

    print(f"Días lluviosos: {dias_lluviosos}")
    print(f"Temperatura mínima: {temperatura_minima}")
    print(f"Temperatura máxima: {temperatura_maxima}")


temperatura = int(input("Introduce la temperatura inicial: "))
lluvia = int(input("Introduce la probabilidad de lluvia inicial (0-100): "))
dias = int(input("Introduce la cantidad de días a simular: "))

simulador_clima(temperatura, lluvia, dias)
