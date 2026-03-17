# Clase base
class Estudiante:

    def __init__(self, nombre, matricula, edad, carrera):
        self.nombre = nombre
        self.matricula = matricula
        self.edad = edad
        self.carrera = carrera

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Matrícula:", self.matricula)
        print("Edad:", self.edad)
        print("Carrera:", self.carrera)


# Clase derivada Licenciatura
class EstudianteLicenciatura(Estudiante):

    def __init__(self, nombre, matricula, edad, carrera, semestre):
        super().__init__(nombre, matricula, edad, carrera)
        self.semestre = semestre

    def mostrar_info(self):
        super().mostrar_info()
        print("Semestre:", self.semestre)
        print("----------------------")


# Clase derivada Posgrado
class EstudiantePosgrado(Estudiante):

    def __init__(self, nombre, matricula, edad, carrera, especialidad):
        super().__init__(nombre, matricula, edad, carrera)
        self.especialidad = especialidad

    def mostrar_info(self):
        super().mostrar_info()
        print("Especialidad:", self.especialidad)
        print("----------------------")


# Sistema
class SistemaEstudiantes:

    def __init__(self):
        self.lista_estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.lista_estudiantes.append(estudiante)
        print("Estudiante agregado correctamente.\n")

    def mostrar_estudiantes(self):
        if len(self.lista_estudiantes) == 0:
            print("No hay estudiantes registrados.\n")
        else:
            for estudiante in self.lista_estudiantes:
                estudiante.mostrar_info()


# Programa principal
def main():

    sistema = SistemaEstudiantes()

    while True:

        print("\n===== SISTEMA DE ESTUDIANTES =====")
        print("1. Agregar estudiante Licenciatura")
        print("2. Agregar estudiante Posgrado")
        print("3. Mostrar estudiantes")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            matricula = input("Matrícula: ")
            edad = int(input("Edad: "))
            carrera = input("Carrera: ")
            semestre = input("Semestre: ")

            estudiante = EstudianteLicenciatura(nombre, matricula, edad, carrera, semestre)
            sistema.agregar_estudiante(estudiante)

        elif opcion == "2":
            nombre = input("Nombre: ")
            matricula = input("Matrícula: ")
            edad = int(input("Edad: "))
            carrera = input("Carrera: ")
            especialidad = input("Especialidad: ")

            estudiante = EstudiantePosgrado(nombre, matricula, edad, carrera, especialidad)
            sistema.agregar_estudiante(estudiante)

        elif opcion == "3":
            sistema.mostrar_estudiantes()

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()