class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self,dato):
        self.raiz = Nodo(dato)

    def agregar_recursivo(self,nodo,dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.agregar_recursivo(nodo.derecha,dato)
    
    def agregar(self, dato):
        self.agregar_recursivo(self.raiz,dato)

    def inorden_recursivo(self,nodo):
        if nodo is not None:
            self.inorden_recursivo(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.inorden_recursivo(nodo.derecha)

    def inorden(self):
        self.inorden_recursivo(self.raiz)
        print("")