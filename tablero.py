# Clase que representa el tablero del juego
from nave import Nave
class Tablero:

    def __init__(self, tamano=10):

        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2

    def colocar_nave(self, nave, x, y, orientacion):
        """
        Coloca una nave en el tablero en las coordenadas especificadas
        """
        pass

    def comprobar_impacto(self, x, y):
        """
        Comprueba si hay una nave en las coordenadas indicadas
        """

        print("[LOG] estoy en tablero comprobando impacto")
        return Nave.recibir_disparo()
