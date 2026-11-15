import numpy as np
import random

from variables import AGUA, AGUA_DISPARADA, BARCO, TAMANO_TABLERO, TOCADO


def mostrar_instrucciones():
    """
    Muestra por pantalla las reglas básicas y la leyenda de símbolos del juego.
    """
    print("--- HUNDIR LA FLOTA ---")
    print(f"Dispara indicando fila y columna (de 0 a {TAMANO_TABLERO - 1}), separadas por espacio o coma.")
    print("Si das a un barco repites turno. Si cae en agua, le toca a la máquina.")
    print("Leyenda del tablero:")
    print(f"  {AGUA} -> Agua sin explorar")
    print(f"  {BARCO} -> Barco intacto")
    print(f"  {TOCADO} -> Barco tocado")
    print(f"  {AGUA_DISPARADA} -> Disparo al agua")


def pedir_coordenadas(tablero):
    """
    Pide por consola las coordenadas de disparo y valida que sean correctas.

    Args:
        tablero (Tablero): Tablero rival sobre el que se va a realizar el disparo.

    Returns:
        tuple: Par de enteros (fila, columna) validados y disponibles.
    """
    limite = TAMANO_TABLERO - 1

    while True:
        respuesta = input(f"Introduce coordenadas de disparo (0-{limite}, ej: 3, 5): ")
        datos = respuesta.replace(",", " ").split()

        if len(datos) != 2:
            print("Formato incorrecto. Tienes que poner dos números (fila y columna).")
            continue

        try:
            fila = int(datos[0])
            col = int(datos[1])
        except ValueError:
            print("Error: las coordenadas tienen que ser números enteros.")
            continue

        if fila < 0 or fila >= TAMANO_TABLERO or col < 0 or col >= TAMANO_TABLERO:
            print(f"Te has salido del tablero. Introduce números entre 0 y {limite}.")
            continue

        if tablero.disparos[fila, col] != AGUA:
            print("Ya habías disparado en esa casilla. Prueba con otra.")
            continue

        return fila, col


def elegir_disparo_maquina(tablero):
    """
    Selecciona aleatoriamente una coordenada donde la máquina aún no ha disparado.

    Args:
        tablero (Tablero): Tablero del jugador que recibe el disparo de la máquina.

    Returns:
        tuple: Coordenada (fila, columna) elegida al azar.
    """
    filas_libres, cols_libres = np.where(tablero.disparos == AGUA)
    opciones = list(zip(filas_libres, cols_libres))

    fila, col = random.choice(opciones)
    return int(fila), int(col)


def quedan_barcos(tablero):
    """
    Comprueba si todavía quedan casillas de barco sin tocar en el tablero.

    Args:
        tablero (Tablero): Tablero que se quiere comprobar.

    Returns:
        bool: True si queda al menos una casilla con barco, False si están todos hundidos.
    """
    barcos_restantes = np.sum(tablero.tablero == BARCO)
    return int(barcos_restantes) > 0