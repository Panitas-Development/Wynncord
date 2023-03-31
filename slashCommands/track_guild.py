import discord
from discord.ext import commands
from discord import app_commands
from utils import command_logger
from guilds import get_guild

tracked_guilds = []

class Trackear_guilds(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='track_guild', description="Añade nueva guild a la lista de trackeo para notificaciones")
    @app_commands.describe(guild="Nombre de guild a trackear")
    async def track_guild(self, interaction: discord.Interaction, guild: str):
        command_logger(interaction.user, '/track_guild', interaction.channel)
        data = get_guild(guild)
        if not data:
            await interaction.response.send_message(f'No se ha encontrado la guild "{guild}".')
        else:
            tracked_guilds.append(data.name)
            await interaction.response.send_message(f'Se ha trackeado la guild "{data.name}" con exito!.')

    @app_commands.command(name='untrack_guild', description="Quita la guild de la lista de trackeos.")
    @app_commands.describe(guild="Nombre de guild a quitar")
    async def untrack_guild(self, interaction: discord.Interaction, guild: str):
        command_logger(interaction.user, '/untrack_guild', interaction.channel)
        if guild in tracked_guilds:
            tracked_guilds.remove(guild)
            await interaction.response.send_message(f'"{guild}" se ha removido con exito!.')
        else:
            await interaction.response.send_message(f'La guild "{guild}" no se encuentra en la lista de trackeos.')


async def setup(bot: commands.Bot):
    await bot.add_cog(Trackear_guilds(bot))
