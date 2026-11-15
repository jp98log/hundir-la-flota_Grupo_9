# AI_LOG · Team Challenge Hundir la flota

Este registro no cuenta para la nota. Sirve para ver dónde vais solos y dónde os apoyáis. Si no habéis usado IA en una parte, dejad el nivel en 0: también es un dato útil.

**Grupo:** jp98log, gabrielito7008, Enrique-e y SebastianMezaG (Grupo 9)

**Herramientas usadas:** Claude (README.md, requirements.txt y esta plantilla). Cada integrante añade aquí las que haya usado.

> El repositorio es público: no pongáis datos personales ni contraseñas en los prompts que copiéis aquí.

## Resumen por módulo

Niveles: **0** sin IA · **1** consulta puntual, el código es nuestro · **2** la IA escribe partes y las adaptamos · **3** casi todo lo escribe la IA

| Módulo | Quién lo ha llevado | Nivel de IA (0-3) | Nº de prompts | ¿Lo podríais repetir sin IA? (sí / en parte / no) |
|---|---|---|---|---|
| `variables.py` | gabrielito7008 | | | |
| `clases.py` | Enrique-e | | | |
| `funciones.py` | jp98log | | | |
| `main.py` | gabrielito7008 | | | |
| `README.md` | SebastianMezaG | 3 | 2 | en parte |

## Registro de prompts

Copiad este bloque por cada prompt que haya influido en vuestro código.

### README.md · Prompt 1

- **Objetivo:** entender qué me tocaba en el reto y preparar el issue #5 (README, requirements.txt y la plantilla de AI_LOG.md).
- **Prompt:** "Help me with this work, im not sure what to do, pull from github, I have been added to this groups github and there you have access to it all, I don't want you to push anything to avoid it saying that it was you"
- **Respuesta relevante:** un borrador del README (instalación, ejecución, reglas, qué se ve en pantalla, símbolos y estructura), `requirements.txt` con numpy y esta plantilla con los módulos y sus responsables. También me avisó de que `BARCOS` en `variables.py` solo sumaba 10 casillas y el enunciado pide 20.
- **Cambios:** ninguno; el borrador se subió tal cual.
- **Comprobación:** la IA comparó cada regla del README con el enunciado del notebook y comprobó que `pip install -r requirements.txt` instala numpy. Antes del merge lo revisa otro integrante en el Pull Request.
- **Decisión propia:** que la IA no hiciera commits ni push: los commits y el Pull Request los hago yo.

### README.md · Prompt 2

- **Objetivo:** que la IA dejara hecho el issue #5 en lugar de darme instrucciones.
- **Prompt:** "just do the work I need to do/assigned to me"
- **Respuesta relevante:** creó la rama `docs/5-readme-requirements-ailog` en mi ordenador y puso en ella `README.md`, `requirements.txt` y `AI_LOG.md`, listos para hacer commit.
- **Cambios:** ninguno.
- **Comprobación:** `git status` muestra solo esos tres archivos.
- **Decisión propia:** hacer yo los commits, el push y el Pull Request.

### Módulo X · Prompt 1

- **Objetivo:** qué queríais resolver.
- **Prompt:** copiadlo tal cual.
- **Respuesta relevante:** la parte que usasteis, resumida.
- **Cambios:** qué modificasteis y por qué.
- **Comprobación:** cómo verificasteis que funcionaba.
- **Decisión propia:** qué decidisteis vosotros.
