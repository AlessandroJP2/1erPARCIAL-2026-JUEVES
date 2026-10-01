import datetime as d
from Ejercicio6 import ProductoKwikE
from Ejercicio7 import KwikEMart


class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)
    
    def agregar(self,elem):
        nuevo_nodo = Nodo(elem)
        if not self.header:
            self.header = nuevo_nodo
            return
        actual = self.header
        while actual.nxt:
            actual = actual.nxt
        actual.nxt = nuevo_nodo
        
    def mostrar(self):
        actual = self.header
        elementos = []
        while actual:
            elementos.append(actual.elem)
            actual = actual.next
        print("Elementos de la lista:", elementos)
        
Market = KwikEMart()
Market.agregar(ProductoKwikE("Caramelo", 1, d.date(2027,6,30), 10.0, 100, "Snacks"))

Lista = ListaEnlazada()
