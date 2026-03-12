class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None

    def frente(self):
        if not self.esta_vacia():
            return self.elementos[0]
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def tamaño(self):
        return len(self.elementos)

def sistema_pacientes():
    cola_criticos = Cola()
    cola_normales = Cola()
    print("Sistema de atención médica")
    print("Ingrese el número de acciones:")
    n = int(input())
    print("Ingrese las acciones (N nombre, C nombre o A):")

    for _ in range(n):
        accion = input().split()

        if accion[0] == "N":
            nombre = accion[1]
            cola_normales.encolar(nombre)
            print("Paciente N nuevo :", nombre)

        elif accion[0] == "C":
            nombre = accion[1]
            cola_criticos.encolar(nombre)
            print("Paciente C nuevo :", nombre)

        elif accion[0] == "A":
            if not cola_criticos.esta_vacia():
                paciente = cola_criticos.desencolar()
                print("Se atiende a", paciente)

            elif not cola_normales.esta_vacia():
                paciente = cola_normales.desencolar()
                print("Se atiende a", paciente)

            else:
                print("no hay pacientes")

if __name__ == "__main__":
    sistema_pacientes()