from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'UTN@Tall3er'
api = Api(app)
jwt = JWTManager(app)

# Importamos los recursos para cada tabla
from productos import ProductosResource
from clientes import ClientesResource
from facturas import FacturasResource
from inventario import InventarioResource

# Agregamos los recursos a las rutas del API
api.add_resource(ProductosResource, '/productos',
                 '/productos/<int:producto_id>')
api.add_resource(ClientesResource, '/clientes', '/clientes/<int:cliente_id>')
api.add_resource(FacturasResource, '/facturas', '/facturas/<int:factura_id>')
api.add_resource(InventarioResource, '/inventario',
                 '/inventario/<int:inventario_id>')

if __name__ == '__main__':
  app.run(debug=True)
