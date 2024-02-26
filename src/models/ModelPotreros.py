from .entities.potreros import Potrero, Registrarrotacion
from .entities.lote import Lote
from flask import Flask, flash
from datetime import datetime, timedelta

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
    def mostrarRegistros(cls, db):
        try:
            cursor = db.connection.cursor()
            sql = '''
                SELECT r.idregistro, p.potrero_nombre, l.nombre, r.entradasalida, r.fecharotacion, r.posiblereingreso, r.estado, r.idlote, r.oservacion
                FROM registrosrotacion r
                JOIN lotes l ON r.idlote = l.idlote
                JOIN potreros p ON r.idpotrero = p.idpotrero
                '''
            cursor.execute(sql)
            registros = cursor.fetchall()

            return registros
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
    def mostrarlote(self, db, lote):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT potreros.potrero_nombre, lotes.nombre FROM lotes JOIN potreros ON lotes.idpotrero = potreros.idpotrero WHERE lotes.idlote = %s;'
            h = cursor.execute(sql, (lote,))
            ubicacion = cursor.fetchall()
            print(F'ESTA ES LA ubicaion {ubicacion}')

            return ubicacion
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
    @classmethod
    def rotarFinal(self, db, registrorotar):
        try:
            cursor = db.connection.cursor()
            """ fechadigitada = datetime.strptime(fecha1, "%Y-%m-%d")
            fechaAproximada = fechadigitada + timedelta(days=30) """
            sql = 'INSERT INTO `registrosrotacion`( `idpotrero`, `entradasalida`, `fecharotacion`, `posiblereingreso`, `estado`, `idlote`, `oservacion`) VALUES (%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql, (registrorotar.idpotrero,registrorotar.entradasalida,registrorotar.fecharotacion, registrorotar.posibleingreso,registrorotar.estado,registrorotar.idlote,registrorotar.observacion,))
            rotacion = cursor.fetchall()

            return rotacion
        except Exception as ex:
            raise Exception(ex)
        finally:
            cursor.close()
    @classmethod
    def mostrarOpcionesLotesAdmin(self, db):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT potreros.potrero_nombre, lotes.nombre FROM lotes JOIN potreros ON lotes.idpotrero = potreros.idpotrero '
            h = cursor.execute(sql)
            ubicacion = cursor.fetchall()
            print(F'ESTA ES LA ubicaion {ubicacion}')

            return ubicacion
        except Exception as ex:
            raise Exception(ex)
        finally:
            cursor.close()
    @classmethod
    def mostrarRegistrosPotreros(self, db):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT potreros.potrero_nombre, lotes.nombre FROM registrosrotacion JOIN potreros ON lotes.idpotrero = potreros.idpotrero '
            h = cursor.execute(sql)
            ubicacion = cursor.fetchall()
            print(F'ESTA ES LA ubicaion {ubicacion}')

            return ubicacion
        except Exception as ex:
            raise Exception(ex)
        finally:
            cursor.close()