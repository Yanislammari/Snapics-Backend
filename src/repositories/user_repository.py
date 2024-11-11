from src.models.user import User
from src.utils.config import db


class UserRepository:
    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id: str):
        return User.query.get(user_id)

    @staticmethod
    def get_user_by_email(mail: str):
        return User.query.filter_by(mail=mail).first()

    @staticmethod
    def get_user_by_username(username: str):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def set_user_by_id(user_id: str, data: dict):
        user = User.query.get(user_id)
        if not user:
            return None

        if "username" in data:
            user.username = data["username"]
        if "mail" in data:
            user.mail = data["mail"]
        if "password" in data:
            user.password = data["password"]

        db.session.commit()
        return user

    @staticmethod
    def delete_user_by_id(user_id: str):
        User.query.filter_by(id=user_id).delete()
        db.session.commit()
