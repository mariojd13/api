from database import connect_db

class Producto:
    def __init__(self, id, nombre, precio, descripcion):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

class Cliente:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

class Factura:
    def __init__(self, id, cliente_id, fecha, total):
        self.id = id
        self.cliente_id = cliente_id
        self.fecha = fecha
        self.total = total

class Inventario:
    def __init__(self, id, producto_id, cantidad):
        self.id = id
        self.producto_id = producto_id
        self.cantidad = cantidad
