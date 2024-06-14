
from flask_cors import CORS
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
CORS(app) 

db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hola, esta es la API para la base de datos de aves.'

if __name__ == '__main__':
    app.run(debug=True)
