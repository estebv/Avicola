from flask import Blueprint, jsonify, request
from models import db, Huevos

huevos_blueprint = Blueprint('huevos_blueprint', __name__)

@huevos_blueprint.route('/api/huevos', methods=['GET'])
def get_huevos():
    huevos = Huevos.query.all()
    return jsonify([huevo.serialize() for huevo in huevos])

@huevos_blueprint.route('/api/huevos/<int:id>', methods=['GET'])
def get_huevo(id):
    huevo = Huevos.query.get(id)
    if not huevo:
        return jsonify({"error": "Registro de huevo no encontrado"}), 404
    return jsonify(huevo.serialize())

@huevos_blueprint.route('/api/huevos', methods=['POST'])
def add_huevo():
    data = request.get_json()
    nuevo_huevo = Huevos(
        fecha_puesta=data['fecha_puesta'],
        peso_huevo=data['peso_huevo'],
        calidad_huevo=data['calidad_huevo'],
        total_huevo=data['total_huevo'],
        id_galpon=data['id_galpon']
    )
    db.session.add(nuevo_huevo)
    db.session.commit()
    return jsonify({"message": "Registro de huevo añadido exitosamente"}), 201

@huevos_blueprint.route('/huevos/<int:id>', methods=['PUT'])
def update_huevo(id):
    huevo = Huevos.query.get(id)
    if not huevo:
        return jsonify({"error": "Registro de huevo no encontrado"}), 404

    data = request.get_json()
    huevo.fecha_puesta = data['fecha_puesta']
    huevo.peso_huevo = data['peso_huevo']
    huevo.calidad_huevo = data['calidad_huevo']
    huevo.total_huevo = data['total_huevo']
    huevo.id_galpon = data['id_galpon']

    db.session.commit()
    return jsonify({"message": "Registro de huevo actualizado exitosamente"})

@huevos_blueprint.route('/huevos/<int:id>', methods=['DELETE'])
def delete_huevo(id):
    huevo = Huevos.query.get(id)
    if not huevo:
        return jsonify({"error": "Registro de huevo no encontrado"}), 404

    db.session.delete(huevo)
    db.session.commit()
    return jsonify({"message": "Registro de huevo eliminado exitosamente"})
