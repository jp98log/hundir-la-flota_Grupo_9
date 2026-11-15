import numpy as np
from variables import TAMANO_TABLERO, BARCOS, AGUA, BARCO, TOCADO, AGUA_DISPARADA

class Tablero:
    """
  
    Tablero de juego de un jugador.
    
    Attributes:
        id_jugador (str): Identificador del jugador.
        tamano (int): Lado del tablero (tamano x tamano).
        tablero (np.ndarray): Barcos del jugador y disparos recibidos.
        disparos (np.ndarray): Solo los disparos recibidos, sin barcos.
    """
    def __init__(self, id_jugador):
        """
        Crea un tablero vacío para un jugador.  

        Args:
            id_jugador (str): Identificador del jugador.
        """
        self.id_jugador = id_jugador
        self.tamano = TAMANO_TABLERO
        self.tablero = np.full((self.tamano, self.tamano), AGUA)
        self.disparos = np.full((self.tamano, self.tamano), AGUA)
   
    def recibir_disparo(self, fila: int, columna: int) -> str:
        """
        Procesa un disparo en la casilla (fila, columna).

        Args:
            fila (int): Fila del disparo, de 0 a 9.
            columna (int): Columna del disparo, de 0 a 9.

        Returns:
            str: "tocado", "agua" o "repetido".
        """

    def mostrar(self):
        """Imprime el tablero por pantalla."""
        print(self.tablero)