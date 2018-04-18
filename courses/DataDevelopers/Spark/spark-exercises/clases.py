class Cliente:
    def __init__(self, linea):
        self.dni, self.nombre, self.direccion = linea.split(',')
class Tarjeta(object):
    def __init__(self, linea):
        self.dni, self.nombre, self.tipo_tarjeta, self.num_tarjeta = linea.split(',')
