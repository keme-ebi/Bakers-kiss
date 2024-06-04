import os
from decouple import config
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class Config:
    SECRET_KEY=config('SECRET_KEY', 'secret')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    # in case you want to test with sqlite, uncomment the uri below and comment out the one with config('DB_URI')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR, 'db.sqlite3')

    # the uri below is for mysql, in order to keep privacy, store credentials in .env file under the name DB_URI
    # i.e 'mysql+pymysql://username:password@localhost/bakers_kiss'
    # bakers_kiss is the name of the database used, feel free to choose a different name
    SQLALCHEMY_DATABASE_URI = config('DB_URI')
    MAIL_SERVER = 'smtp.gmail.com'
    PORT = 587
    MAIL_USERNAME = config('MAIL_USERNAME')
    MAIL_PASSWORD = config('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = config('MAIL_DEFAULT_SENDER')
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    MAIL_SERVER = 'smtp.gmail.com'
    PORT = 587
    MAIL_USERNAME = config('MAIL_USERNAME')
    MAIL_PASSWORD = config('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = config('MAIL_DEFAULT_SENDER')
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    

class ProdConfig(Config):
    pass


config_dict = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig
}