import pytest
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

import config
from src import create_app


@pytest.fixture
def app():
    app = create_app(config.TestingConfig)
    app.config.from_object(config.TestingConfig)
    with app.app_context() as ctx:
        ctx.push()
    db = SQLAlchemy(app)
    db.init_app(app)

    app.engine = create_engine(app.config["DATABASE_URL"], pool_size=5, pool_recycle=6)

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture
def client(app):
    return app.test_client()
