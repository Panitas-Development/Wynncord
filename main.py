import discord
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

client = discord.Client(intents=discord.Intents.default())

client.run(os.environ.get("TOKEN"))