from flask import Blueprint, request, jsonify
api = Blueprint('api', __name__)

from models import db, People, User, Favorite_People

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
    favorites_users= Favorite_People.query.all()
    return jsonify(favorites_users), 200
