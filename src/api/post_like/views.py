from flask import Blueprint, jsonify, g

from src.api import Post, PostLike
from src.auth.views import auth
from src.utils.error_utils import ErrorUtils

post_like_api = Blueprint("post_like_api", __name__)


@post_like_api.route("/posts/<int:id>/likes", methods=["POST"])
@auth.login_required
def create_post_like(id):

    post = Post.get(id)
    if not post:
        return ErrorUtils.raise_not_found("Post")

    already_liked = PostLike.liked_by_me(post)
    if already_liked:
        post_like = PostLike.get_by_post_and_owner(post_id=post.id, owner_id=g.user.id)
        return jsonify(PostLike.to_dict(PostLike.delete(post_like.id)))
    post_like = PostLike.create(post=post)
    return jsonify(PostLike.to_dict(post_like))
