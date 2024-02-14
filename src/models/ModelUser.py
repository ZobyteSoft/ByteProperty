from .entities.user import User

class ModelUser():
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = '''SELECT id, username, password, fullname FROM user WHERE username = '{}' '''.format(user.username)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, username, fullname FROM user WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
 
    @classmethod
    def register(cls, db, user):
        try:
            cursor = db.connection.cursor()

            # Verificar si el nombre de usuario ya existe
            sql = "SELECT * FROM user WHERE username = %s"
            cursor.execute(sql, (user.username,))
            existing_user = cursor.fetchone()
            if existing_user:
                # El nombre de usuario ya existe
                return None

            # Insertar nuevo usuario en la base de datos
            contra = User.generarpass(user.password)
            sql = "INSERT INTO user (username, password, fullname) VALUES (%s, %s, %s)"
            cursor.execute(sql, (user.username, contra, user.fullname))
            db.connection.commit()

            return True

        except Exception as ex:
            raise Exception(ex)
        finally:
            cursor.close()

