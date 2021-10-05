import re
from typing import Dict, List
import discord
from discord.ext import commands
import webScrapper

def start(TOKEN: str, bot: commands.Bot):

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')


    @bot.command(name = "test", help = "Test current command in development")
    async def test(ctx: commands.Context):
        print(ctx.author)
        await ctx.reply("hey hey")

    
    @bot.command(name = "summarize", help = "Summarize a subject")
    async def summarize(ctx: commands.Context, search_arg):
        information_from_pages: List[Dict] = webScrapper.gahter_information(webScrapper.get_links(search_arg))
        for information_from_page in information_from_pages:
            paragraphs_from_page = information_from_page['paragraphs']
            for paragraph in paragraphs_from_page:
                await ctx.reply(paragraph)
            await ctx.reply(information_from_page['link'])
        await ctx.reply('FIN')


    bot.run(TOKEN)