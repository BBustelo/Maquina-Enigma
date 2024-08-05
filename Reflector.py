class Reflector:
    def __init__(self, conf):
        self.derecha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.izquierda = conf

    def avanzar(self, pos):
        caracter = self.izquierda[pos]
        return self.derecha.find(caracter)


