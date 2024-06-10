from flask import Blueprint, request, jsonify
api = Blueprint('api', __name__)

from models import db, People, User

#OPERACIONES DE CHARACTERS

@api.route('/people', methods=['GET'])
def get_characters():
    characters= People.query.all()
    return jsonify(characters), 200

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
    return jsonify(users), 200
