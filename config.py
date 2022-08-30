import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY")
    SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT")
    API_V1_PREFIX = os.getenv("API_V1_PREFIX")
    EMAIL_TOKEN_VALID = os.getenv("EMAIL_TOKEN_VALID")
    EMAIL_CONFIRMATION_FREQ_MINUTES = os.getenv("EMAIL_CONFIRMATION_FREQ_MINUTES")
    TOKEN_VALID = os.getenv("TOKEN_VALID")
    ROOT_FILE_FOLDER = os.getenv("ROOT_FILE_FOLDER")
    DATABASE_URL = os.getenv("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    EMAIL_API_KEY = os.getenv("EMAIL_API_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    JSON_SORT_KEYS = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True
    DATABASE_URL = os.getenv("DATABASE_TEST_URL")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_TEST_URL")
    USER = os.getenv("TEST_USER")
    USER_PASSWORD = os.getenv("TEST_USER_PASSWORD")
