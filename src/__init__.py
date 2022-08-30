import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app_settings = config.DevelopmentConfig
    app.config.from_object(app_settings)

    db.init_app(app)
    from src.api.file.views import file_api
    from src.api.post.views import post_api
    from src.api.user.views import user_api
    from src.api.post_comment.views import post_comment_api
    from src.api.post_like.views import post_like_api

    app.register_blueprint(file_api)
    app.register_blueprint(post_api)
    app.register_blueprint(user_api)
    app.register_blueprint(post_comment_api)
    app.register_blueprint(post_like_api)

    app.engine = create_engine(app.config["DATABASE_URL"])

    with app.app_context():
        db.create_all()

    return app
