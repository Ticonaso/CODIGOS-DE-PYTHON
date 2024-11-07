
class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def mostrar(self):
        print(f"La persona se llama {self.nombre} {self.apellido}")

class Estudiante(Persona):
    def __init__(self,nombre,apellido,carrera):
        super().__init__(nombre,apellido)
        self.carrera = carrera
    
    def mostrarcarrera(self):

        print((f"El estudiante {self.nombre} estudia {self.carrera}"))
michell1 = Estudiante("michell","ticona","programacion")
michell1.mostrarcarrera()