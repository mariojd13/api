from flask_restful import Resource, reqparse
from models import Producto
from data import productos_data

parser = reqparse.RequestParser()
parser.add_argument('nombre', type=str, required=True, help='El nombre del producto es requerido.')
parser.add_argument('precio', type=float, required=True, help='El precio del producto es requerido.')
parser.add_argument('descripcion', type=str)

class ProductosResource(Resource):
    def get(self, producto_id=None):
        if producto_id:
            producto = next((p for p in productos_data if p.id == producto_id), None)
            if producto:
                return producto.__dict__
            else:
                return {'message': 'Producto no encontrado'}, 404
        else:
            return [p.__dict__ for p in productos_data]

    def post(self):
        args = parser.parse_args()
        producto = Producto(id=len(productos_data) + 1, **args)
        productos_data.append(producto)
        return producto.__dict__, 201

    def put(self, producto_id):
        producto = next((p for p in productos_data if p.id == producto_id), None)
        if producto:
            args = parser.parse_args()
            producto.nombre = args['nombre']
            producto.precio = args['precio']
            producto.descripcion = args['descripcion']
            return producto.__dict__
        else:
            return {'message': 'Producto no encontrado'}, 404

    def delete(self, producto_id):
        global productos_data
        productos_data = [p for p in productos_data if p.id != producto_id]
        return {'message': 'Producto eliminado satisfactoriamente'}
