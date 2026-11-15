"""
Módulo de constantes y configuración global para el juego Hundir la Flota.
"""

# Dimensiones del tablero (10 filas x 10 columnas)
TAMANO_TABLERO = 10

# Diccionario con los tipos de barcos y su longitud (eslora)
BARCOS = {
    "Portaviones": 4,
    "Buque": 3,
    "Submarino": 2,
    "Lancha": 1
}

# Diccionario con el numero de barcos de cada tipo
CANTIDAD_BARCOS = {
    "Portaviones": 1,
    "Buque": 2,
    "Submarino": 3,
    "Lancha": 4
}

# Símbolos visuales que se mostrarán en la consola
AGUA = "~"              # Casilla vacía sin disparar
BARCO = "O"             # Casilla ocupada por un barco propio
TOCADO = "X"            # Disparo que ha acertado en un barco
AGUA_DISPARADA = "·"    # Disparo que ha caído al agua
