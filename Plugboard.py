class Plugboard:

    def __init__(self, arreglo=None):

        self.izquierda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.derecha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if arreglo is not None:
            for par in arreglo:
                caracterUno = par[0]
                caracterDos = par[1]
                posUno = self.izquierda.find(caracterUno)
                posDos = self.derecha.find(caracterDos)
                self.derecha = self.derecha[:posUno] + caracterDos + self.derecha[posUno+1:]
                self.derecha = self.derecha[:posDos] + caracterUno + self.derecha[posDos+1:]

    def avanzar(self, pos):
        caracter = self.izquierda[pos]
        return self.derecha.find(caracter)

    def retroceder(self, pos):
        caracter = self.derecha[pos]
        return self.izquierda.find(caracter)
