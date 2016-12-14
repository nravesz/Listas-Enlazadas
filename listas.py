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
		n_act = self.prim
		cadena = ""
		while n_act:
			cadena = cadena + str(n_act.dato) + ","
			n_act = n_act.prox
		cadena = cadena.rstrip(",")
		return "[{}]".format(cadena)
	
	def __len__(self):
		return self.len
	
	def pop(self,i=None):
		"""Elimina el nodo en la posición i y devuelve el dato contenido.
		Si i está fuera de rango, levanta la excepción IndexError.
		Si no se recibe la posición, devuelve el último elemento."""
		if i==None:
			i = self.len - 1
		elif i<0 or i>self.len:
			raise IndexError("Índice fuera de rango")
		elif i==0:
			# Caso particular: eliminar el primer elemento de la lista
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
	
	def insert(self,i,dato):
		"""Inserta un elemento en la posición i con el dato que recibe por parámetro"""
		if i < 0 or i > self.len:
			raise IndexError("Posición inválida")
		nuevo = Nodo(dato)
		if i == 0:
			nuevo.prox = self.prim
			self.prim = nuevo
		else:
			nodo = self.prim
			for pos in range(0,i-1):
				nodo = nodo.prox
			nuevo.prox = nodo.prox
			nodo.prox = nuevo
		self.len = self.len + 1

	def append(self,dato):
		nuevo = Nodo(dato)
		if not self.prim:
			self.prim = nuevo
		else:
			nodo = self.prim
			while nodo.prox != None:
				nodo = nodo.prox
			nodo.prox = nuevo
		self.len = self.len + 1
	
	def extend(self,otro):
		if not isinstance(otro, ListaEnlazada):
			raise TypeError("La lista debe ser extendida con otra lista")
		if not otro.prim:
			return
		if not self.prim:
			self.prim = otro.prim
		if not self.prim.prox:
			self.prim.prox = otro.prim
		else:
			nodo = self.prim
			while nodo.prox != None:
				nodo = nodo.prox
			nodo.prox = otro.prim
		self.len = self.len + otro.len

	def devolver_elemento(self,i):
		"""Recibe una posición como parámetro. Empieza a contar las posiciones desde el último elemento. Devuelve el dato contenido en el nodo de esa posición"""
		if i < 0 or i > self.len - 1:
			raise IndexError("Posición inválida")
		if i == 0:
			dato = self.prim.dato
		else:
			i = self.len - 1 - i
			nodo = self.prim
			for pos in range(0,i):
				nodo = nodo.prox
			dato = nodo.dato
		return dato
	
	def eliminar_posiciones(self,numeros):
		n_ant = self.prim
		n_act = n_ant.prox
		contador = 0
		for pos in range(1,self.len):
			if pos in numeros:
				n_ant.prox = n_act.prox
				contador += 1
			n_ant = n_act
			n_act = n_ant.prox
		if 0 in numeros:
			self.prim = self.prim.prox
		self.len -= contador

	def merge(self,otro):
		"""Recibe una otra lista enlazada como parámetro. Devuelve una nueva lista con TODOS los elementos de ambas ordenados
		Pre condición: elementos de ambas listas ordenados
		Pre condición: elementos de tipo int"""
		nueva = ListaEnlazada()
		n1 = self.prim
		n2 = otro.prim
		while not n1==None and not n2==None:
			if n1.dato<n2.dato:
				nueva.append(n1.dato)
				n1 = n1.prox
			elif n1.dato>n2.dato:
				nueva.append(n2.dato)
				n2 = n2.prox
			elif n1.dato==n2.dato:
				nueva.append(n1.dato)
				nueva.append(n2.dato)
				n1 = n1.prox
				n2 = n2.prox
		while n1==None and n2!=None:
			nueva.append(n2.dato)
			n2 = n2.prox
		while n2==None and n1!=None:
			nueva.append(n1.dato)
			n1 = n1.prox
		return nueva
	
	def downsample(self,k):
		"""Elimina los nodos que se encuentran en posiciones que no son múltiplo del número pasado por parametro"""
		if self.prim == None:
			return
		if k<1:
			raise ValueError
		n_ant = self.prim
		n_act = n_ant.prox
		contador = 0
		for i in range(1,self.len):
			if i%k!=0:
				n_ant.prox = n_act.prox
				contador += 1
			else:
				n_ant = n_act
			n_act = n_act.prox
		self.len -= contador
	
	def downsample1(self,k):
		if k<1:
			raise ValueError
		cont = 1
		ant = self.prim
		act = ant.prox
		while act:
			if cont%k!=0:
				ant.prox = act.prox
			else:
				ant = act
			cont += 1
			act = act.prox
	
	def invertir(self):
		if not self.prim:
			return
		if not self.prim.prox:
			return
		else:
			aux = Pila()
			nodo = self.prim
			while nodo:
				dato = nodo.dato
				aux.apilar(dato)
				nodo = nodo.prox
				self.prim = nodo
				self.len -= 1
			while not aux.esta_vacia():
				dato = aux.desapilar()
				nuevo = Nodo(dato)
				if not self.prim:
					self.prim = nuevo
				else:
					nodo = self.prim
					while nodo.prox != None:
						nodo = nodo.prox
					nodo.prox = nuevo
				self.len += 1

	def suma_acumulativa(self,i):
		if i > self.len - 1:
			raise IndexError
		else:
			contador = 0
			nodo = self.prim
			for pos in range(0,i):
				dato = nodo.dato
				contador += dato
				nodo = nodo.prox
			nodo.dato = contador
		
class Pila:
	def __init__(self):
		self.elementos = []
	
	def __str__(self):
		return str(self.elementos)
	
	def apilar(self,x):
		self.elementos.append(x)
	
	def desapilar(self):
		if self.elementos == 0:
			raise IndexError("La pila está vacía")
		return self.elementos.pop()
	
	def esta_vacia(self):
		return len(self.elementos) == 0
	
	def ver_primero(self):
		if len(self.elementos) == 0:
			return []
		return self.elementos[-1]
	
	def __len__(self):
		return len(self.elementos)


class Cola:

	def __init__(self):
		self.primero = None
		self.ultimo = None
	
	def __str__(self):
		n_act = self.primero
		cadena = ""
		while n_act:
			cadena = cadena + str(n_act.dato) + ","
			n_act = n_act.prox
		cadena = cadena.rstrip(",")
		return "[{}]".format(cadena)
	
	def encolar(self,x):
		nuevo = Nodo(x)
		if self.ultimo:
			self.ultimo.prox = nuevo
			self.ultimo = nuevo
		else:
			self.primero = nuevo
			self.ultimo = nuevo
	
	def desencolar(self):
		if not self.primero:
			raise ValueError("La cola está vacía")
		valor = self.primero.dato
		self.primero = self.primero.prox
		if not self.primero:
			self.ultimo = None
		return valor
	
	def esta_vacia(self):
		return self.primero == None