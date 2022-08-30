from flask import Blueprint, jsonify, request

from src.api import Post, PostComment
from src.auth.views import auth

post_comment_api = Blueprint("post_comment_api", __name__)


@post_comment_api.route("/posts/<int:id>/comments", methods=["POST"])
@auth.login_required
def create_post_comment(id):

    post = Post.get(id)
    if not post:
        return jsonify(False), 404

    data_dict = request.json

    post_comment = PostComment.create(description=data_dict.get("description"), post=post)
    return jsonify(PostComment.to_dict(post_comment))
