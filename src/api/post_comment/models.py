from datetime import datetime

from flask import g

from src import db


class PostComment(db.Model):
    __tablename__ = "post_comment"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    post = db.relationship("Post", back_populates="comments")
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    owner = db.relationship("User", back_populates="comments")
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated = db.Column(db.DateTime, nullable=False, default=datetime.now())

    @staticmethod
    def create(description, post):
        post_comment = PostComment(
            description=description, post=post, owner=g.user, created=datetime.now(), updated=datetime.now()
        )
        db.session.add(post_comment)
        db.session.commit()
        return post_comment

    @staticmethod
    def to_dict(obj):
        if not obj:
            return None
        return {
            "id": obj.id,
            "description": obj.description,
            "post_id": obj.post_id,
            "owner_id": obj.owner_id,
            "created": obj.created,
            "updated": obj.updated,
        }

    @staticmethod
    def to_dict_multi(objects):
        if not objects:
            return []
        return [PostComment.to_dict(obj) for obj in objects]
