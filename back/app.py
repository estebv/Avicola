
from flask_cors import CORS
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from models import db


app = Flask(__name__)
app.config.from_object(Config)
CORS(app) 
 # Configura CORS para todas las rutas
db = SQLAlchemy(app)

# Aquí puedes definir tus modelos SQLAlchemy, por ejemplo:
# from models import User

@app.route('/')
def index():
    return 'Hola, esta es la API para la base de datos de aves.'

if __name__ == '__main__':
    app.run(debug=True)
