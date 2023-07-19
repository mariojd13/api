from flask_restful import Resource, reqparse
from models import Cliente
from data import clientes_data

parser = reqparse.RequestParser()
parser.add_argument('nombre', type=str, required=True, help='El nombre del cliente es requerido.')
parser.add_argument('email', type=str, required=True, help='El email del cliente es requerido.')

class ClientesResource(Resource):
    def get(self, cliente_id=None):
        if cliente_id:
            cliente = next((c for c in clientes_data if c.id == cliente_id), None)
            if cliente:
                return cliente.__dict__
            else:
                return {'message': 'Cliente no encontrado'}, 404
        else:
            return [c.__dict__ for c in clientes_data]

    def post(self):
        args = parser.parse_args()
        cliente = Cliente(id=len(clientes_data) + 1, **args)
        clientes_data.append(cliente)
        return cliente.__dict__, 201

    def put(self, cliente_id):
        cliente = next((c for c in clientes_data if c.id == cliente_id), None)
        if cliente:
            args = parser.parse_args()
            cliente.nombre = args['nombre']
            cliente.email = args['email']
            return cliente.__dict__
        else:
            return {'message': 'Cliente no encontrado'}, 404

    def delete(self, cliente_id):
        global clientes_data
        clientes_data = [c for c in clientes_data if c.id != cliente_id]
        return {'message': 'Cliente eliminado satisfactoriamente'}
