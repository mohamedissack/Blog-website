import os

class Config: 
    '''
    General configuration for parent class
    '''
    SECRET_KEY='cSZVa45zc7P5pcLwPwKWsQ'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:12345@localhost/blogpost'

    # email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'mohamedissack7573@gmail.com'
    MAIL_PASSWORD = 'Salah4580'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",1)
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:12345@localhost/blog'
        

class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:12345@localhost/blogpost'
    
    DEBUG = True   

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test': TestConfig
}