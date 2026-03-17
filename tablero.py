# Clase que representa el tablero del juego
from nave import Nave
class Tablero:

    def __init__(self, tamano=10):

        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2

        self.naves = []

        #inicializacion de las naves
        por1 = Nave("Enterprise", "portaaviones", 5)

        fra1 = Nave("Bismarck", "fragata", 3)
        fra2 = Nave("Prince of Wales", "fragata", 3)
        fra3 = Nave("Graf Spee", "fragata", 3)

        sub1 = Nave("U-47", "submarino", 1)
        sub2 = Nave("U-96", "submarino", 1)
        sub3 = Nave("U-505", "submarino", 1)
        sub4 = Nave("U-534", "submarino", 1)

        self.casillero = [
            [None, None, None, None, None, None, None, None, None, None],
            [None, por1, por1, por1, por1, por1, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, fra1, None, None, None, None, None, None],
            [None, None, None, fra1, None, None, sub1, None, None, None],
            [None, None, None, fra1, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, fra2, fra2, fra2, None, None, sub3, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, fra3, fra3, fra3, None, sub4, None, None, None, sub2]
        ]



    def colocar_nave(self, nave, x, y, orientacion):
        """
        Coloca una nave en el tablero en las coordenadas especificadas
        """

        for index, value in enumerate(self.casillero):
            if index == y:
                for i in range(0,nave.tamano):
                    value[x] = nave
                    x+=1

    def comprobar_impacto(self, x, y):
        """
        Comprueba si hay una nave en las coordenadas indicadas
        """

        print("[LOG] estoy en tablero comprobando impacto")
        '''
        n1 = Nave("barco",2)
        return n1.recibir_disparo()
        '''



        if isinstance(self.casillero[x][y], Nave):
            self.casillero[x][y].recibir_disparo()
            if self.casillero[x][y].tamano == 0: #para representar que le ha dado
                self.casillero[x][y] = 0
                return self.HUNDIDO
            else:
                self.casillero[x][y] = 0  #para representar que le ha dado
                return self.TOCADO
        else:
            return self.AGUA




