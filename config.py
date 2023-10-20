
import os


SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

#or \
#    'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'C:\Users\lau20\Desktop\sqlite')

SQLALCHEMY_TRACK_MODIFICATIONS = False

