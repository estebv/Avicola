from flask import Blueprint, jsonify, request
from models import db, Mortalidad

mortalidad_blueprint = Blueprint('mortalidad_blueprint', __name__)

@mortalidad_blueprint.route('/mortalidades', methods=['GET'])
def get_mortalidades():
    mortalidades = Mortalidad.query.all()
    return jsonify([mortalidad.serialize() for mortalidad in mortalidades])

@mortalidad_blueprint.route('/mortalidades/<int:id>', methods=['GET'])
def get_mortalidad(id):
    mortalidad = Mortalidad.query.get(id)
    if not mortalidad:
        return jsonify({"error": "Registro de mortalidad no encontrado"}), 404
    return jsonify(mortalidad.serialize())

@mortalidad_blueprint.route('/mortalidades', methods=['POST'])
def add_mortalidad():
    data = request.get_json()
    nueva_mortalidad = Mortalidad(
        numero_galpon=data['numero_galpon'],
        estado_salud=data['estado_salud'],
        fecha_muerte=data['fecha_muerte'],
        causa_muerte=data['causa_muerte'],
        numero_aves=data['numero_aves'],
        id_galpon=data['id_galpon']
    )
    db.session.add(nueva_mortalidad)
    db.session.commit()
    return jsonify({"message": "Registro de mortalidad añadido exitosamente"}), 201

@mortalidad_blueprint.route('/mortalidades/<int:id>', methods=['PUT'])
def update_mortalidad(id):
    mortalidad = Mortalidad.query.get(id)
    if not mortalidad:
        return jsonify({"error": "Registro de mortalidad no encontrado"}), 404

    data = request.get_json()
    mortalidad.numero_galpon = data['numero_galpon']
    mortalidad.estado_salud = data['estado_salud']
    mortalidad.fecha_muerte = data['fecha_muerte']
    mortalidad.causa_muerte = data['causa_muerte']
    mortalidad.numero_aves = data['numero_aves']
    mortalidad.id_galpon = data['id_galpon']

    db.session.commit()
    return jsonify({"message": "Registro de mortalidad actualizado exitosamente"})

@mortalidad_blueprint.route('/mortalidades/<int:id>', methods=['DELETE'])
def delete_mortalidad(id):
    mortalidad = Mortalidad.query.get(id)
    if not mortalidad:
        return jsonify({"error": "Registro de mortalidad no encontrado"}), 404

   
