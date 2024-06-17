from flask import Blueprint, jsonify, request
from models import db, Pesaje

pesaje_blueprint = Blueprint('pesaje_blueprint', __name__)

@pesaje_blueprint.route('/pesajes', methods=['GET'])
def get_pesajes():
    pesajes = Pesaje.query.all()
    return jsonify([pesaje.serialize() for pesaje in pesajes])

@pesaje_blueprint.route('/pesajes/<int:id>', methods=['GET'])
def get_pesaje(id):
    pesaje = Pesaje.query.get(id)
    if not pesaje:
        return jsonify({"error": "Registro de pesaje no encontrado"}), 404
    return jsonify(pesaje.serialize())

@pesaje_blueprint.route('/api/pesajes', methods=['POST'])
def add_pesaje():
    data = request.get_json()
    nuevo_pesaje = Pesaje(
        numero_ave=data['numero_ave'],
        estado_salud=data['estado_salud'],
        peso=data['peso'],
        fecha_Pesaje=data['fecha_Pesaje'],
        id_galpon=data['id_galpon']
    )
    db.session.add(nuevo_pesaje)
    db.session.commit()
    return jsonify({"message": "Registro de pesaje añadido exitosamente"}), 201

@pesaje_blueprint.route('/pesajes/<int:id>', methods=['PUT'])
def update_pesaje(id):
    pesaje = Pesaje.query.get(id)
    if not pesaje:
        return jsonify({"error": "Registro de pesaje no encontrado"}), 404

    data = request.get_json()
    pesaje.numero_ave = data['numero_ave']
    pesaje.estado_salud = data['estado_salud']
    pesaje.peso = data['peso']
    pesaje.fecha_Pesaje = data['fecha_Pesaje']
    pesaje.id_galpon = data['id_galpon']

    db.session.commit()
    return jsonify({"message": "Registro de pesaje actualizado exitosamente"})

@pesaje_blueprint.route('/pesajes/<int:id>', methods=['DELETE'])
def delete_pesaje(id):
    pesaje = Pesaje.query.get(id)
    if not pesaje:
        return jsonify({"error": "Registro de pesaje no encontrado"}), 404

    db.session.delete(pesaje)
    db.session.commit()
    return jsonify({"message": "Registro de pesaje eliminado exitosamente"})
