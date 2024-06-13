from flask import Blueprint, jsonify, request
from models import db, Alimentos

alimentos_blueprint = Blueprint('alimentos_blueprint', __name__)

@alimentos_blueprint.route('/alimentos', methods=['GET'])
def get_alimentos():
    alimentos = Alimentos.query.all()
    return jsonify([alimento.serialize() for alimento in alimentos])

@alimentos_blueprint.route('/alimentos/<int:id>', methods=['GET'])
def get_alimento(id):
    alimento = Alimentos.query.get(id)
    if not alimento:
        return jsonify({"error": "Registro de alimento no encontrado"}), 404
    return jsonify(alimento.serialize())

@alimentos_blueprint.route('/alimentos', methods=['POST'])
def add_alimento():
    data = request.get_json()
    nuevo_alimento = Alimentos(
        marca_Alimento=data['marca_Alimento'],
        etapa_alimento=data['etapa_alimento'],
        fecha_consumo=data['fecha_consumo'],
        cantidad_kg=data['cantidad_kg'],
        id_galpon=data['id_galpon']
    )
    db.session.add(nuevo_alimento)
    db.session.commit()
    return jsonify({"message": "Registro de alimento añadido exitosamente"}), 201

@alimentos_blueprint.route('/alimentos/<int:id>', methods=['PUT'])
def update_alimento(id):
    alimento = Alimentos.query.get(id)
    if not alimento:
        return jsonify({"error": "Registro de alimento no encontrado"}), 404

    data = request.get_json()
    alimento.marca_Alimento = data['marca_Alimento']
    alimento.etapa_alimento = data['etapa_alimento']
    alimento.fecha_consumo = data['fecha_consumo']
    alimento.cantidad_kg = data['cantidad_kg']
    alimento.id_galpon = data['id_galpon']

    db.session.commit()
    return jsonify({"message": "Registro de alimento actualizado exitosamente"})

@alimentos_blueprint.route('/alimentos/<int:id>', methods=['DELETE'])
def delete_alimento(id):
    alimento = Alimentos.query.get(id)
    if not alimento:
        return jsonify({"error": "Registro de alimento no encontrado"}), 404

    db.session.delete(alimento)
    db.session.commit()
    return jsonify({"message": "Registro de alimento eliminado exitosamente"})
