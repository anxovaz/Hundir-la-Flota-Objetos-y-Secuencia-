from nave import Nave
from casilla import Casilla
'''
Clase que representa el tablero del juego, contiene el tablero del juego con Casillas
Atributos:
tamano

Métodos:
__init__ -> inicializador
colocar_nave -> coloca nave en la posición inidcada
comprobar_impacto -> comprueba el impacto
__str__ -> devuelve el casillero
'''
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

        self.casillero = []


        #crea el tablero con t0do agua
        for i in range(0, tamano):
            lista = []
            for j in range(0, tamano):
                c = Casilla("agua")
                lista.append(c)
            self.casillero.append(lista)

        #genera casillas con Naves

        casilla01 = Casilla(por1)
        casilla11 = Casilla(fra1)
        casilla12 = Casilla(fra2)
        casilla13 = Casilla(fra3)
        casilla21 = Casilla(sub1)
        casilla22 = Casilla(sub2)
        casilla23 = Casilla(sub3)
        casilla24 = Casilla(sub4)

        #agrega las Naves al Tablero

        self.casillero[0][0]=casilla01
        self.casillero[6][1]=casilla11
        self.casillero[6][2]=casilla12
        self.casillero[6][3]=casilla13
        self.casillero[2][5]=casilla21
        self.casillero[2][6]=casilla22
        self.casillero[2][7]=casilla23
        self.casillero[2][8]=casilla24


    def colocar_nave(self, nave, x, y):
        """
        Coloca una nave en el tablero en las coordenadas especificadas
        """
        c0 = Casilla(nave)
        self.casillero[x][y] = c0

    def comprobar_impacto(self, x, y):
        """
        Comprueba si hay una nave en las coordenadas indicadas y devuelve el resultado con las constantes: self.TOCADO, self.HUNDIDO, self.AGUA
        """

        print("[LOG] estoy en tablero comprobando impacto")



        if isinstance(self.casillero[x][y], Casilla): #siempre va a ser true
            resultado = self.casillero[x][y].recibirDisparo()
            if resultado == -1:
                raise Exception("No se puede atacar 2 veces la misma posición")
            elif resultado == 1:
                return self.TOCADO
            elif resultado == 2:
                return self.HUNDIDO
            else:
                return self.AGUA
        else: #no devería de llegar aquí nunca, pero en caso de que suceda se detendría la qjecución
            raise Exception("Error inesperado, objeto Casilla no creado")


    def __str__(self):
        return f"{self.casillero}"

