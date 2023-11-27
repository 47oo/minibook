# user_repository.py

from sqlalchemy.orm import Session
from models.user_model import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, username: str, password: str, nickname: str):
        new_user = User(username=username, password=password, nickname=nickname)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def get_user_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_username(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def get_all_users(self):
        return self.db.query(User).all()

    def update_user_nickname(self, user_id: int, new_nickname: str):
        user = self.get_user_by_id(user_id)
        if user:
            user.nickname = new_nickname
            self.db.commit()
            self.db.refresh(user)
            return user

    def delete_user(self, user_id: int):
        user = self.get_user_by_id(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
            return user
