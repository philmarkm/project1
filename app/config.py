import os
from  dotenv import load_dotenv
from flask import url_for

load_dotenv() 

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my-super-secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER= 'project1/app'
    SAFE_FORMATS = {'jpg', 'png', 'jpeg'}

    
