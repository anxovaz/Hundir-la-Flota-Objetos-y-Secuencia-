class Nave:
    def __init__(self, nombre, tamano):
        self.__nombre = nombre
        self.__tamano = tamano

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            raise TypeError("Error de tipo en nombre")
    @property
    def tamano(self):
        return self.__tamano
    @tamano.setter
    def tamano(self, tamano):
        if isinstance(tamano, int):
            self.__tamano = tamano
        elif isinstance(tamano, str):
            if tamano.isdigit():
                self.__tamano = int(tamano)
            else:
                raise ValueError("Error de valor en tamano")
        elif isinstance(tamano, float):
            self.__tamano = int(tamano)

    def recibir_disparo(self):
        self.__tamano -= 1
        if self.__tamano <= 0:
            return "Nave destruida"
        else:
            return f"Nave impactada le quedan {self.__tamano} vidas"

