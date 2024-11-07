
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def cum(self):
        try:
            self.edad += 1
        except TypeError:
            print("Tiene que colocar un numero")
        print(f"La nueva edad de {self.nombre} es {self.edad}")

kelvin = Persona("kelvin",19)

kelvin.cum()
kelvin.cum()
kelvin.cum()

mamani = Persona("mamani","platano")
mamani.cum()
kelvin.cum()