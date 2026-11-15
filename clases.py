import numpy as np
import random
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
        self.barcos = BARCOS
        self.tablero = np.full((self.tamano, self.tamano), AGUA)
        self.disparos = np.full((self.tamano, self.tamano), AGUA)
   
    def colocar_barcos(self):
            """
            Colocar todos los barcos en el tablero de forma aleatoria.
               
            Cada barco queda entero dentro del tablero y sin pisar a otro.
            """
            for nombre, longitud in BARCOS.items(): # La Longitud lo da el bucle y cambia en cada vuelta: 4,3,2,1...
                colocado = False    # Todavía no hemos encontrado sitio para este barco
                while not colocado: # Repite hasta encontrar un sitio válido
                    fila = random.randint(0, self.tamano - 1) # Elige al azar la fila donde empieza; self.tamano es 10, así que self.tamano - 1 es 9. La fila es entre 0 y 9, que son las filas del tablero.
                    columna = random.randint(0, self.tamano - 1) # Elige al azar la colimna donde empieza; self.tamano - longitud para que el barco no se salga.
                    orientacion = random.choice(["N", "S", "E","O"])    # Hacia dónde apunta el barco
                    
                    # Zona que ocuparia el barco: filas f1:f2 y columas c1:c2
                    if orientacion == "E":  # Este: hacia la derecha
                        f1, f2 = fila, fila + 1 # Ocupa solo una fila
                        c1, c2 = columna, columna + longitud    # Desde la columna hacia la derecha
                    elif orientacion == "O":    # Oeste: hacia la izquierda
                        f1, f2 = fila, fila + 1 # Ocupa solo una fila
                        c1, c2 = columna - longitud + 1, columna + 1    # Desde la columna hacia la izquierda
                    elif orientacion == "S":    # Sur: hacia abajo
                        f1, f2 = fila, fila + longitud  # Desde la fila hacia abajo
                        c1, c2 = columna, columna + 1    # Ocupa solo una columna
                    else:   # Norte: hacia arriba
                        f1, f2 = fila - longitud + 1, fila + 1  # Desde la fila hacia arriba
                        c1, c2 = columna, columna + 1   # Ocupa solo una columna

                    dentro = f1 >= 0 and c1 >= 0 and f2 <= self.tamano and c2 <= self.tamano    # ¿Cabe en el tablero?
                    if dentro and np.all(self.tablero[f1:f2, c1:c2] == AGUA):   # ¿Cabe y todo es agua?
                        self.tablero[f1:f2, c1:c2] = BARCO  # Pinta el barco
                        colocado = True # Barco colocado: se sale del while y pasa al siguiente
    
    def recibir_disparo(self, fila: int, columna: int) -> str:
        """
        Procesa un disparo en la casilla (fila, columna).

        Args:
            fila (int): Fila del disparo, de 0 a 9.
            columna (int): Columna del disparo, de 0 a 9.

        Returns:
            str: "tocado", "agua" o "repetido".
        """
        if self.disparos[fila, columna] != AGUA:    # Si ya no es AGUA, ya se disparó ahí
            return "repetido"   # El disparo no cuenta
        if self.tablero[fila, columna] == BARCO:    # Si en esa casilla hay barco
            self.tablero[fila, columna] = TOCADO    # Se marca tocado en el tablero propio
            self.disparos[fila, columna] = TOCADO   # y en el que ve el rival
            return "tocado" 
        self.tablero[fila, columna] = AGUA_DISPARADA    # Si no había barco, se marca agua disparada en tu tablero
        self.disparos[fila, columna] = AGUA_DISPARADA   # y también en el tablero que ve el rival
        return "agua"  

    def mostrar(self, ocultar_barcos=False):    # Muestra el tablero completo
        """
        Imprime el tablero por pantalla.
        Args:
            ocultar_barcos (bool): Si es True, no se ven los barcos, solo los disparos.
        """
        if ocultar_barcos:
            print(self.disparos)    # Imprime solo los disparos, sin revelar dónde están los barcos
        else:
            print(self.tablero) # Imprime mis barcos y los disparos recibidos   