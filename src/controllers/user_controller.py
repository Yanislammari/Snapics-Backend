from flask import Blueprint, request, jsonify, abort
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


@user_blueprint.route("/users/<string:id>", methods=["PUT"])
def update_user(id):
    if not UserService.get_user_by_id(id):
        abort(404, description="User not found.")

    data = request.get_json()
    if not data:
        abort(400, description="No data provided.")

    try:
        updated_user = UserService.set_user_by_id(id, data)
    except ValueError as e:
        abort(400, description=str(e))

    return jsonify({
        "id": str(updated_user.id),
        "username": updated_user.username,
        "mail": updated_user.mail,
        "password": updated_user.password
    })
