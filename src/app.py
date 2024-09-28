"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Personaje, Planeta, Vehiculo, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# @app.route('/user', methods=['GET'])
# def handle_hello():

#     users = User.query.all()
#     usuarios_serializados = [ persona.serialize() for persona in users  ]
#     return jsonify(usuarios_serializados), 200


# @app.route('/user', methods=['POST'])
# def add_user():
#     body = request.json
    
#     name = body.get('name',None)
#     last_name = body.get('last_name',None)
#     email = body.get('email',None)
#     password = body.get('password', None)

#     try:
#         new_user = User(name = name, last_name = last_name, email = email, password = password, is_active = True )

#         db.session.add(new_user) 
#         db.session.commit()

#         return jsonify({"msg":"success"}), 201
    
#     except:
#         return jsonify({"Error":"Something happened"}), 500
    

# @app.route('/user/<int:id>', methods=['DELETE'])
# def remove_user(id):
#     searched_user = User.query.filter_by(id = id).one_or_none()

#     if searched_user != None:
#         db.session.delete(searched_user)
#         db.session.commit()
#         return jsonify(searched_user.serialize()),200
#     else:
#         return jsonify({"error": f"User with id: {id} not found!"}), 404

# @app.route('/user/<int:id>' , methods=['PUT'])
# def edit_user(id):
#     searched_user = User.query.filter_by(id = id).one_or_none()

#     body = request.json
#     new_name = body.get('name', None)
#     new_last_name = body.get('last_name', None)
#     new_password = body.get('password', None)

#     if searched_user != None:

#         if new_name != None:
#             searched_user.name = new_name
#         if new_last_name != None:
#             searched_user.last_name = new_last_name
#         if new_password != None:
#             searched_user.password = new_password

#         db.session.commit()

#         return jsonify(searched_user.serialize(),200)
#     else:
#         return jsonify({"error": f"User with id: {id} not found!"}), 404


#
#
#ENDPOINTS DEL PROYECTO:
#
#

#POST USER
@app.route('/user', methods=['POST'])
def add_user():
    body = request.json
    
    name = body.get('name',None)
    last_name = body.get('last_name',None)
    email = body.get('email',None)
    password = body.get('password', None)

    try:
        new_user = User(name = name, last_name = last_name, email = email, password = password, is_active = True )

        db.session.add(new_user) 
        db.session.commit()

        return jsonify({"msg":"success"}), 201
    
    except:
        return jsonify({"Error":"Something happened"}), 500


#POST VEHICULOS
@app.route('/vehiculo', methods=['POST'])
def add_vehiculo():
    body = request.json

    name = body.get('name',None)
    marca = body.get('marca',None)
    capacidad = body.get('capacidad',None)
    pasajeros = body.get('pasajeros', None)
    tripulacion = body.get('tripulacion', None)
    modelo = body.get('modelo', None)

    try:
        new_vehiculo = User(name = name, marca = marca, capacidad = capacidad, pasajeros = pasajeros,
                         tripulacion = tripulacion, modelo = modelo )

        db.session.add(new_vehiculo) 
        db.session.commit()

        return jsonify({"msg":"success"}), 201
    
    except:
        return jsonify({"Error":"Something happened"}), 500


#POST PERSONAJES
@app.route('/personaje', methods=['POST'])
def add_personaje():
    body = request.json
    
    name = body.get('name',None)
    planeta_origen = body.get('planeta_origen',None)
    altura = body.get('altura',None)
    unidades_altura = body.get('unidades_altura',None)
    peso = body.get('peso',None)
    unidades_peso = body.get('unidades_peso',None)

    try:
        new_personaje = Personaje(name = name, planeta_origen = planeta_origen, altura = altura, 
                                unidades_altura = unidades_altura, peso = peso, unidades_peso = unidades_peso )

        db.session.add(new_personaje) 
        db.session.commit()

        return jsonify({"msg":"success"}), 201
    
    except:
        return jsonify({"Error":"Something happened"}), 500

#POST PLANETAS
@app.route('/planeta', methods=['POST'])
def add_planeta():
    body = request.json
    
    name = body.get('name',None)
    clima = body.get('clima',None)
    diametro = body.get('diametro',None)
    poblacion = body.get('poblacion',None)

    try:
        new_planeta = Planeta(name = name, clima = clima, diametro = diametro, poblacion = poblacion )

        db.session.add(new_planeta) 
        db.session.commit()

        return jsonify({"msg":"success"}), 201
    
    except:
        return jsonify({"Error":"Something happened"}), 500

# [GET] /people Get a list of all the people in the database.
@app.route('/personaje', methods=['GET'])
def get_personajes():
    personajes = Personaje.query.all()
    personajes_serializados = [ personaje.serialize() for personaje in personajes ]
    return jsonify(personajes_serializados), 200

# [GET] /people/<int:people_id> Get one single person's information.
@app.route('/personaje/<int:id>', methods=['GET'])
def get_personaje():
    searched_personaje = Personaje.query.filter_by(id = id).one_or_none()
    return jsonify(searched_personaje.serialize()), 200

# [GET] /planets Get a list of all the planets in the database.
@app.route('/planeta', methods=['GET'])
def get_planetas():
    planetas = Planeta.query.all()
    planetas_serializados = [ planeta.serialize() for planeta in planetas ]
    return jsonify(planetas_serializados), 200

# [GET] /planets/<int:planet_id> 
@app.route('/planeta/<int:id>', methods=['GET'])
def get_planeta():  #verificar si se pone ID en parametro
    searched_planeta = Planeta.query.filter_by(id = id).one_or_none()
    return jsonify(searched_planeta.serialize()), 200

# [GET] /users Get a list of all the blog post users.
@app.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()
    usuarios_serializados = [ usuario.serialize() for usuario in users  ]
    return jsonify(usuarios_serializados), 200

# [GET] /users/favorites Get all the favorites that belong to the current user.
@app.route('/user/<int:id>/favorite', methods = ['GET'])
def get_users_favorites(id):
    user_favorites = Favorites.query.filter_by(user = id).one_or_none()  
    return jsonify(user_favorites.serialize()),200

# [POST] /favorite/planet/<int:planet_id> Add a new favorite planet to the current user with the planet id = planet_id.
@app.route('/user/<int:id>/favorite/planet/<int:planet_id>', methods = ["POST"])
def add_planeta_favorite(id, planeta_id):
    try:
        new_favorite_planet = Favorites(user = id, planeta = planeta_id)

        db.session.add(new_favorite_planet) 
        db.session.commit()

        return jsonify({"msg":"success"}), 201
    
    except:
        return jsonify({"Error":"Something happened"}), 500


# [POST] /favorite/people/<int:people_id> Add new favorite people to the current user with the people id = people_id.
@app.route('/user/<int:id>/favorite/personaje/<int:personaje_id>', methods = ["POST"])
def add_personaje_favorite(id, personaje_id):
    try:
        new_favorite_personaje = Favorites(user = id, personaje = personaje_id)

        db.session.add(new_favorite_personaje) 
        db.session.commit()

        return jsonify({"msg":"success"}), 201
    
    except:
        return jsonify({"Error":"Something happened"}), 500

# [DELETE] /favorite/planet/<int:planet_id> Delete a favorite planet with the id = planet_id.
@app.route('/user/<int:id>/favorite/planeta/<int:planeta_id>', methods=['DELETE'])
def remove_favorite_planeta(id, planeta_id):
    searched_favorite_planet = Favorites(user = id, planeta = planeta_id)

    if searched_favorite_planet != None:
        db.session.delete(searched_favorite_planet)
        db.session.commit()
        return jsonify(searched_favorite_planet.serialize()),200
    else:
        return jsonify({"error": f"User with id: {id} or Planet with id: {planeta_id} not found!"}), 404

# [DELETE] /favorite/people/<int:people_id> Delete a favorite people with the id = people_id.
@app.route('/user/<int:id>/favorite/planeta/<int:planeta_id>', methods=['DELETE'])
def remove_favorite_personaje(id, personaje_id):
    searched_favorite_personaje = Favorites(user = id, personaje = personaje_id)

    if searched_favorite_personaje != None:
        db.session.delete(searched_favorite_personaje)
        db.session.commit()
        return jsonify(searched_favorite_personaje.serialize()),200
    else:
        return jsonify({"error": f"User with id: {id} or Character with id: {personaje_id} not found!"}), 404

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
