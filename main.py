from discord.ext import commands
import initialization
import myDiscordBot


if __name__ == '__main__':
	TOKEN: str
	bot: commands.Bot
	TOKEN, bot = initialization.initialize()
	myDiscordBot.start(TOKEN, bot)