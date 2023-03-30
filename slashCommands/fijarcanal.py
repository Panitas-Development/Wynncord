import discord
from discord.ext import commands
from discord import app_commands
from utils import command_logger


class Fijarcanal(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="fijarcanal", description="Fija el canal en el que se ejecuta el comando para enviar las notificaciones de guerra.")
    async def fijarcanal(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Este canal ahora recibira notificaciones de guerra!")
        command_logger(interaction.user, '/fijarcanal', interaction.channel)


async def setup(bot: commands.Bot):
    await bot.add_cog(Fijarcanal(bot))
