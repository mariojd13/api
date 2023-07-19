from models import Producto, Cliente, Factura, Inventario

# Datos provisionales para cada tabla
productos_data = [
    Producto(id=1, nombre='Anillo de oro', precio=250.0, descripcion='Anillo de oro de 18 quilates'),
    Producto(id=2, nombre='Collar de plata', precio=120.0, descripcion='Collar de plata 925'),
    # Agrega más productos aquí
]

clientes_data = [
    Cliente(id=1, nombre='John Doe', email='john@example.com'),
    Cliente(id=2, nombre='Jane Smith', email='jane@example.com'),
    # Agrega más clientes aquí
]

facturas_data = [
    Factura(id=1, cliente_id=1, fecha='2023-07-18', total=370.0),
    Factura(id=2, cliente_id=2, fecha='2023-07-17', total=120.0),
    # Agrega más facturas aquí
]

inventario_data = [
    Inventario(id=1, producto_id=1, cantidad=10),
    Inventario(id=2, producto_id=2, cantidad=5),
    # Agrega más inventario aquí
]
