import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-keys'


    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///'+os.path.join(basedir, 'simple.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
