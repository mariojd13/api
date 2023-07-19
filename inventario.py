from flask_restful import Resource, reqparse
from models import Inventario
from data import inventario_data

parser = reqparse.RequestParser()
parser.add_argument('producto_id', type=int, required=True, help='El ID del producto es requerido.')
parser.add_argument('cantidad', type=int, required=True, help='La cantidad en inventario es requerida.')

class InventarioResource(Resource):
    def get(self, inventario_id=None):
        if inventario_id:
            inventario = next((inv for inv in inventario_data if inv.id == inventario_id), None)
            if inventario:
                return inventario.__dict__
            else:
                return {'message': 'Registro de inventario no encontrado'}, 404
        else:
            return [inv.__dict__ for inv in inventario_data]

    def post(self):
        args = parser.parse_args()
        inventario = Inventario(id=len(inventario_data) + 1, **args)
        inventario_data.append(inventario)
        return inventario.__dict__, 201

    def put(self, inventario_id):
        inventario = next((inv for inv in inventario_data if inv.id == inventario_id), None)
        if inventario:
            args = parser.parse_args()
            inventario.producto_id = args['producto_id']
            inventario.cantidad = args['cantidad']
            return inventario.__dict__
        else:
            return {'message': 'Registro de inventario no encontrado'}, 404

    def delete(self, inventario_id):
        global inventario_data
        inventario_data = [inv for inv in inventario_data if inv.id != inventario_id]
        return {'message': 'Registro de inventario eliminado satisfactoriamente'}
