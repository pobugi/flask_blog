from datetime import datetime

from flask import g

from src import db


class PostLike(db.Model):
    __tablename__ = "post_like"
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    post = db.relationship("Post", back_populates="likes")
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    owner = db.relationship("User", back_populates="likes")
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated = db.Column(db.DateTime, nullable=False, default=datetime.now())

    @staticmethod
    def create(post):
        post_like = PostLike(
            post=post, owner=g.user, created=datetime.now(), updated=datetime.now()
        )
        db.session.add(post_like)
        db.session.commit()
        return post_like

    @staticmethod
    def to_dict(obj):
        if not obj:
            return None
        return {
            "id": obj.id,
            "post_id": obj.post_id,
            "owner_id": obj.owner_id,
            "created": obj.created,
            "updated": obj.updated,
        }

    @staticmethod
    def to_dict_multi(objects):
        if not objects:
            return []
        return [PostLike.to_dict(obj) for obj in objects]
