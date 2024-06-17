from flask import Blueprint, jsonify, request
from models import db, Vacunacion

vacunacion_blueprint = Blueprint('vacunacion_blueprint', __name__)

@vacunacion_blueprint.route('/vacunaciones', methods=['GET'])
def get_vacunaciones():
    vacunaciones = Vacunacion.query.all()
    return jsonify([vacunacion.serialize() for vacunacion in vacunaciones])

@vacunacion_blueprint.route('/vacunaciones/<int:id>', methods=['GET'])
def get_vacunacion(id):
    vacunacion = Vacunacion.query.get(id)
    if not vacunacion:
        return jsonify({"error": "Registro de vacunación no encontrado"}), 404
    return jsonify(vacunacion.serialize())

@vacunacion_blueprint.route('/api/vacunaciones', methods=['POST'])
def add_vacunacion():
    data = request.get_json()
    nueva_vacunacion = Vacunacion(
        nombre_Vacuna=data['nombre_Vacuna'],
        fecha=data['fecha'],
        id_galpon=data['id_galpon']
    )
    db.session.add(nueva_vacunacion)
    db.session.commit()
    return jsonify({"message": "Registro de vacunación añadido exitosamente"}), 201

@vacunacion_blueprint.route('/vacunaciones/<int:id>', methods=['PUT'])
def update_vacunacion(id):
    vacunacion = Vacunacion.query.get(id)
    if not vacunacion:
        return jsonify({"error": "Registro de vacunación no encontrado"}), 404

    data = request.get_json()
    vacunacion.nombre_Vacuna = data['nombre_Vacuna']
    vacunacion.fecha = data['fecha']
    vacunacion.id_galpon = data['id_galpon']

    db.session.commit()
    return jsonify({"message": "Registro de vacunación actualizado exitosamente"})

@vacunacion_blueprint.route('/vacunaciones/<int:id>', methods=['DELETE'])
def delete_vacunacion(id):
    vacunacion = Vacunacion.query.get(id)
    if not vacunacion:
        return jsonify({"error": "Registro de vacunación no encontrado"}), 404

    db.session.delete(vacunacion)
    db.session.commit()
    return jsonify({"message": "Registro de vacunación eliminado exitosamente"})
