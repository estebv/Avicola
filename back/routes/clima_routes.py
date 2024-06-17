from flask import Blueprint, jsonify, request
from models import db, Clima

clima_blueprint = Blueprint('clima_blueprint', __name__)

@clima_blueprint.route('/api/clima', methods=['GET'])
def get_clima():
    clima = Clima.query.all()
    return jsonify([c.serialize() for c in clima])

@clima_blueprint.route('/clima/<int:id>', methods=['GET'])
def get_clima_by_id(id):
    clima = Clima.query.get(id)
    if not clima:
        return jsonify({"error": "Clima no encontrado"}), 404
    return jsonify(clima.serialize())

@clima_blueprint.route('/api/clima', methods=['POST'])
def add_clima():
    data = request.get_json()
    nuevo_clima = Clima(
        fecha=data['fecha'],
        temperatura=data['temperatura'],
        precipitacion=data['precipitacion']
    )
    db.session.add(nuevo_clima)
    db.session.commit()
    return jsonify({"message": "Registro de clima añadido exitosamente"}), 201

@clima_blueprint.route('/clima/<int:id>', methods=['PUT'])
def update_clima(id):
    clima = Clima.query.get(id)
    if not clima:
        return jsonify({"error": "Clima no encontrado"}), 404

    data = request.get_json()
    clima.fecha = data['fecha']
    clima.temperatura = data['temperatura']
    clima.precipitacion = data['precipitacion']

    db.session.commit()
    return jsonify({"message": "Clima actualizado exitosamente"})

@clima_blueprint.route('/clima/<int:id>', methods=['DELETE'])
def delete_clima(id):
    clima = Clima.query.get(id)
    if not clima:
        return jsonify({"error": "Clima no encontrado"}), 404

    db.session.delete(clima)
    db.session.commit()
    return jsonify({"message": "Clima eliminado exitosamente"})

