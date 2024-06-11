from flask import Blueprint, request, jsonify
api = Blueprint('api', __name__)

from models import db, People, Favorite_People, Planet, Favorite_Planet, User 

#OPERACIONES DE CHARACTERS

@api.route('/people', methods=['GET'])
def get_characters():
    characters= People.query.all()
    characters= list(map(lambda characters: characters.to_dict(), characters))
    return jsonify(characters), 200

@api.route('/people/<int:people_id>', methods=['GET'])
def get_people(people_id):
    people= People.query.filter_by(id= people_id).first()
    result= people.to_dict()
    return jsonify(result), 200


@api.route('/people', methods=['POST'])
def add_characters():
    datos = request.get_json()
    print(datos['name'])
    print(datos['url'])
    
    name = request.json.get('name')
    url = request.json.get('url')
    print(name)
    print(url)

    people= People()
    people.name= name
    people.url= url

    db.session.add(people)
    db.session.commit()

    return jsonify(people.to_dict()), 201

@api.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_people(people_id):
 
    user_id= 1
    favorites_people= Favorite_People()  
    favorites_people.user_id= user_id
    favorites_people.people_id= people_id

    db.session.add(favorites_people) 
    db.session.commit()
    return jsonify(favorites_people.to_dict()), 200

#OPERACIONES DE PLANETAS

@api.route('/planets', methods=['GET'])
def get_planets():
    planets= Planet.query.all()
    planets= list(map(lambda planets: planets.to_dict(), planets))
    return jsonify(planets), 200

@api.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet= Planet.query.filter_by(id= planet_id).first()
    result= planet.to_dict()
    return jsonify(result), 200

@api.route('/planet', methods=['POST'])
def add_planets():
    datos = request.get_json()
    print(datos['name'])
    print(datos['url'])
    
    name = request.json.get('name')
    url = request.json.get('url')
    print(name)
    print(url)

    planet= Planet()
    planet.name= name
    planet.url= url

    db.session.add(planet)
    db.session.commit()

    return jsonify(planet.to_dict()), 201

@api.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
 
    user_id= 1
    favorites_planets= Favorite_Planet()  
    favorites_planets.user_id= user_id
    favorites_planets.planet_id= planet_id

    db.session.add(favorites_planets) 
    db.session.commit()
    return jsonify(favorites_planets.to_dict()), 200

#OPERACIONES DE USUARIO

@api.route('/users', methods=['GET'])
def get_users():
    users= User.query.all()
    users= list(map(lambda users: users.to_dict(), users))
    return jsonify(users), 200

@api.route('/users/<username>/favorites', methods=['GET'])
def get_favorites_users(username):
    user= User.query.filter_by(username= username).first()
    result= user.to_dict()
    return jsonify(result), 200

@api.route('/user/favorites', methods=['GET'])
def user_favorites():
    user_id= 1
    favorites_planets= Favorite_Planet.query.filter_by(user_id= user_id)
    favorites_characters= Favorite_People.query.filter_by(user_id= user_id)
    results_planets= favorites_planets.to_dict()
    results_characters= favorites_characters.to_dict()

    return jsonify(results_planets, results_characters), 200