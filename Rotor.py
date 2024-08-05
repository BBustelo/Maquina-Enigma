class Rotor:
    def __init__(self, conf, muesca = None, inicio = None):
        self.izquierda = conf
        self.derecha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.muesca = muesca
        if inicio is not None:
            while inicio != self.derecha[0]:
                self.derecha = self.derecha[1:] + self.derecha[0]

    def setInicio(self, inicio):
        self.incio = inicio

    def getInicio(self):
        return self.incio

    def getDerecha(self):
        return self.derecha

    def avanzar(self, pos):
        caracter = self.izquierda[pos]
        return self.derecha.find(caracter)

    def retroceder(self, pos):
        caracter = self.derecha[pos]
        return self.izquierda.find(caracter)

    def rotar(self):
        self.derecha = self.derecha[1:] + self.derecha[0]


