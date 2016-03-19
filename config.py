import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'guess-what-it-is-so-simple'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
