import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents = intents)

@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected to Discord!')


@bot.command(name = 'hello')
async def hello(cxt):
	await cxt.send('OK')
	await cxt.send(bot.users)


if __name__ == '__main__':
	bot.run(TOKEN)
