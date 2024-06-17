from flask import Flask, jsonify,request
from flask_cors import CORS
from config import Config
from models import db
from routes import register_blueprints

# Crear instancia de Flask
app = Flask(__name__)
app.config.from_object(Config)

# Configurar SQLAlchemy
db.init_app(app)

# Configurar CORS para permitir todas las rutas desde localhost:3000
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Registrar blueprints
register_blueprints(app)

# rutas
@app.route('/')
def index():
    return 'Hola, esta es la API para la base de datos de aves.'

if __name__ == '__main__':
    app.run(debug=True)

# Ruta de ejemplo para recibir solicitudes POST
# @app.route('/api/galpon', methods=['POST'])
#def handle_post_request():
 #   data = request.json  # Obtener los datos JSON de la solicitud
    # Aquí puedes procesar los datos como desees
#    return jsonify({"message": "Solicitud recibida correctamente", "data": data}), 200

# Ruta de ejemplo para recibir solicitudes GET
#@app.route('/api/galpon', methods=['GET'])
#def handle_get_request():
    # Aquí puedes devolver datos o realizar otras acciones
#    return jsonify({"message": "Solicitud GET recibida correctamente"}), 200
#