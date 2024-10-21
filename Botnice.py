import os
import discord
from discord.ext import commands
import yt_dlp
import asyncio
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    raise ValueError("El token no fue encontrado. Verifica tu archivo .env.")

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

FFMPEG_PATH = "C:/ffmpeg/bin/ffmpeg.exe"
FFMPEG_OPTIONS = {
    'options': '-vn',
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
}

YDL_OPTIONS = {
    'format': 'bestaudio/best',
    'noplaylist': True,
    'default_search': 'ytsearch5',
    'quiet': True
}

class BotNice(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.queue = []
        self.search_results = []

    @commands.command()
    async def search(self, ctx, *, query: str):
        async with ctx.typing():
            try:
                with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
                    info = ydl.extract_info(query, download=False)
                    entries = info.get('entries', [])[:5]

                    if not entries:
                        return await ctx.send("No se encontraron resultados.")

                    self.search_results = [(entry['url'], entry['title']) for entry in entries]

                    response = "**Resultados de la búsqueda:**\n"
                    for idx, (_, title) in enumerate(self.search_results, 1):
                        response += f"{idx}. {title}\n"
                    response += "\nUsa `_select <número>` para elegir una opción."

                    await ctx.send(response)
            except yt_dlp.DownloadError as e:
                await ctx.send(f'Error al buscar la canción: {e}')
            except Exception as e:
                await ctx.send(f'Ocurrió un error: {str(e)}')

    @commands.command()
    async def select(self, ctx, option: int):
        if option < 1 or option > len(self.search_results):
            return await ctx.send("Opción inválida. Elige un número de las opciones mostradas.")

        url, title = self.search_results[option - 1]
        self.queue.append((url, title))
        await ctx.send(f'**{title}** agregado a la cola.')

        if not ctx.voice_client or not ctx.voice_client.is_playing():
            await self.play_next(ctx)

    async def play_next(self, ctx):

        if self.queue:
            url, title = self.queue.pop(0)

            if not ctx.voice_client:
                await ctx.send("No estoy conectado a ningún canal de voz.")
                return

            try:

                source = discord.FFmpegPCMAudio(url, executable=FFMPEG_PATH, **FFMPEG_OPTIONS)
                ctx.voice_client.play(source, after=lambda e: self.client.loop.create_task(self.play_next(ctx)))
                await ctx.send(f'Reproduciendo: **{title}**')
            except Exception as e:
                await ctx.send(f'Error al reproducir: {str(e)}')

                await self.play_next(ctx)
        else:
            await ctx.send('La cola está vacía.')

    @commands.command()
    async def join(self, ctx):

        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("¡Debes unirte a un canal de voz primero!")

    @commands.command()
    async def skip(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send('Canción saltada.')

    @commands.command()
    async def disconnect(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send('Desconectado del canal de voz.')

client = commands.Bot(command_prefix='_', intents=intents)

async def main():
    await client.add_cog(BotNice(client))
    await client.start(TOKEN)

asyncio.run(main())
