
class Potrero():
    def __init__(self, idpotrero, potrero_nombre, zona, area, promediodias, tipopastura, estado, coordenada, observacion):
        self.idpotrero = idpotrero
        self.potrero_nombre = potrero_nombre
        self.zona = zona
        self.area = area
        self.promediodias = promediodias
        self.tipopastura = tipopastura
        self.estado = estado
        self.coordenada = coordenada
        self.observacion = observacion

class Registrarrotacion():
    def __init__(self, idregistro, idpotrero, entradasalida, fecharotacion, posiblereingreso, estado, idlote, observacion):
        self.idregistro = idregistro
        self.idpotrero = idpotrero
        self.entradasalida = entradasalida
        self.fecharotacion = fecharotacion
        self.posiblereingreso = posiblereingreso
        self.estado = estado
        self.idlote = idlote
        self.observacion = observacion
