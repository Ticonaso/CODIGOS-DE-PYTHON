
class Fabrica:
    def __init__(self,llanta,color,precio ):
        self.llanta = llanta
        self.color = color
        self.precio = precio

class Moto(Fabrica):
    def cantidad(self):
        print(self.llanta,self.color,self.precio)
     
class Carro(Fabrica):
        def cantidad(self):
            print(self.llanta,self.color,self.precio)

carro_1 = Carro(4,"rojo",12000)
moto_1 = Moto(2,"amarillo",8000)
moto_2 = Moto(2,"negro",1000)

moto_1.cantidad()
carro_1.cantidad()