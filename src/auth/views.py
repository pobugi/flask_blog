from flask import g
from flask_httpauth import HTTPBasicAuth

from src.api.user.models import User

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    if not username:
        return False
    user = User.get_by_username(username)
    if not user:
        user = User.create(username)
    g.user = user
    return True
