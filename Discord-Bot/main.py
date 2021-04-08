import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

client = commands.Bot(command_prefix = 'sh!')

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.command(pass_context=True)
async def join(ctx):
	channel = ctx.message.author.voice.voice_channel
	await client.join_voice_channel(channel)

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('sh!hello'):
		await message.channel.send('Hi!')

keep_alive()
client.run(os.getenv('TOKEN'))