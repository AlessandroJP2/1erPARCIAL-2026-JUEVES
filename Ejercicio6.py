import datetime as d

class ProductoKwikE:
    def __init__(self, descripcion : str, id_producto : int,
                    fecha_vencimiento : d.date, precio : float,
                    stock: int, categoria: str):
    
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

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
        elif detalle == self.categoria:
            self.categoria = str(input("Ingrese la nueva categoria:"))
            return print(f"La nueva categoria del producto es {self.categoria}")

    def modificar_stock(self):
        if self.fecha_vencimiento < d.date.today():
            self.stock = 0
            return print("El producto ha vencido")
        else:
            return print("El producto no ha vencido")
    def __str__(self):
        return f"Producto: {self.descripcion}, ID: {self.id_producto}, Precio: {self.precio}, stock: {self.stock}, Fecha de vencimiento: {self.fecha_vencimiento}"

    def __eq__(self,other):
        if (other.id_producto == self.id_producto) and (other.descripcion == self.descripcion):
            return f"Los productos son iguales"
        else:
            return f"Los productos no son iguales"

caramelo = ProductoKwikE("Caramelo", 1, d.date(2027,6,30), 10.0, 100, "Snacks")
pelota = ProductoKwikE("pelota", 1, d.date(2027,6,30), 10.0, 100, "Conveniencia")

print(caramelo)

print(caramelo == pelota)