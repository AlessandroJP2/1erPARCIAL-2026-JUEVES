import datetime as d

class ProductoKwikE:
    def __init__(self, descripcion : str, id_producto : int,
                    fecha_vencimiento : d.date, precio : float,
                    stock: int):
    
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock

    def cambiar(self, detalle):
        if detalle == self.descripcion:
            self.descripcion = str(input("Ingrese la nueva descripcion:"))
            return print(f"La nueva descripcion del producto es {self.descripcion}")
        elif detalle == self.id_producto:
            self.id_producto = int(input("Ingrese el nuevo id:"))
            return print(f"El nuevo id del producto es {self.id_producto}")
        elif detalle == self.fecha_vencimiento:
            self.fecha_vencimiento = d.date(input("Ingrese la nueva fecha de vencimiento: "))
            return print(f"La nueva fecha de vencimiento del producto es {self.fecha_vencimiento}")
        elif detalle == self.precio:
            self.precio = float(input("Ingrese el nuevo precio: "))
            return print(f"El nuevo precio del producto es {self.precio}")
        elif detalle == self.stock:
            self.stock = int(input("Ingrese el nuevo stock:"))
            return print(f"El nuevo stock del producto es {self.stock}")

    def modificar_stock(self):
        if self.fecha_vencimiento < d.date.today():
            self.stock = 0
            return print("El producto ha vencido")
        else:
            return print("El producto no ha vencido")


caramelo = ProductoKwikE("Caramelo", 1, d.date(2027,6,30), 10.0, 100)

caramelo.cambiar(caramelo.id_producto)

caramelo.modificar_stock()
