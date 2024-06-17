from flask import Blueprint, jsonify, request
from models import db, Ave


aves_blueprint = Blueprint('aves_blueprint', __name__)

@aves_blueprint.route('/api/aves', methods=['GET'])
def get_aves():
    aves = Ave.query.all()
    return jsonify([ave.serialize() for ave in aves])

@aves_blueprint.route('/aves/<int:id>', methods=['GET'])
def get_ave(id):
    ave = Ave.query.get(id)
    if not ave:
        return jsonify({"error": "Ave no encontrada"}), 404
    return jsonify(ave.serialize())

@aves_blueprint.route('/api/aves', methods=['POST'])
def add_ave():
    data = request.get_json()
    nueva_ave = Ave(
        raza=data['raza'],
        fecha_nacimiento=data['fecha_nacimiento'],
        fecha_llegada=data['fecha_llegada'],
        origen=data['origen'],
        total_aves=data['total_aves'],
        id_galpon=data['id_galpon']
    )
    db.session.add(nueva_ave)
    db.session.commit()
    return jsonify({"message": "Ave añadida exitosamente"}), 201

@aves_blueprint.route('/aves/<int:id>', methods=['PUT'])
def update_ave(id):
    ave = Ave.query.get(id)
    if not ave:
        return jsonify({"error": "Ave no encontrada"}), 404

    data = request.get_json()
    ave.raza = data['raza']
    ave.fecha_nacimiento = data['fecha_nacimiento']
    ave.fecha_llegada = data['fecha_llegada']
    ave.origen = data['origen']
    ave.total_aves = data['total_aves']
    ave.id_galpon = data['id_galpon']

    db.session.commit()
    return jsonify({"message": "Ave actualizada exitosamente"})

@aves_blueprint.route('/aves/<int:id>', methods=['DELETE'])
def delete_ave(id):
    ave = Ave.query.get(id)
    if not ave:
        return jsonify({"error": "Ave no encontrada"}), 404

    db.session.delete(ave)
    db.session.commit()
    return jsonify({"message": "Ave eliminada exitosamente"})
