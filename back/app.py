from flask import Flask, jsonify
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
