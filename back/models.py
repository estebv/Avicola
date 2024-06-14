from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Galpon(db.Model):
    __tablename__ = 'galpon'
    
    id_galpon = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero_Galpon = db.Column(db.Integer)
    numero_aves = db.Column(db.Integer)

    condiciones_ambientales = db.relationship('CondicionesAmbientales', backref='galpon', lazy=True)
    aves = db.relationship('Ave', backref='galpon', lazy=True)
    mortalidades = db.relationship('Mortalidad', backref='galpon', lazy=True)
    pesajes = db.relationship('Pesaje', backref='galpon', lazy=True)
    vacunaciones = db.relationship('Vacunacion', backref='galpon', lazy=True)
    huevos = db.relationship('Huevos', backref='galpon', lazy=True)
    alimentos = db.relationship('Alimentos', backref='galpon', lazy=True)

class CondicionesAmbientales(db.Model):
    __tablename__ = 'CondicionesAmbientales'

    id_CondicionesAmbientales = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.Date, nullable=False)
    temperatura = db.Column(db.Numeric(5, 2))
    humedad = db.Column(db.Numeric(5, 2))
    ventilacion = db.Column(db.String(50))
    iluminacion = db.Column(db.String(50))
    id_galpon = db.Column(db.Integer, db.ForeignKey('galpon.id_galpon'))

class Ave(db.Model):
    __tablename__ = 'aves'

    ave_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    raza = db.Column(db.String(255))
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    fecha_llegada = db.Column(db.Date, nullable=False)
    origen = db.Column(db.String(255), nullable=False)
    total_aves = db.Column(db.Integer)
    id_galpon = db.Column(db.Integer, db.ForeignKey('galpon.id_galpon'))

class Mortalidad(db.Model):
    __tablename__ = 'mortalidad'

    mortalidad_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_muerte = db.Column(db.Date)
    causa_muerte = db.Column(db.String(255))
    numero_aves = db.Column(db.Integer)
    id_galpon = db.Column(db.Integer, db.ForeignKey('galpon.id_galpon'))

class Pesaje(db.Model):
    __tablename__ = 'pesaje'

    pesaje_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero_ave = db.Column(db.Integer)
    estado_salud = db.Column(db.String(255), nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    fecha_Pesaje = db.Column(db.Date, nullable=False)
    id_galpon = db.Column(db.Integer, db.ForeignKey('galpon.id_galpon'))

class Vacunacion(db.Model):
    __tablename__ = 'vacunacion'

    vacunacion_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_Vacuna = db.Column(db.String(255), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    id_galpon = db.Column(db.Integer, db.ForeignKey('galpon.id_galpon'))

class Huevos(db.Model):
    __tablename__ = 'huevos'

    huevo_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_puesta = db.Column(db.Date, nullable=False)
    peso_huevo = db.Column(db.Numeric(5, 2), nullable=False)
    calidad_huevo = db.Column(db.Integer, nullable=False)
    total_huevo = db.Column(db.Integer, nullable=False)
    id_galpon = db.Column(db.Integer, db.ForeignKey('galpon.id_galpon'))

class Alimentos(db.Model):
    __tablename__ = 'alimentos'

    alimento_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    marca_Alimento = db.Column(db.String(255), nullable=False)
    etapa_alimento = db.Column(db.String(255), nullable=False)
    fecha_consumo = db.Column(db.Date, nullable=False)
    cantidad_kg = db.Column(db.Integer, nullable=False)
    id_galpon = db.Column(db.Integer, db.ForeignKey('galpon.id_galpon'))

class Clima(db.Model):
    __tablename__ = 'Clima'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.Date, nullable=False)
    temperatura = db.Column(db.Numeric(5, 2))
    precipitacion = db.Column(db.Numeric(5, 2))
