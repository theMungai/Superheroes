from flask import Blueprint, request, jsonify
from app.models import db, Hero, Power, HeroPower
from sqlalchemy.exc import IntegrityError

api = Blueprint('api', __name__)


@api.route('/heroes')
def get_heroes():
    return jsonify([hero.to_dict() for hero in Hero.query.all()])


@api.route('/heroes/<int:id>')
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero.to_dict())
    return jsonify({"error": "Hero not found"}), 404


@api.route('/powers')
def get_powers():
    return jsonify([power.to_dict() for power in Power.query.all()])


@api.route('/powers/<int:id>', methods=['GET', 'PATCH'])
def power_detail(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    if request.method == 'GET':
        return jsonify(power.to_dict())

    try:
        data = request.get_json()
        power.description = data.get("description", power.description)
        db.session.commit()
        return jsonify(power.to_dict())
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400


@api.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    try:
        hp = HeroPower(
            strength=data["strength"],
            power_id=data["power_id"],
            hero_id=data["hero_id"]
        )
        db.session.add(hp)
        db.session.commit()
        return jsonify(hp.to_dict()), 201
    except (ValueError, IntegrityError) as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400
