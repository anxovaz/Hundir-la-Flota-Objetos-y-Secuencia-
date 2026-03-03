from nave import Nave
class Tablero:
    def __init__(self, tamano):
        self.__tamano = tamano

    @property
    def tamano(self):
        return self.__tamano
    @tamano.setter
    def tamano(self, tamano):
        if isinstance(tamano, int):
            self.__tamano = tamano
        elif isinstance(tamano, float):
            self.__tamano = int(tamano)
        elif isinstance(tamano, str):
            if tamano.isdigit():
                self.__tamano = int(tamano)
            else:
                raise ValueError("Tamaño incorrecto")
        else:
            raise TypeError("Tamano incorrecto")

    def comprobar_impacto(self): #verifica impacto en coordenadas
        pass

    def __str__(self):
        return "Tablero de tamaño: " + str(self.__tamano)

