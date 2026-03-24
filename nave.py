class Nave:
    '''
    Clase que representa una nave

    Attributos:
    tipo: tipo de nave
    nombre: nombre de nave
    tamano: tamano de nave (que es igual a la vida)

    Métodos:
    setters y getters para atributos
    recibir_disparo() -> le resta 1 a tamano (que tambien indica la vida)
    __init__ -> inicializador
    __str__ -> Devuelve un string con iformación sobre la nave
    '''
    def __init__(self, nombre, tipo, tamano):
        self.nombre = nombre
        self.tamano = tamano
        self.tipo = tipo

    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo):
        if isinstance(tipo, str):
            self.__tipo = tipo
        else:
            raise TypeError("Tipo tiene que ser string")
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

    def __str__(self):
        return f"Nombre {self.nombre}, Tamano {self.tamano}, Tipo {self.tipo}"