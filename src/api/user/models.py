from datetime import datetime

from src import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)
    posts = db.relationship("Post", back_populates="owner")
    likes = db.relationship("PostLike", back_populates="owner")
    comments = db.relationship("PostComment", back_populates="owner")

    @staticmethod
    def create(username):
        user = User(username=username, created=datetime.now(), updated=datetime.now())
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def to_dict(obj):
        if not obj:
            return None
        return {
            "id": obj.id,
            "username": obj.username,
            "created": obj.created,
            "updated": obj.updated,
        }

    @staticmethod
    def to_dict_multi(objects):
        if not objects:
            return []
        return [User.to_dict(obj) for obj in objects]
