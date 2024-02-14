from .entities.potreros import Potrero
from .entities.lote import Lote
from flask import Flask, flash


class ModelLote():
    
    @classmethod
    def nuevo(self, db, lote):
        try:
            cursor = db.connection.cursor()
            sql = '''SELECT * FROM lotes WHERE nombre = %s '''
            cursor.execute(sql, (lote.nombre,))
            tubo =cursor.fetchone()
            print(tubo)
            if tubo:
                flash('El Lote ya existe..')
            else:
                sql = 'INSERT INTO lotes( nombre) VALUES (%s)'
                cursor.execute(sql, (lote.nombre))
                db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
        finally:
            cursor.close()
    @classmethod
    def rotar(self, db, potrero, lote):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT idpotrero FROM lotes WHERE idlote = %s'
            cursor.execute(sql, (lote,))
            db.connection.commit()
            lotes = cursor.fetchall()
            if lotes:
                sqle = 'UPDATE `lotes` SET `idpotrero`= %s WHERE idlote = %s'
                sqls = 'UPDATE `potreros` SET `estado`= "Ocupado" WHERE idpotrero = %s'
                cursor.execute(sqle, (potrero, lote))
                cursor.execute(sqls, (potrero,))
                db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
        finally:
            cursor.close()