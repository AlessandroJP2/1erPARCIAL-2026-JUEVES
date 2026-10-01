from Ejercicio6 import ProductoKwikE

class KwikEMart:
    def __init__(self, Bebidas = [], Snacks =[], Conveniencia = []):
        self.Bebidas = Bebidas
        self.Snacks = Snacks
        self.Conveniencia = Conveniencia
        
    def agregar(self,producto):
        if producto.categoria not in ["Bebidas", "Snacks", "Conveniencia"]:
            raise ValueError("La categoría del producto no es válida")
        elif producto.categoria == "Bebidas":
            self.Bebidas.append(producto)
            self.actualizar_stock()
            return self.Bebidas
        elif producto.categoria == "Snacks":
            self.Snacks.append(producto)
            self.actualizar_stock()
            return self.Snacks
        elif producto.categoria == "Conveniencia":
            self.Conveniencia.append(producto)
            self.actualizar_stock()
            return self.Conveniencia
    
    def remover(self, producto):
        if producto not in self.Bebidas and producto not in self.Snacks and producto not in self.Conveniencia:
            raise ValueError("El producto no se encuentra en el pasillo")
        elif producto in self.Bebidas:
            self.Bebidas.remove(producto)
        elif producto in self.Snacks:
            self.Snacks.remove(producto)
        elif producto in self.Conveniencia:
            self.Conveniencia.remove(producto)
        self.actualizar_stock()
        
        return print(f"El producto {producto.descripcion} fue removido del pasillo")
    
    def remover_vencidos(self):
        if producto not in self.Bebidas and producto not in self.Snacks and producto not in self.Conveniencia:
            raise ValueError("El producto no está en el pasillo")
        else:
            for producto in self.Bebidas[:]:
                if producto.fecha_vencimiento.hour < 24:
                    self.Bebidas.remove(producto)
            for producto in self.Snacks[:]:
                if producto.fecha_vencimiento.hour < 24:
                    self.Snacks.remove(producto)
            for producto in self.Conveniencia[:]:
                if producto.fecha_vencimiento.hour < 24:
                    self.Conveniencia.remove(producto)
    
        return self.Bebidas, self.Snacks, self.Conveniencia

    def actualizar_stock(self, producto, stock):
        if self.agregar.id_producto == producto.id_producto:
            producto.stock += stock
        elif self.remover.id_producto == producto.id_producto:
            if producto.stock < 0:
                raise ValueError("El stock no puede ser negativo")
            else:
                producto.stock -= stock
        return print(f"El stock del producto {producto.descripcion} fue actualizado")
    

    
        
            