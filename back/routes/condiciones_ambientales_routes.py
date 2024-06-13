from flask import Blueprint, jsonify, request
from models import db, CondicionesAmbientales

condiciones_blueprint = Blueprint('condiciones_blueprint', __name__)

@condiciones_blueprint.route('/condiciones', methods=['GET'])
def get_condiciones():
    condiciones = CondicionesAmbientales.query.all()
    return jsonify([condicion.serialize() for condicion in condiciones])

@condiciones_blueprint.route('/condiciones/<int:id>', methods=['GET']) 
def get_condicion(id):
    condicion = CondicionesAmbientales.query.get(id)
    if not condicion:
        return jsonify({"error": "Condiciones ambientales no encontradas"}), 404
    return jsonify(condicion.serialize())

@condiciones_blueprint.route('/condiciones', methods=['POST'])
def add_condicion():
    data = request.get_json()
    nueva_condicion = CondicionesAmbientales(
        fecha=data['fecha'],
        temperatura=data['temperatura'],
        humedad=data['humedad'],
        ventilacion=data['ventilacion'],
        iluminacion=data['iluminacion'],
        id_galpon=data['id_galpon']
    )
    db.session.add(nueva_condicion)
    db.session.commit()
    return jsonify({"message": "Condiciones ambientales añadidas exitosamente"}), 201

@condiciones_blueprint.route('/condiciones/<int:id>', methods=['PUT'])
def update_condicion(id):
    condicion = CondicionesAmbientales.query.get(id)
    if not condicion:
        return jsonify({"error": "Condiciones ambientales no encontradas"}), 404

    data = request.get_json()
    condicion.fecha = data['fecha']
    condicion.temperatura = data['temperatura']
    condicion.humedad = data['humedad']
    condicion.ventilacion = data['ventilacion']
    condicion.iluminacion = data['iluminacion']
    condicion.id_galpon = data['id_galpon']

    db.session.commit()
    return jsonify({"message": "Condiciones ambientales actualizadas exitosamente"})

@condiciones_blueprint.route('/condiciones/<int:id>', methods=['DELETE'])
def delete_condicion(id):
    condicion = CondicionesAmbientales.query.get(id)
    if not condicion:
        return jsonify({"error": "Condiciones ambientales no encontradas"}), 404

    db.session.delete(condicion)
    db.session.commit()
    return jsonify({"message": "Condiciones ambientales eliminadas exitosamente"})
