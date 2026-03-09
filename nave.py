# Clase que representa una nave en el juego
class Nave:
    def __init__(self, nombre, tamano):
        self.__nombre = nombre
        self.__tamano = tamano

    @property
    def nombre(self):
        return self.__nombre
    @property
    def tamano(self):
        return self.__tamano
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    @tamano.setter
    def tamano(self, tamano):
        self.__tamano = tamano

    def recibir_disparo(self):
        """
        Procesa el impacto en la nave
        """
        return ""