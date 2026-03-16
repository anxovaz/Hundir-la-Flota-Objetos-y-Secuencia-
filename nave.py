# Clase que representa una nave en el juego
from unboundmodule import regional_log_stats


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

        Como la vida es igual al tamanho y en esta clase no hay ningun atributo que haga referencia a la posicion en el
        tablero, ya que esta en __init__ de Tablero en una lista, simplemente se le resta 1 a self.tamano

        """
        self.tamano -= 1
        if self.tamano < 0:
            raise ValueError(f"Error no esperado, el atributo tamano es negativo. self.tamano -> {self.tamano}")
        else:
            return True #confirmación de que se ha quitado 1 vida (tamano) correctamente