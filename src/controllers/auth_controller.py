from flask import Blueprint, request, jsonify, abort
from src.services.auth_service import AuthService

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/auth/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    mail = data.get("mail")
    password = data.get("password")

    if not username or not mail or not password:
        abort(400, description="Missing required fields")
    try:
        user = AuthService.register(username, mail, password)
        return jsonify({
            "id": user.id,
            "username": user.username,
            "mail": user.mail
        }), 201
    except ValueError as e:
        abort(400, description=str(e))
