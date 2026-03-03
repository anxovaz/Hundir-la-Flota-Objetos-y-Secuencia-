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
            raise TypeError("Tablero incorrecto")

    def lanzar_ataque(self,x,y):
        ataque = self.__tablero.comprobar_impacto(x,y)
        self.mostrar_resultado(ataque)

    def mostrar_resultado(self,resultado):
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        else:
            print("Hundido")

        return resultado

    def inicializar_naves(self):
        #colocar naves
        pass

if __name__ == "__main__":
    t1 = Tablero(10)
    j1 = Juego(t1)
    j1.lanzar_ataque(2,3)



