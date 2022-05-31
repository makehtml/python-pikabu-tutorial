"""
Here should be some docstring for config.py
Config file for any library we are going to use.
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    APP_NAME = 'NaviProj'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' \
                              + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}