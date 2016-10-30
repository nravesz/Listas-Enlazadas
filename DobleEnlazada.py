class Nodo:
    def __init__(self,dato,prox=None,ant=None):
        self.dato=dato
        self.prox=prox
        self.ant=ant

class ListaDoble:
    def __init__(self):
        """Crea una lista doble enlazada vacía"""
        self.prim = None
        self.len = 0
    def append(self,dato):
        """Agrega un nodo al final de la lista"""
        if self.len == 0:
            self.prim = Nodo(dato)
        else:
            nodo = self.prim
            while nodo.prox!=None:
                nodo = nodo.prox'
            nodo.prox = Nodo(dato)
    def insert(self,dato,pos)
        """Recibe un dato y una posición e inserta el nodo en la posición correspondiente"""
        if pos == self.len:
            self.append(dato)
        else:
            for i in range(pos-1):
                nodo = nodo.prox
            anterior = nodo
            prox = nodo.prox
            nodo_nuevo = Nodo(dato,prox,anterior)
    def pop(self,pos):
        """Recibe una posición, elimina el nodo que se encuentra ahí y devuelve el dato"""
        nodo = self.prim
        if pos==0:
            dato = nodo.dato
            nodo_sig = nodo.prox
            nodo_sig.ant = None
            self.prim = nodo_sig
        elif pos == self.len-1:
            while nodo.prox!=None:
                nodo = nodo.prox
            dato = nodo.dato
            nodo_anterior = nodo.ant
            nodo_anterior = None
        else:
            for i in range(pos-1):
                nodo = nodo.prox
            dato = nodo.prox.dato
            nodo_siguiente = nodo.prox.prox
            nodo_siguiente.ant = nodo
            nodo.prox = nodo_siguiente
        return dato
