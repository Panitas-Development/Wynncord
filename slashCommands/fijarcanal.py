import discord
from discord.ext import commands
from discord import app_commands
from utils import command_logger


class Fijarcanal(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #TODO obtener canal para fijar las notificaciones.
    @app_commands.command(name="fijarcanal", description="Fija el canal en el que se ejecuta el comando para enviar las notificaciones de guerra.")
    async def fijarcanal(self, interaction: discord.Interaction):
        command_logger(interaction.user, '/fijarcanal', interaction.channel)
        await interaction.response.send_message(f"Este canal ahora recibira notificaciones de guerra!")



async def setup(bot: commands.Bot):
    await bot.add_cog(Fijarcanal(bot))
