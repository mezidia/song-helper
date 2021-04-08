import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

client = commands.Bot(command_prefix = 'sh!')

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.command()
async def join(ctx):
	channel = ctx.author.voice.channel
	print(channel)
	await channel.connect()

@client.command()
async def leave(ctx):
	await ctx.voice_client.disconnect()

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('sh!hello'):
		await message.channel.send('Hi!')

keep_alive()
client.run(os.getenv('TOKEN'))