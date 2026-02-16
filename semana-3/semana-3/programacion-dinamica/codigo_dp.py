def buscar_binaria(lista, nombre):
    izquierda = 0
    derecha = len(lista) - 1
  
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio][0] == nombre:
            return medio
        elif lista[medio][0] < nombre:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
  
def main():
    estudiantes = []
    sumar_notas = 0
    contador = 0

    while True:
        print("\n1. Registrar estudiante")
        print("2. Buscar estudiante")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Mostrar promedio")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            nota = float(input("Nota: "))

            estudiantes.append((nombre, nota))
            estudiantes.sort()

            sumar_notas += nota
            contador += 1
            print("Estudiante registrado")

        elif opcion == "2":
            nombre = input("Nombre a buscar: ")
            pos = buscar_binaria(estudiantes, nombre)

            if pos != -1:
                print("Encontrado:", estudiantes[pos])
            else:
                print("No encontrado")

        elif opcion == "3":
            nombre = input("Nombre a actualizar: ")
            pos = buscar_binaria(estudiantes, nombre)

            if pos != -1:
                nueva_nota = float(input("Nueva nota: "))
                sumar_notas -= estudiantes[pos][1]
                sumar_notas += nueva_nota
                estudiantes[pos] = (nombre, nueva_nota)
                estudiantes.sort()
                print("Actualizado")
            else:
                print("No encontrado")

        elif opcion == "4":
            nombre = input("Nombre a eliminar: ")
            pos = buscar_binaria(estudiantes, nombre)

            if pos != -1:
                sumar_notas -= estudiantes[pos][1]
                contador -= 1
                estudiantes.pop(pos)
                print("Eliminado")
            else:
                print("No encontrado")

        elif opcion == "5":
            if contador > 0:
                promedio = sumar_notas / contador
                print("Promedio:", round(promedio, 2))
            else:
                print("No hay estudiantes")

        elif opcion == "6":
            print("Programa finalizado")
            break

        else:
            print("Opción inválida")

main()
