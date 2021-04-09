import os
import asyncio
import discord
import youtube_dl
from keep_alive import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix=commands.when_mentioned_or("sh!"))

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='join', help='How to join the channel')
    async def join(self, ctx):
        """Joins a voice channel"""
        channel = ctx.author.voice.channel
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command(name='play', help='How to play the song')
    async def play(self, ctx, *, url):
        """Plays from a url (almost anything youtube_dl supports)"""
        try :
            server = ctx.message.guild
            voice_channel = server.voice_client

            async with ctx.typing():
                player = await YTDLSource.from_url(url, loop=self.bot.loop)
                ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

            await ctx.send(f'Now playing: {player.title}')

        except:
            await ctx.send("The bot is not connected to a voice channel.")

    @commands.command(name='pause', help='How to pause the song')
    async def pause(self, ctx):
        """Pauses a voice from bot"""
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.pause()
        else:
            await ctx.send("The bot is not playing anything at the moment.")

    @commands.command(name='stop', help='How to stop the song')
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()

@client.event
async def on_ready():
		await client.change_presence(status = discord.Status.online, activity = discord.Game('Mezidia is the best!'))
		print('We have logged in as {0.user}'.format(client))

client.add_cog(Music(client))

keep_alive()
client.run(os.getenv('TOKEN'))
