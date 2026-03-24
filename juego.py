from nave import Nave
from tablero import Tablero

'''
Clase que gestiona el Juego, el init lanza los ataques e instancia el tablero

Atributos:
N/A

Métodos:
__init__ -> gestor del juego
mostrtar_resultado -> muestra el resultado por pantalla
lanzar_ataque -> lanzar ataque

'''
class Juego:
    def __init__(self):
        #instancia Tablero
        self.obj_tablero = Tablero()

        #Lanza ataques
        self.lanzar_ataque(0, 0)
        self.lanzar_ataque(1, 2)
        self.lanzar_ataque(1, 3)
        self.lanzar_ataque(2, 8)
        self.lanzar_ataque(1, 5)

        print("---")

        #prueba para comprobar el mét0do colocar_nave()
        self.lanzar_ataque(6, 4)
        nave1 = Nave("nave Test","submarino", 1)
        #al coolocar una nave el mét0do colocar_nave de Tablero crea una casilla en la que mete a la nave indicada, por lo cual como se está creando un nuevo objeto la variable Casilla.__estado estará como False (no visitada)
        #para cambiarlo se puede modificar la casilla usando el setter de contenido en vez de crear una nueva
        self.obj_tablero.colocar_nave(nave1,6,4)
        self.lanzar_ataque(6, 4)


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
        Ejecuta un disparo en la posición indicada y muestra el resultado usando el mét0do mostrar_resultado

        """
        print(f"Atacando a  {x}, {y} ")

        resultado = self.obj_tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)


if __name__ == "__main__":
    Juego()


