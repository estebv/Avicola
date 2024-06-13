from flask import Flask
from config import Config
from models import db, Galpon

app = Flask(__name__)
app.config.from_object(Config)

# Inicializa SQLAlchemy
db.init_app(app)

# Crea todas las tablas (esto solo debe usarse durante el desarrollo)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return "Hola, esta es la API para la base de datos de aves."

if __name__ == "__main__":
    app.run(debug=True)
