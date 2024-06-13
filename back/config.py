import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456789@localhost/la_Reina_Huevo_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
