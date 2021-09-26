import discord
from discord.ext import commands

def start(TOKEN: str, bot: commands.Bot):

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')


    @bot.command(name = "test", help = "Test current command in development")
    async def test(ctx: commands.Context):
        print(ctx.author)
        await ctx.send("TEST")
        await ctx.reply("hey hey")

    
    @bot.command(name = "summarize", help = "Summarize a subject")
    async def summarize(ctx: commands.Context):
        pass


    bot.run(TOKEN)