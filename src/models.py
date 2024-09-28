from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable = False)
    email = db.Column(db.String(250), unique= True, nullable = False)
    password = db.Column(db.String(250), nullable = False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    # date = db.Column(db.Date, index = True)

    def __init__ (self, name, last_name, email, password, is_active):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_active = True

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Personaje(db.Model):
    __tablename__ = 'personaje'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), nullable = False)
    planeta_origen = db.Column(db.Integer, ForeignKey('planeta.id'))
    altura = db.Column(db.Float, nullable = False)
    unidades_altura = db.Column(db.String(250), nullable = False)
    peso = db.Column(db.Float, nullable = False)
    unidades_peso = db.Column(db.String(250), nullable = False)

    def __init__(self, id, name, planeta_origen, altura, unidades_altura, peso, unidades_peso):
        self.id = id
        self.name = name
        self.planeta_origen = planeta_origen
        self.altura = altura
        self.unidades_altura = unidades_altura
        self.peso = peso
        self.unidades_peso = unidades_peso

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }


class Planeta(db.Model):
    __tablename__ = 'planeta'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), nullable = False)
    clima = db.Column(db.String(250), nullable = False)
    diametro = db.Column(db.Float, nullable = False)
    poblacion = db.Column(db.Integer, nullable = False)

    def __init__(self, id, name, clima, diametro, poblacion):
        self.id = id
        self.name = name
        self.clima = clima
        self.diametro = diametro
        self.poblacion = poblacion

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }


class Vehiculo(db.Model):
    __tablename__ = 'vehiculo'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), nullable = False)
    marca = db.Column(db.String(250), nullable = False)
    capacidad = db.Column(db.Integer, nullable = False)
    pasajeros = db.Column(db.Integer, nullable = False)
    tripulacion = db.Column(db.Integer, nullable = False)
    modelo = db.Column(db.String(250), nullable = False)

    def __init__(self, id, name, marca, capacidad, pasajeros, tripulacion, modelo):
        self.id = id
        self.name = name
        self.marca = marca
        self.capacidad = capacidad 
        self.pasajeros = pasajeros
        self.tripulacion = tripulacion
        self.modelo = modelo

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }
  

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.Integer, ForeignKey('user.id'))
    personaje = db.Column(db.Integer, ForeignKey('personaje.id'))
    planeta = db.Column(db.Integer, ForeignKey('planeta.id'))
    vehiculo = db.Column(db.Integer, ForeignKey('vehiculo.id'))

    def __init__(self, id, user, personaje, planeta, vehiculo):
        self.id = id
        self.user = user
        self.personaje = personaje
        self.planeta = planeta
        self.vehiculo = vehiculo

    def serialize(self):
        return {
            "id" : self.id,
            "user": self.user,
            "personaje": self.personaje,
            "planeta" : self.planeta,
            "vehiculo": self.vehiculo,
            # do not serialize the password, its a security breach
        }