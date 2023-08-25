import discord
from discord import app_commands, ui
from discord.ui import Modal
from discord.ext import commands, tasks
from colorama import Back, Fore, Style
import time
from discord.utils import format_dt
import platform
from colorama import Back, Fore, Style
import json

with open('config.json', 'r') as f:
    data = json.load(f)
    token_discord_bot = data['token']
    version_discord_bot = data['version']
    status_discord_bot = data['status']
    prefix_discord_bot = data['prefix_bot']
    
# Créez une instance de bot
bot = commands.Bot(command_prefix=str(prefix_discord_bot), intents=discord.Intents.all(), help_command=None)



# Événement on_ready : appelé lorsque le bot est prêt
prfx = (
    Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S UTC", time.gmtime())
    + Back.RESET + Fore.WHITE + Style.BRIGHT
)


@bot.event
async def on_ready():
    changeStatus.start()
    print(prfx + " Connection de " + Fore.YELLOW + bot.user.name)
    print(prfx + " Bot ID " + Fore.YELLOW + str(bot.user.id))
    print(prfx + " Status " + Fore.YELLOW + str(status_discord_bot))
    print(prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
    print(prfx + " Python Version " + Fore.YELLOW +
          str(platform.python_version()))


@tasks.loop(seconds=120)
async def changeStatus():
    servers = len(bot.guilds)
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1

    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name=f"Prefix: {prefix_discord_bot} | {members} membres"))




# Lancer le bot
bot.run(str(token_discord_bot))
