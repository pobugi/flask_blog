from flask import Blueprint, jsonify

from src.api import User

user_api = Blueprint("user_api", __name__)


@user_api.route("/users", methods=["GET"])
def get_users():
    users = User.get_all()
    return jsonify(User.to_dict_multi(users))
