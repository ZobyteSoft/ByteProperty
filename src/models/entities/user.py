from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, fullname=""):
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname

    @staticmethod
    def generarpass(password):
        return generate_password_hash(password, method='pbkdf2:sha256')

    
    @staticmethod
    def check_password(hashed_password, password):
        return check_password_hash(hashed_password, password)
