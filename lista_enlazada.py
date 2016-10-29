class Nodo:
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox
    def __str__(self):
        return str(self.dato)

class ListaEnlazada:
    def __init__(self):
        self.prim = None
        self.len = 0
    def __str__(self):
        r = "["
        act = self.prim
        while act:
            r = r + str(act.dato) + ","
        return r + "]"
    def __len__(self):
        return self.len
    def pop(self, i=None):
        if i is None:
            i = self.len - 1
        if i<0 or i>=self.len:
            raise IndexException("Índice fuera de rango")
        if i == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range(1,i):
                n_ant = n_act
                n_act = n_ant.prox
        dato = n_act.dato
        n_ant.prox = n_act.prox
        self.len = self.len - 1
        return dato
    def __iter__(self):
        return _IteradorListaEnlazada(self.prim)
    def append(self,dato):
        nodo_nuevo = Nodo(dato)
        nodo = self.prim
        if nodo == None:
            self.prim = nodo_nuevo
        else:
            while nodo.prox is not None:
                nodo = nodo.prox
            nodo.prox = nodo_nuevo
        self.len = self.len + 1
    def extend(self,otro):
        nodo = otro.prim
        while nodo!=None:
            self.append(nodo.dato)
            nodo = nodo.prox

class _IteradorListaEnlazada:
    def __init__(self,prim):
        self.actual = prim
    def __next__(self):
        if self.actual is None:
            raise StopIteration
        dato = self.prim.dato
        self.actual = self.actual.prox
        return dato
    def __str__(self):
        return str(self.actual.dato)
