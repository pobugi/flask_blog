from flask import Blueprint, jsonify, request

from src.api import Post, PostLike
from src.auth.views import auth

post_like_api = Blueprint("post_like_api", __name__)


@post_like_api.route("/posts/<int:id>/likes", methods=["POST"])
@auth.login_required
def create_post_like(id):

    post = Post.get(id)
    if not post:
        return jsonify(False), 404

    post_like = PostLike.create(post=post)
    return jsonify(PostLike.to_dict(post_like))
