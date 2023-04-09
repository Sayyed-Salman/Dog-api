from flask import Blueprint
from flask import request, jsonify
from app.models.Dog import Dog, DogSchema
from app import db

api_bp = Blueprint('api', __name__)


@api_bp.route('/dogs', methods=['GET'])
def get_dogs():
    schema = DogSchema(many=True)
    return jsonify(schema.dump(Dog.query.all())), 200


@api_bp.route('/add_dog', methods=['POST'])
def add_dog():
    dog = DogSchema().load(request.get_json())
    db.session.add(dog)
    db.session.commit()
    return "", 201
