from nave import Nave
class Tablero:
    def __init__(self, tamano):
        self.__tamano = tamano
        self.__init_tablero()

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

    def __init_tablero(self):
        self.__tablero = []
        for i in self.__tamano:
            for j in self.__tamano:
                self.__tablero.append("")

    def comprobar_impacto(self,x,y): #verifica impacto en coordenadas
        pass

    def colocar_nave(self,nave,x,y,orientacion):
        pass

    def __str__(self):
        return "Tablero de tamaño: " + str(self.__tamano)

