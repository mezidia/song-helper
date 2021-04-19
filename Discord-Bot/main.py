import os
import time
import asyncio
import discord
import youtube_dl
from keep_alive import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix=commands.when_mentioned_or("sh!"))

queueArray = []

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

    @commands.command(name='join', help='Joins bot to the channel')
    async def join(self, ctx):
        """Joins a voice channel"""
        if not ctx.message.author.voice:
            await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
            return
        else:
            channel = ctx.message.author.voice.channel
        await channel.connect()

    @commands.command(name='play', help='Bot will play the song')
    async def play(self, ctx, *, url):
        """Plays from a url (almost anything youtube_dl supports)"""
        try :
            async with ctx.typing():
                player = await YTDLSource.from_url(url, loop=self.bot.loop)
                voice_client = ctx.message.guild.voice_client
                if voice_client.is_playing():
                    global queueArray
                    queueArray.append(url)

                    await ctx.send(f'Song {player.title} has been added to the queue')
                else:
                    ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
                    await ctx.send(f'Now playing: {player.title}')

        except IndexError as e:
            await ctx.send("Something has happened!")
            print(e)

        seconds = 7
        time.sleep(seconds)
        # discord.FFmpegPCMAudio.cleanup(self)
        for file in os.listdir('./'):
            if file.split('.')[-1] in ['webm', 'm4a']:
                os.remove(file)

    # @commands.command(name='skip', help='Bot will sktp the song')
    # async def skip(self, ctx):
    #     """Skips current song and play next in queue"""
    #     stop(self, ctx)

    @commands.command(name='queue', help='Bot will show the queue')
    async def queue(self, ctx):
        """Shows the queue"""
        await ctx.send('Current queue has:')

        global queueArray
        await ctx.send(f'Your queue now is {queueArray}')
        #for song in queueArray:
        #    await ctx.send(song)

    @commands.command(name='remove', help='Bot will remove song from the queue')
    async def remove(self, ctx, number):
        """Removes song from the queue"""
        global queueArray
        try:
            del(queueArray[int(number)])
            await ctx.send(f'Your queue now is {queueArray}')
        
        except IndexError as e:
            await ctx.send("Your queue is either **empty** or the index is **out of range**")
            print(e)


    @commands.command(name='pause', help='Bot will pause the song')
    async def pause(self, ctx):
        """Pauses a voice from bot"""
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.pause()
        else:
            await ctx.send("The bot is not playing anything at the moment.")

    @commands.command(name='resume', help='Bot will resume the song')
    async def resume(self, ctx):
        """Resumes a voice from bot"""
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_paused():
            await voice_client.resume()
        else:
            await ctx.send("The bot was not playing anything before this. Use 'play' command")

    @commands.command(name='stop', help='Bot will stop the song')
    async def stop(self, ctx):
        """Stops a voice from bot"""
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.stop()
        else:
            await ctx.send("The bot is not playing anything at the moment.")

    #@commands.command(name='repeat', help='Bot will loop the song')
    #async def repeat(self, ctx):
    #    voice_client = ctx.message.guild.voice_client
    #    voice_client.play(audio, after=lambda e: Music.repeat(ctx.guild, #voice_client.voice, ctx.audio))
    #    voice_client.is_playing()
    #    await ctx.send("Current music will be repeated")

    @commands.command(name='leave', help='Bot will leave the voice channel')
    async def leave(self, ctx):
        """Stops and disconnects the bot from voice"""
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_connected():
            await voice_client.disconnect()
        else:
            await ctx.send("The bot is not connected to a voice channel.")

@client.event
async def on_ready():
		await client.change_presence(status = discord.Status.online, activity = discord.Game('Mezidia is the best!'))
		print('We have logged in as {0.user}'.format(client))

client.add_cog(Music(client))

keep_alive()
client.run(os.getenv('TOKEN'))
