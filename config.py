from os import environ

INSTANCE_FOLDER_PATH = '/Users/arttuladhar/tmp/db'

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + INSTANCE_FOLDER_PATH + '/db.sqlite'
