import os
from typing import Tuple
import discord
from dotenv import load_dotenv
from discord.ext import commands

def initialize() -> Tuple[str, commands.Bot]:
    load_dotenv()
    TOKEN: str = os.getenv('DISCORD_TOKEN')

    intents: discord.Intents = discord.Intents.default()
    intents.members = True
    bot: commands.Bot = commands.Bot(command_prefix='!', intents = intents)
    return TOKEN, bot