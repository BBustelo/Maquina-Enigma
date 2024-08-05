from Plugboard import Plugboard
from Reflector import Reflector
from Rotor import Rotor
from Teclado import Teclado

class Enigma():
    def __init__(self, reflector, rotorI, rotorII, rotorIII, plugboard, teclado):
        self.reflector = reflector
        self.rotorI = rotorI
        self.rotorII = rotorII
        self.rotorIII = rotorIII
        self.plugboard = plugboard
        self.teclado = teclado

    def encriptar(self, mensaje):
        encriptado = ''
        for caracter in mensaje:
            self.rotorIII.rotar()
            if self.rotorIII.muesca == self.rotorIII.derecha[0]:
                self.rotorII.rotar()
            elif self.rotorII.muesca == self.rotorII.derecha[0]:
                self.rotorI.rotar()
            elif self.rotorIII.muesca == self.rotorIII.derecha[0] and self.rotorII.muesca == self.rotorII.derecha[0]:
                self.rotorII.rotar()
                self.rotorI.rotar()
            if caracter == ' ':
                encriptado = encriptado + caracter
            else:
                caracter = self.teclado.pos(caracter)
                caracter = self.plugboard.avanzar(caracter)
                caracter = self.rotorIII.avanzar(caracter)
                caracter = self.rotorII.avanzar(caracter)
                caracter = self.rotorI.avanzar(caracter)
                caracter = self.reflector.avanzar(caracter)
                caracter = self.rotorI.retroceder(caracter)
                caracter = self.rotorII.retroceder(caracter)
                caracter = self.rotorIII.retroceder(caracter)
                caracter = self.plugboard.retroceder(caracter)
                caracter = self.teclado.letra(caracter)
                encriptado = encriptado + caracter
        return encriptado

"""""
teclado = Teclado()
plugboard = Plugboard()
reflectorA = Reflector('VZBRGITYUPSDNHLXAWMJQOFECK')
reflectorB = Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
reflectorC = Reflector('FVPJIAOYEDRZXWGCTKUQSBNMHL')
I = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', muesca='Q')
II = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', muesca='E')
III = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', muesca='V')
"""


