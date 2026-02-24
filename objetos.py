class Nave:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
        if self.vida <= 0:
            self.hundido = True
        else:
            self.hundido = False


