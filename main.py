"""
Archivo principal (main) para ejecutar el juego Hundir la Flota.
"""

from clases import Tablero
from funciones import (
    elegir_disparo_maquina,
    mostrar_instrucciones,
    pedir_coordenadas,
    quedan_barcos,
)


def main():
    # 1. Mostrar instrucciones y bienvenida
    mostrar_instrucciones()
    input("\nPresiona Enter para comenzar la partida...")

    # 2. Inicializar tableros para el Jugador y la Máquina
    tablero_jugador = Tablero("Jugador")
    tablero_maquina = Tablero("Máquina")

    # 3. Colocar los barcos en ambos tableros
    print("\nColocando tus barcos...")
    tablero_jugador.colocar_barcos()

    print("Colocando los barcos de la máquina...")
    tablero_maquina.colocar_barcos()

    # 4. Bucle principal de la partida
    turno_jugador = True  # Empieza el jugador

    while True:
        print("\n" + "=" * 40)

        if turno_jugador:
            print("\n--- TU TURNO ---")
            print("Tablero de disparos al enemigo:")
            tablero_maquina.mostrar(ocultar_barcos=True)

            # Pedir y validar coordenadas de ataque
            fila, col = pedir_coordenadas(tablero_maquina)
            resultado = tablero_maquina.recibir_disparo(fila, col)

            if resultado == "tocado":
                print(f"¡Impacto! Has dado a un barco en ({fila}, {col}). ¡Repites turno!")
            elif resultado == "agua":
                print(f"Agua en ({fila}, {col}). Turno de la máquina.")
                turno_jugador = False
            elif resultado == "repetido":
                print("Ya habías disparado ahí. Prueba otra vez.")
                continue

            # Comprobar si el jugador ha ganado
            if not quedan_barcos(tablero_maquina):
                print("\n¡ENHORABUENA! ¡Has hundido toda la flota enemiga y has ganado! 🎉")
                break

        else:
            print("\n--- TURNO DE LA MÁQUINA ---")
            fila, col = elegir_disparo_maquina(tablero_jugador)
            resultado = tablero_jugador.recibir_disparo(fila, col)
            print(f"La máquina ha disparado a ({fila}, {col}) -> Resultado: {resultado.upper()}")

            print("\nTu tablero actual:")
            tablero_jugador.mostrar(ocultar_barcos=False)

            if resultado == "tocado":
                print("¡La máquina te ha dado! Vuelve a tirar.")
                turno_jugador = False
            else:
                print("La máquina falló. Es tu turno.")
                turno_jugador = True

            # Comprobar si la máquina ha ganado
            if not quedan_barcos(tablero_jugador):
                print("\nGAME OVER. La máquina ha destruido toda tu flota. 😢")
                break


if __name__ == "__main__":
    main()
