
class Perro:
    def __init__(self,peso,nombre,raza):
        self.peso = peso
        self.nombre = nombre
        self.raza = raza
    
    def comer(self):
        print(f"el perro {self.nombre} es comiendo")

perro_1 = Perro(30,"juan","golden")

print(perro_1.peso)
print(perro_1.nombre)
print(perro_1.raza)

perro_1.comer()