import discord
from discord.ext import commands

def start(TOKEN: str, bot: commands.Bot):

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')


    @bot.command(name = 'hello')
    async def hello(ctx: commands.Context):
        await ctx.send('OK')

    bot.run(TOKEN)
    print("xd")