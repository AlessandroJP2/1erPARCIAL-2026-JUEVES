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

    