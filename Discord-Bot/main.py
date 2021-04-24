import os
import time
import asyncio
import discord
import youtube_dl
from keep_alive import keep_alive
from discord.ext import commands


client = commands.Bot(command_prefix=commands.when_mentioned_or("sh!"))

queueArray = []
seconds = 7
status = 'Mezidia is the best!'

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
        try:
            if not ctx.message.author.voice:
                await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
                return
            else:
                channel = ctx.message.author.voice.channel
            await channel.connect()

        except IndexError as e:
            await ctx.send("Something wrong has happend during **join command!**")
            print(e)

    async def delete_songs(self):
        """Delete songs files"""
        try:
            time.sleep(seconds)
            # discord.FFmpegPCMAudio.cleanup(self)
            for file in os.listdir('./'):
                if file.split('.')[-1] in ['webm', 'm4a']:
                    os.remove(file)

        except IndexError as e:
            print(e)

    async def play_next(self, ctx):
        """Plays next song in queue after another"""
        try:
            global queueArray
            player = await YTDLSource.from_url(queueArray[0], loop=self.bot.loop)

            if len(queueArray) == 1:
                ctx.voice_client.play(player)
            
            elif len(queueArray) >= 2:
                ctx.voice_client.play(player, after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(ctx), loop = self.bot.loop))

            del queueArray[0]
            asyncio.run_coroutine_threadsafe(self.delete_songs(), loop = self.bot.loop)

        except IndexError as e:
            async with ctx.typing():
                await ctx.send("Your queue is either **empty** or the index is **out of range**")
            print(e)

    @commands.command(name='play', help='Bot will play the song')
    async def play(self, ctx, *, url):
        """Plays from a url (almost anything youtube_dl supports)"""
        try:
            async with ctx.typing():
                player = await YTDLSource.from_url(url, loop=self.bot.loop)
                voice_client = ctx.message.guild.voice_client
                if voice_client.is_playing():
                    global queueArray
                    queueArray.append(url)

                    await ctx.send(f'Song "{player.title}" has been added to the queue')
                else:
                    ctx.voice_client.play(player, after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(ctx), loop = self.bot.loop))
                    await ctx.send(f'Now playing: "{player.title}"')
                
                asyncio.run_coroutine_threadsafe(self.delete_songs(), loop = self.bot.loop)

        except IndexError as e:
            async with ctx.typing():
                await ctx.send("Something wrong has happend during **play command!**")
            print(e)

    @commands.command(name='queue', help='Bot will show the queue')
    async def queue(self, ctx):
        """Shows the queue"""
        async with ctx.typing():
            global queueArray
            await ctx.send(f'Your queue now is {queueArray}')

    @commands.command(name='remove', help='Bot will remove song from the queue')
    async def remove(self, ctx, number):
        """Removes song from the queue"""
        try:
            async with ctx.typing():
                global queueArray
                del(queueArray[int(number)])
                await ctx.send(f'Your queue now is {queueArray}')
        
        except IndexError as e:
            async with ctx.typing():
                await ctx.send("Your queue is either **empty** or the index is **out of range**")
            print(e)

    @commands.command(name='pause', help='Bot will pause the song')
    async def pause(self, ctx):
        """Pauses a voice from bot"""
        try:
            voice_client = ctx.message.guild.voice_client
            if voice_client.is_playing():
                await voice_client.pause()
            else:
                async with ctx.typing():
                    await ctx.send("The bot is not playing anything at the moment.")

        except IndexError as e:
            async with ctx.typing():
                await ctx.send("Something wrong has happend during **pause command!**")
            print(e)

    @commands.command(name='resume', help='Bot will resume the song')
    async def resume(self, ctx):
        """Resumes a voice from bot"""
        try:
            voice_client = ctx.message.guild.voice_client
            if voice_client.is_paused():
                await voice_client.resume()
            else:
                async with ctx.typing():
                    await ctx.send("The bot was not playing anything before this. Use 'play' command")

        except IndexError as e:
            async with ctx.typing():
                await ctx.send("Something wrong has happend during **resume command!**")
            print(e)

    @commands.command(name='stop', help='Bot will stop the song')
    async def stop(self, ctx):
        """Stops a voice from bot"""
        try:
            voice_client = ctx.message.guild.voice_client
            if voice_client.is_playing():
                await voice_client.stop()
            else:
                async with ctx.typing():
                    await ctx.send("The bot is not playing anything at the moment.")

        except IndexError as e:
            async with ctx.typing():
                await ctx.send("Something wrong has happend during **stop command!**")
            print(e)

    #@commands.command(name='repeat', help='Bot will loop the song')
    #async def repeat(self, ctx):
    #    voice_client = ctx.message.guild.voice_client
    #    voice_client.play(audio, after=lambda e: Music.repeat(ctx.guild, #voice_client.voice, ctx.audio))
    #    voice_client.is_playing()
    #    await ctx.send("Current music will be repeated")

    @commands.command(name='leave', help='Bot will leave the voice channel')
    async def leave(self, ctx):
        """Stops and disconnects the bot from voice"""
        try:
            voice_client = ctx.message.guild.voice_client
            if voice_client.is_connected():
                await voice_client.disconnect()
            else:
                async with ctx.typing():
                    await ctx.send("The bot is not connected to a voice channel.")

        except IndexError as e:
            async with ctx.typing():
                await ctx.send("Something wrong has happend during **leave command!**")
            print(e)

@client.event
async def on_ready():
    """Invokes, when bot is hosted"""
    try:
		    await client.change_presence(status = discord.Status.online, activity = discord.Game(status))
		    print('We have logged in as {0.user}'.format(client))

    except IndexError as e:
        print(e)

client.add_cog(Music(client))

keep_alive()
client.run(os.getenv('TOKEN'))
