import re
import os
import discord
import webScrapper
from dotenv import load_dotenv
from typing import Dict, List
from discord.ext import commands


def start():
    load_dotenv()
    TOKEN: str = os.getenv('DISCORD_TOKEN')

    intents: discord.Intents = discord.Intents.default()
    intents.members = True
    bot: commands.Bot = commands.Bot(command_prefix='!', intents = intents)


    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')


    @bot.command(name = "test", help = "Test current command in development")
    async def test(ctx: commands.Context):
        print(ctx.author)
        await ctx.reply("hey hey")

    
    @bot.command(name = "search", help = "google search")
    async def summarize(ctx: commands.Context, search_arg, number_p_per_link_arg = 3, number_links_arg = 5):
        information_from_pages: List[Dict] = webScrapper.gahter_information(webScrapper.get_links(search_arg))
        current_number_links: int = 0
        for information_from_page in information_from_pages:
            paragraphs_from_page = information_from_page['paragraphs']
            current_number_p: int = 0
            for paragraph in paragraphs_from_page:
                await ctx.reply(paragraph)
                current_number_p += 1
                if current_number_p >= number_p_per_link_arg:
                    break
            await ctx.reply(information_from_page['link'])
            current_number_links += 1
            if current_number_links >= number_links_arg:
                break
        await ctx.reply('FIN')


    @bot.event
    async def on_command_error(ctx: commands.Context, exception):
        await ctx.reply(exception)

    bot.run(TOKEN)