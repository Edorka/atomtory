import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    pathToDB = os.path.join(basedir, 'data/items.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + pathToDB
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestConfig(Config):
    """Test configuration."""
    ENV = 'test'
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
