from flask import Blueprint, jsonify, request

from src.api.post.models import Post
from src.auth.views import auth

post_api = Blueprint("post_api", __name__)


@post_api.route("/posts", methods=["GET"])
def get_posts():
    blog_posts = Post.get_all()
    return jsonify(Post.to_dict_multi(blog_posts))


@post_api.route("/posts", methods=["POST"])
@auth.login_required
def create_post():

    data_dict = request.json

    blog_post = Post.create(
        title=data_dict.get("title"),
        description=data_dict.get("description"),
    )
    return jsonify(Post.to_dict(blog_post))
