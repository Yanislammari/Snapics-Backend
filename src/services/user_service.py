from src.repositories.user_repository import UserRepository


class UserService:
    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()

    @staticmethod
    def get_user_by_id(user_id: str):
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    @staticmethod
    def get_user_by_email(mail: str):
        user = UserRepository.get_user_by_email(mail)
        if not user:
            raise ValueError("User not found")
        return user

    @staticmethod
    def get_user_by_username(username: str):
        user = UserRepository.get_user_by_username(username)
        if not user:
            raise ValueError("User not found")
        return user

    @staticmethod
    def set_user_by_id(user_id: str, data: dict):
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        updated_user = UserRepository.set_user_by_id(user_id, data)
        if not updated_user:
            raise ValueError("Error updating user")

        return updated_user

    @staticmethod
    def delete_user_by_id(user_id: str):
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        UserRepository.delete_user_by_id(user_id)
