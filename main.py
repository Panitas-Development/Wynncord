import discord
from discord.ext import commands
from utils import logger
from commandHandler import command_handler

# configuracion para usar archivo '.env'
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Configuracion del cliente
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    logger(f'Aplicacion funcionando con cliente: {bot.user}')
    await command_handler(bot)


bot.run(os.environ.get('TOKEN'))
