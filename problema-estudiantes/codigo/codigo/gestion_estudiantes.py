def main():
    suma_notas = 0
    nombres = []
    notas = []

    entrada = input("Ingresa los nombres y notas de los estudiantes: ")
    datos_estudiantes = entrada.split()

    for i in range(0, len(datos_estudiantes), 2):
        nombre = datos_estudiantes[i]
        nota = float(datos_estudiantes[i + 1])

        nombres.append(nombre)
        notas.append(round(nota, 2))

    for nota in notas:
        suma_notas += nota

    promedio = suma_notas / len(notas)

    for i in range(len(notas)):
        if notas[i] >= promedio:
            print(nombres[i])

main()
