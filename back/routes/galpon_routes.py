#delete this file
from flask import Blueprint, jsonify, request
from models import db, Galpon

galpon_blueprint = Blueprint('galpon_blueprint', __name__)

@galpon_blueprint.route('/api/galpon', methods=['GET'])
def get_galpones():
    galpones = Galpon.query.all()
    return jsonify([galpon.serialize() for galpon in galpones])

@galpon_blueprint.route('/api/galpon/<int:id_galpon>', methods=['GET'])
def get_galpon(id_galpon):
    galpon = Galpon.query.get(id_galpon)
    if not galpon:
        return jsonify({"error": "Galpon no encontrado"}), 404
    return jsonify(galpon.serialize())

@galpon_blueprint.route('/api/galpon', methods=['POST'])
def add_galpon():
    data = request.get_json()
    nuevo_galpon = Galpon(
        numero_Galpon=data['numero_Galpon'],
        numero_aves=data['numero_aves']
    )
    db.session.add(nuevo_galpon)
    db.session.commit()
    return jsonify({"message": "Galpon añadido exitosamente"}), 201

@galpon_blueprint.route('/api/galpon/<int:id_galpon>', methods=['PATCH'])
def update_galpon(id_galpon):
    galpon = Galpon.query.get(id_galpon)
    if not galpon:
        return jsonify({"error": "Galpon no encontrado"}), 404

    data = request.get_json()
    
    if 'numero_Galpon' in data:
        galpon.numero_Galpon = data['numero_Galpon']
    
    if 'numero_aves' in data:
        galpon.numero_aves = data['numero_aves']

    db.session.commit()
    return jsonify({"message": "Galpon actualizado exitosamente"}), 200

@galpon_blueprint.route('/api/galpon/<int:id_galpon>', methods=['DELETE'])
def delete_galpon(id_galpon):
    galpon = Galpon.query.get(id_galpon)
    if not galpon:
        return jsonify({"error": "Galpon no encontrado"}), 404

    db.session.delete(galpon)
    db.session.commit()
    return jsonify({"message": "Galpon eliminado exitosamente"})
