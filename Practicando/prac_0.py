#atributos: Nombre, nota
#metodos: imprimir(nombre y nota), aprobado o desaprobado

class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar(self):
        print(f"El alumno {self.nombre} tiene {self.nota} de nota")

    def aprob(self):
        if self.nota >= 13:
            print(f"el alumno {self.nombre} esta aprobado")
        else:
            print(f"el alumno {self.nombre} esta desaprobado")

Ticonaso = Alumno("Michell",3)
kelvin_pc = Alumno("Kelvin",15)
River = Alumno("River",13)
mamane = Alumno("Mamani",16)

Ticonaso.mostrar()
kelvin_pc.mostrar()
River.aprob()

mamane.mostrar()
mamane.aprob()
