from datetime import datetime

from flask import g

from src import db
from src.api import User


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    owner = db.relationship("User", back_populates="posts")
    comments = db.relationship("PostComment", back_populates="post")
    likes = db.relationship("PostLike", back_populates="post")
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)

    @property
    def likes_count(self):
        from src.api import PostLike
        return PostLike.query.filter_by(post_id=self.id).count()

    @staticmethod
    def create(title, description):
        blog_post = Post(
            title=title, description=description, owner=g.user, created=datetime.now(), updated=datetime.now()
        )
        db.session.add(blog_post)
        db.session.commit()
        return blog_post

    @staticmethod
    def get(id):
        return Post.query.get(id)

    @staticmethod
    def get_all():
        blog_posts = Post.query.all()
        return blog_posts

    @staticmethod
    def to_dict(obj):
        if not obj:
            return None
        from src.api import PostComment, PostLike

        return {
            "id": obj.id,
            "title": obj.title,
            "description": obj.description,
            "likes_count": obj.likes_count,
            "owner": User.to_dict(obj.owner),
            "comments": PostComment.to_dict_multi(obj.comments),
            "likes": PostLike.to_dict_multi(obj.likes),
            "created": obj.created,
            "updated": obj.updated,
        }

    @staticmethod
    def to_dict_multi(objects):
        if not objects:
            return []
        return [Post.to_dict(obj) for obj in objects]
