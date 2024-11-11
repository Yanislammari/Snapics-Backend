import uuid
from src.utils.config import db
from sqlalchemy.dialects.postgresql import UUID


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4(), unique=True, nullable=False)
    username = db.Column(db.String(10), unique=True, nullable=False)
    mail = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return (
            f"<User id: {self.id}, "
            f"username: {self.username}, "
            f"mail: {self.mail}"
        )
