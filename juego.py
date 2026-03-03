from tablero import Tablero

class Juego:
    def __init__(self, tablero):
        self.__tablero = tablero

    @property
    def tablero(self):
        return self.__tablero

    @tablero.setter
    def tablero(self,tablero):
        if isinstance(tablero,Tablero):
            self.__tablero = tablero
        else:
            raise TypeError("Valor no válido")

    def lanzar_ataque(self,x,y):
        ataque = self.__tablero.comprobar_impacto(x,y)
        self.mostrar_resultado(ataque)

    def mostrar_resultado(self,resultado):
        if resultado:
            return "Impacto"
        else:
            return "Agua"

    def inicializar_naves(self):
        #colocar naves
        pass



