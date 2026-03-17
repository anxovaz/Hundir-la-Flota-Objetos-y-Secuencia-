from nave import Nave
from tablero import Tablero


class Juego:
    def __init__(self):
        self.obj_tablero = Tablero()

        self.lanzar_ataque(1, 1)
        self.lanzar_ataque(1, 2)
        self.lanzar_ataque(1, 3)
        self.lanzar_ataque(1, 4)
        self.lanzar_ataque(1, 5)

        print("---")

        self.lanzar_ataque(6, 4)
        nave1 = Nave("nave Test","submarino", 1)
        self.obj_tablero.colocar_nave(nave1,6,4)
        self.lanzar_ataque(6, 4)


    def inicializar_naves(self):
        """
        Crea e inicializa todas las naves del juego
        """
        pass

    def mostrar_resultado(self, resultado: int):
        """
        Muestra por pantalla el resultado de un disparo.

        """
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")

    def lanzar_ataque(self, x, y):
        """
        Ejecuta un disparo en la posición indicada

        """
        print(f"Atacando a  {x}, {y} ")

        resultado = self.obj_tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)


if __name__ == "__main__":
    Juego()


