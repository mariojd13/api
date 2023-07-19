from flask_restful import Resource, reqparse
from models import Factura
from data import facturas_data

parser = reqparse.RequestParser()
parser.add_argument('cliente_id', type=int, required=True, help='El ID del cliente es requerido.')
parser.add_argument('fecha', type=str, required=True, help='La fecha de la factura es requerida.')
parser.add_argument('total', type=float, required=True, help='El total de la factura es requerido.')

class FacturasResource(Resource):
    def get(self, factura_id=None):
        if factura_id:
            factura = next((f for f in facturas_data if f.id == factura_id), None)
            if factura:
                return factura.__dict__
            else:
                return {'message': 'Factura no encontrada'}, 404
        else:
            return [f.__dict__ for f in facturas_data]

    def post(self):
        args = parser.parse_args()
        factura = Factura(id=len(facturas_data) + 1, **args)
        facturas_data.append(factura)
        return factura.__dict__, 201

    def put(self, factura_id):
        factura = next((f for f in facturas_data if f.id == factura_id), None)
        if factura:
            args = parser.parse_args()
            factura.cliente_id = args['cliente_id']
            factura.fecha = args['fecha']
            factura.total = args['total']
            return factura.__dict__
        else:
            return {'message': 'Factura no encontrada'}, 404

    def delete(self, factura_id):
        global facturas_data
        facturas_data = [f for f in facturas_data if f.id != factura_id]
        return {'message': 'Factura eliminada satisfactoriamente'}
