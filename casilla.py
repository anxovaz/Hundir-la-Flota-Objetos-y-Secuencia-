from nave import Nave
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

    def recibirDisparo(self):
        '''
        recibirDisparo devuelve 0 en caso de agua, 1 en caso de nave, -1 en caso de que el usuario haya atacado 2 veces a la misma casilla y 2 hundido
        :return:
        '''
        if self.__estado == False: #si no se le ha disparado anteriormente
            self.__estado = True
            if self.__contenido == "agua":
                return 0 #False indica agua
            else: #nave
                self.__contenido.recibir_disparo() #lanza un disparo
                if self.__contenido.tamano == 0: #si se queda sin vidas
                    return 2
                else:
                    return 1
        else:
            return -1

    def __str__(self):
        return f"Contenido: {self.__contenido}\nVisitado: {self.__estado}"

