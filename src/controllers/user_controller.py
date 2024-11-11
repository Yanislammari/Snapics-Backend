from flask import Blueprint, jsonify, abort
from src.services.user_service import UserService

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/users", methods=["GET"])
def get_users():
    users = UserService.get_all_users()
    return jsonify([{
        "id": str(user.id),
        "username": user.username,
        "mail": user.mail,
        "password": user.password,
    } for user in users])


@user_blueprint.route("/users/<string:id>", methods=["GET"])
def get_user(id):
    try:
        user = UserService.get_user_by_id(id)
    except ValueError as e:
        abort(404, description=str(e))

    return jsonify({
        "id": str(user.id),
        "username": user.username,
        "mail": user.mail,
        "password": user.password
    })
