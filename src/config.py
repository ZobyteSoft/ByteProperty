
class Config():
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'

class DevelopmentConfig(Config):
    HOST = '0.0.0.0'
    PORT = 8080
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'gestionpotreros'


config = {
    'development' : DevelopmentConfig
}  