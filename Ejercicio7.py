from Ejercicio6 import ProductoKwikE

class KwikEMart:
    def __init__(self, Bebidas = [], Snacks =[], Conveniencia = []):
        self.Bebidas = Bebidas
        self.Snacks = Snacks
        self.Conveniencia = Conveniencia
        
    def __add__(self,other):
        if other.categoria not in ["Bebidas", "Snacks", "Conveniencia"]:
            raise ValueError("La categoría del producto no es válida")
        elif other.categoria == "Bebidas":
            self.Bebidas.append(other)
            return self.Bebidas
        elif other.categoria == "Snacks":
            self.Snacks.append(other)
            return self.Snacks
        elif other.categoria == "Conveniencia":
            self.Conveniencia.append(other
            return self.Conveniencia
    
    def remover(self, producto):
        if producto not in self.Bebidas and producto not in self.Snacks and producto not in self.Conveniencia:
            raise ValueError("El producto no se encuentra en el stock")
        elif producto in self.Bebidas:
            self.Bebidas.remove(producto)
        elif producto in self.Snacks:
            self.Snacks.remove(producto)
        elif producto in self.Conveniencia:
            self.Conveniencia.remove(producto)
        return print(f"El producto {producto.descripcion} fue removido del stock")
