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
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            raise TypeError
    @tamano.setter
    def tamano(self, tamano):
        if isinstance(tamano, str):
            if tamano.isdigit():
                self.__tamano = int(tamano)
            else:
                raise ValueError
        elif isinstance(tamano, int):
            self.__tamano = tamano

        elif isinstance(tamano, float):
            self.__tamano = int(tamano)

        else:
            raise TypeError

    def recibir_disparo(self):
        """
        Procesa el impacto en la nave
        """
        return ""