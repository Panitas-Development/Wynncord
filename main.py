import discord
from discord.ext import commands
from utils import logger

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Configuracion del cliente
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)

# Setup al iniciar el bot


@bot.event
async def on_ready():
    logger(f'Aplicacion funcionando con cliente: {bot.user}')
    await bot.load_extension("slashCommands.warnotifs")
    try:
        synced = await bot.tree.sync()
        logger(f"Se han sincronizado {len(synced)} comandos.")
    except Exception as e:
        print(e)


bot.run(os.environ.get('TOKEN'))
