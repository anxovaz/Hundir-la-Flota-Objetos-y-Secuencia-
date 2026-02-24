class Nave:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
        if self.vida <= 0:
            self.hundido = True
        else:
            self.hundido = False


class Casilla:
    def __init__(self, numx, numy, ocupada, tipoNave):
        self.numx = numx
        self.numy = numy
        self.ocupada = ocupada
        self.tipoNave = tipoNave

class Tablero:
    def __init__(self, casillasX, casillasY, ocupadas = []):
        self.casillasX = casillasX
        self.casillasY = casillasY
        self.ocupadas = ocupadas