

from flask import Blueprint

# Importa los blueprints de cada archivo individual de rutas
from .galpon_routes import galpon_blueprint
from .condiciones_ambientales_routes import condiciones_blueprint
from .ave_routes import aves_blueprint
from .mortalidad_routes import mortalidad_blueprint
from .pesaje_routes import pesaje_blueprint
from .vacunacion_routes import vacunacion_blueprint
from .huevos_routes import huevos_blueprint
from .alimentos_routes import alimentos_blueprint
from .clima_routes import clima_blueprint

# Define una lista de blueprints para exportar (opcional)
blueprints_list = [
    galpon_blueprint,
    condiciones_blueprint,
    aves_blueprint,
    mortalidad_blueprint,
    pesaje_blueprint,
    vacunacion_blueprint,
    huevos_blueprint,
    alimentos_blueprint,
    clima_blueprint
]

def register_blueprints(app):
    """
    Registra todos los blueprints en la aplicación Flask.

    Args:
        app (Flask): La aplicación Flask en la cual se registrarán los blueprints.

    Returns:
        None
    """
    for blueprint in blueprints_list:
        app.register_blueprint(blueprint)

# Exporta la función para registrar blueprints
__all__ = ['register_blueprints']
