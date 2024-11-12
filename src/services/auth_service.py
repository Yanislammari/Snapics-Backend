import bcrypt
import jwt
import datetime
import os
from dotenv import load_dotenv
from src.models.user import User
from src.repositories.user_repository import UserRepository
from src.utils.config import db

load_dotenv()


class AuthService:
    SECRET_KEY = os.getenv("SECRET_KEY")

    @staticmethod
    def register(username: str, mail: str, password: str):
        if UserRepository.get_user_by_email(mail):
            raise ValueError("Email already registered")
        if UserRepository.get_user_by_username(username):
            raise ValueError("Username already registered")

        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode('utf-8')
        new_user = User(username=username, mail=mail, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def login(email: str, password: str):
        user = UserRepository.get_user_by_email(email)

        if not user:
            raise ValueError("Invalid email")
        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            raise ValueError("Incorrect password")

        token = AuthService.generate_jwt_token(user.id)
        return token

    @staticmethod
    def generate_jwt_token(user_id: str):
        expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        token = jwt.encode({
            'user_id': str(user_id),
            'exp': expiration
        }, AuthService.SECRET_KEY, algorithm='HS256')
        return token

    @staticmethod
    def verify_jwt_token(token: str):
        try:
            payload = jwt.decode(token, AuthService.SECRET_KEY, algorithms=['HS256'])
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired")
        except jwt.InvalidTokenError:
            raise ValueError("Invalid token")
