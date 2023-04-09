import os
basedir = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
