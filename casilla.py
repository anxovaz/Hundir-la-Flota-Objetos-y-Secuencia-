from nave import Nave

'''
Clase casilla

Esta clase representa las casillas que contiene el tablero.

Atributos:
- Casilla.__contenido: contiene o "agua" o una Nave
- Casilla.__estado: Booleano que indica si ya se lanzó un ataque anteriormente o no.

Métodos:
-comprobar_contenido() -> Comprueba si hay agua o Nave y devuelve True o False
-__init__ -> inizializador
-setter y getter -> para Casilla.__contenido (@property y @contenido.setter)
-recibirDisparo -> encargado de lanzar disparo a Nave
.__str__ -> Muestra en formato string una cadena de texto con información sobre el contenido y su estado.
'''
class Casilla:
    def __init__(self, contenido):
        self.contenido = contenido
        self.__estado = False #visitado o no

    @property
    def contenido(self):
        return self.__contenido
    @contenido.setter
    def contenido(self, contenido):
        if isinstance(contenido,str):
            if contenido.lower() == "agua":
                self.__contenido = "agua"
            else:
                raise ValueError("Contenido no valido")
        elif isinstance(contenido,Nave):
            self.__contenido = contenido
        else:
            raise TypeError("Contenido no valido, tipo incorrecto")

    def comprobar_contenido(self):
        #comprueba si hay agua o nave
        if self.__contenido == "agua":
            return False
        else:
            return True

    def recibirDisparo(self):
        '''
        recibirDisparo devuelve:
        0 en caso de agua
        1 en caso de nave
        -1 en caso de que el usuario haya atacado dos o más veces a la misma casilla y
        2  si está hundido

        '''
        if self.__estado == False: #si no se le ha disparado anteriormente
            self.__estado = True
            if self.comprobar_contenido(): #nave
                self.__contenido.recibir_disparo()  # lanza un disparo
                if self.__contenido.tamano == 0:  # si se queda sin vidas
                    return 2
                else:
                    return 1

            else: #agua
                return 0  # False indica agua
        else:
            return -1

    def __str__(self):
        return f"Contenido: {self.__contenido}\nVisitado: {self.__estado}"

