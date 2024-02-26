from .entities.potreros import Potrero
from .entities.lote import Lote
from flask import Flask, flash

class ModelPotreros():
    
    @classmethod
    def nuevo(self, db, potrero):
        try:
            cursor = db.connection.cursor()
            sql = '''SELECT * FROM potreros WHERE potrero_nombre = %s '''
            cursor.execute(sql, (potrero.potrero_nombre,))
            tubo =cursor.fetchone()
            print(tubo)
            if tubo:
                flash('Potrero existe..')
            else:
                sql = 'INSERT INTO potreros( potrero_nombre, zona, area, promediodias, tipopastura, estado, coordenada, observacion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
                cursor.execute(sql, (potrero.potrero_nombre, potrero.zona, potrero.area, potrero.promediodias, potrero.tipopastura, potrero.estado, potrero.coordenada, potrero.observacion))
                db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
        finally:
            cursor.close()
    
    @classmethod
    def mostrarOpcionesPotreros(self, db):
        try:
            cursor = db.connection.cursor()
            sqlp = 'SELECT idpotrero, potrero_nombre FROM potreros'
            cursor.execute(sqlp)
            potreros = [{'idpotrero': row[0], 'nombre': row[1]} for row in cursor.fetchall()]

            return potreros
        except Exception as ex:
            raise Exception(ex)
        finally:
            cursor.close()
    
    @classmethod
    def mostrarOpcionesLotes(self, db):
        try:
            cursor = db.connection.cursor()
            sqlp = 'SELECT idlote, nombre, idpotrero FROM lotes'
            cursor.execute(sqlp)
            lotes = [{'idlote': row[0], 'nombre': row[1]} for row in cursor.fetchall()]

            return lotes
        except Exception as ex:
            raise Exception(ex)
        finally:
            cursor.close()

    @classmethod
    def mostrar(self, db, potrero):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT zona, estado FROM potreros WHERE idpotrero = %s;'
            h = cursor.execute(sql, (potrero,))
            potreros = cursor.fetchall()
            print(F'ESTA ES LA ZONA {potreros}')

            return potreros
        except Exception as ex:
            raise Exception(ex)
        finally:
            cursor.close()

    @classmethod
    def rotar(self, db, lote):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT idpotrero FROM lotes WHERE idlote = %s'
            cursor.execute(sql, (lote,))
            lotes = cursor.fetchall()

            return lotes
        except Exception as ex:
            raise Exception(ex)
        finally:
            cursor.close()