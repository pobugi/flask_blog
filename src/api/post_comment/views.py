from flask import Blueprint, jsonify, request, g

from src.api import Post, PostComment
from src.auth.views import auth

post_comment_api = Blueprint("post_comment_api", __name__)


@post_comment_api.route("/posts/<int:id>/comments", methods=["POST"])
@auth.login_required
def create_post_comment(id):

    post = Post.get(id)
    if not post:
        return jsonify({"error": "Post {} not found".format(id)}), 404

    data_dict = request.json

    post_comment = PostComment.create(description=data_dict.get("description"), post=post)
    return jsonify(PostComment.to_dict(post_comment))


@post_comment_api.route("/posts/<int:id>/comments", methods=["GET"])
@auth.login_required
def get_post_comments(id):

    post = Post.get(id)
    if not post:
        return jsonify({"error": "Post {} not found".format(id)}), 404

    post_comments = PostComment.get_all_by_post_id(post_id=id)
    return jsonify(PostComment.to_dict_multi(post_comments))


@post_comment_api.route("/comments/<int:id>", methods=["GET"])
@auth.login_required
def get_comment_by_id(id):

    post_comment = PostComment.get(id)
    if not post_comment:
        return jsonify({"error": "PostComment {} not found".format(id)}), 404
    return jsonify(PostComment.to_dict(post_comment))


@post_comment_api.route("/comments/<int:id>", methods=["PUT"])
@auth.login_required
def update_comment(id):
    data_dict = request.json

    if not data_dict:
        return jsonify({"error": "Please provide request body"}), 400

    post_comment = PostComment.get(id)
    if not post_comment:
        return jsonify({"error": "PostComment {} not found".format(id)}), 404

    if not post_comment.owner == g.user:
        return jsonify({"error": "You can only update your own comments."}), 403
    return jsonify(PostComment.to_dict(PostComment.update(id, data_dict)))


@post_comment_api.route("/comments/<int:id>", methods=["DELETE"])
@auth.login_required
def delete_comment(id):

    post_comment = PostComment.get(id)
    if not post_comment:
        return jsonify({"error": "PostComment {} not found".format(id)}), 404

    if not post_comment.owner == g.user:
        return jsonify({"error": "You can only delete your own comments."}), 403
    return jsonify(PostComment.to_dict(PostComment.delete(id)))
