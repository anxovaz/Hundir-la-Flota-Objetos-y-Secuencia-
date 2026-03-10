from tablero import Tablero


class Juego:
    def __init__(self):
        self.lanzar_ataque(3, 2)

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
        obj_tablero = Tablero()
        resultado = obj_tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)


if __name__ == "__main__":
    Juego()
    Juego().lanzar_ataque(3, 2)


