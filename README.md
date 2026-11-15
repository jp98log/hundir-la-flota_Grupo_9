# Hundir la flota · Grupo 9

Versión en Python del juego Hundir la flota para jugar contra la máquina desde el terminal. Es el Team Challenge del Sprint 03 de Data Science de The Bridge.

## Requisitos

- Python 3
- NumPy (se instala con `requirements.txt`)

## Instalación

1. Clona el repositorio y entra en la carpeta:

   ```bash
   git clone https://github.com/jp98log/hundir-la-flota_Grupo_9.git
   cd hundir-la-flota_Grupo_9
   ```

2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

   Si prefieres un entorno virtual, créalo antes de instalar:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate        # Windows
   source .venv/bin/activate     # macOS y Linux
   ```

## Cómo ejecutar

Desde la carpeta del proyecto:

```bash
python main.py
```

En macOS y Linux puede que tengas que escribir `python3 main.py`.

## Cómo se juega

- Juegas tú contra la máquina. Cada uno tiene un tablero de 10 × 10 casillas.
- Al empezar, los barcos de los dos tableros se colocan al azar. Cada tablero tiene 10 barcos que ocupan 20 casillas en total:

  | Barcos | Eslora (casillas) | Casillas |
  |---|---|---|
  | 1 | 4 | 4 |
  | 2 | 3 | 6 |
  | 3 | 2 | 6 |
  | 4 | 1 | 4 |
  | **10** | | **20** |

- Se juega por turnos y empiezas tú.
- En tu turno disparas a una casilla del tablero de la máquina. El juego te pide la **fila** y la **columna**, dos números del 0 al 9.
- Si aciertas en un barco, vuelves a disparar. Si das en agua, el turno pasa a la máquina. La máquina sigue la misma regla.
- La máquina dispara a una casilla al azar de tu tablero y nunca repite casilla.
- Si disparas a una casilla a la que ya habías disparado, el disparo no cuenta: el juego te avisa y te pide otra coordenada.
- Si escribes algo que no es una coordenada (letras, números fuera del 0 al 9, un solo número...), el juego te avisa y te la vuelve a pedir. La partida no se cierra.
- Gana quien toque primero las 20 casillas con barco del rival.

## Qué ves en pantalla

En cada turno se imprimen dos tableros:

- **Tu tablero**: tus barcos y los disparos que te ha hecho la máquina.
- **El tablero de la máquina**: solo los disparos que has hecho tú. Sus barcos están ocultos hasta que los tocas.

### Símbolos del tablero

| Símbolo | Significado | Constante en `variables.py` |
|---|---|---|
| `~` | Agua sin disparar. En el tablero de la máquina, también una casilla a la que todavía no has disparado. | `AGUA` |
| `O` | Barco sin tocar. Solo se ve en tu tablero. | `BARCO` |
| `X` | Disparo que ha tocado un barco. | `TOCADO` |
| `·` | Disparo que ha caído al agua. | `AGUA_DISPARADA` |

## Estructura del proyecto

```
hundir-la-flota_Grupo_9/
├── main.py            # arranca y ejecuta la partida
├── clases.py          # la clase Tablero
├── funciones.py       # pedir y validar coordenadas, disparo de la máquina
├── variables.py       # constantes: tamaño, barcos, símbolos y mensajes
├── requirements.txt   # dependencias (numpy)
├── README.md          # este archivo
├── AI_LOG.md          # registro de uso de IA
└── .gitignore
```

Todas las constantes están en `variables.py`. Para cambiar el tamaño del tablero o la flota, solo hay que tocar ese archivo.

## Cómo trabajamos

- Cada tarea es un issue de GitHub, dentro del milestone **Sprint 5**.
- Cada issue tiene su rama, que sale de `main` actualizado: `tipo/numero-de-issue-descripcion` (por ejemplo, `feature/2-clase-tablero`).
- Los commits siguen Conventional Commits: `feat:`, `fix:`, `refactor:`, `docs:`, `test:` y `chore:`.
- Nada entra en `main` sin un Pull Request aprobado por otra persona del grupo.

## Equipo

| Integrante | Se encarga de |
|---|---|
| [jp98log](https://github.com/jp98log) | `funciones.py` |
| [gabrielito7008](https://github.com/gabrielito7008) | `variables.py` y `main.py` |
| [Enrique-e](https://github.com/Enrique-e) | `clases.py` (clase `Tablero`) |
| [SebastianMezaG](https://github.com/SebastianMezaG) | `README.md`, `requirements.txt` y `AI_LOG.md` |
