
class Calculadora:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def suma(self):
        return self.a + self.b
    
    def resta(self):
        return self.a - self.b
    
    def mult(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b
    
operacion = Calculadora(12,2)

print(operacion.suma())
print(operacion.resta())
print(operacion.mult())
print(operacion.div())