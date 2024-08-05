import pygame
class Teclado:

    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def pos(self, letra):
        pos = self.alfabeto.find(letra)
        return pos

    def letra(self, pos):
        letra = self.alfabeto[pos]
        return letra

