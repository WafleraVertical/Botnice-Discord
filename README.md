# BotNice - Un Bot de Música para Discord

## Descripción

BotNice es un bot de música para Discord que permite a los usuarios buscar canciones en YouTube, agregar canciones a una cola de reproducción y escucharlas en un canal de voz. Con comandos simples, los usuarios pueden gestionar su experiencia musical en el servidor de Discord.

## Funcionalidades

- Buscar canciones en YouTube.
- Agregar canciones a una cola de reproducción.
- Reproducir canciones en un canal de voz.
- Saltar canciones en reproducción.
- Unirse y desconectarse de canales de voz.

## Requisitos

- Python 3.8 o superior.
- Bibliotecas necesarias:
  - `discord.py`
  - `yt-dlp`
  - `python-dotenv`

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/BotNice.git
   cd BotNice
Crea un entorno virtual (opcional pero recomendado):

bash
Copiar código
python -m venv .venv
source .venv/bin/activate  # En Windows usa .venv\Scripts\activate
Instala las dependencias:

bash
Copiar código
pip install -r requirements.txt
Configura tu token de Discord:

Crea un archivo .env en la raíz del proyecto con el siguiente contenido:
makefile
Copiar código
DISCORD_TOKEN=tu_token_aqui
Descarga FFmpeg:

Asegúrate de tener FFmpeg instalado y accesible en tu sistema. Puedes usar las builds estáticas disponibles en Gyan.dev.
Uso
Inicia el bot:

bash
Copiar código
python Botnice.py
Comandos disponibles:

_search <nombre_de_la_canción>: Busca canciones en YouTube.
_select <número>: Selecciona una opción de búsqueda para agregar a la cola.
_join: Une al bot en tu canal de voz.
_skip: Salta la canción actual.
_disconnect: Desconecta al bot del canal de voz.
Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir, por favor crea un fork del repositorio y envía un pull request.

Licencia
Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo LICENSE.

Contacto
Si tienes preguntas o comentarios, no dudes en abrir un issue en GitHub.

markdown
Copiar código

### Notas:

- **Asegúrate de reemplazar `tu-usuario` y `tu_token_aqui`** con tu nombre de usuario de GitHub y tu token de Discord, respectivamente.
- Puedes agregar más detalles según sea necesario, como secciones de "Problemas conocidos", "Próximas funciones", etc. según la evolución de tu proyecto.
- Recuerda mantener el archivo actualizado a medida que realizas cambios o mejoras en el bot.





