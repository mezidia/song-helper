import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
import youtube_dl

client = commands.Bot(command_prefix='sh!')

players = {}

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.command()
async def join(ctx):
	channel = ctx.author.voice.channel
	await channel.connect()

@client.command()
async def leave(ctx):
	await ctx.voice_client.disconnect()

@client.command()
async def play(ctx, url: str):
	server = ctx.message.server
	player = await ctx.voice_client.create_ytdl_player(url)
	players[server.id] = player
	player.start

keep_alive()
client.run(os.getenv('TOKEN'))