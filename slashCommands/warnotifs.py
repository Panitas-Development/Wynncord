import discord
from discord.ext import commands
from discord import app_commands
from utils import command_logger
from guilds import get_guild
from warnotifsdata.data_comparision import tracked_guilds, set_traked_channel


class Warnotifs(app_commands.Group):

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

    @app_commands.command(name="fijarcanal",
                          description="Fija el canal en el que se ejecuta el comando para enviar las notificaciones de guerra.")
    async def fijarcanal(self, interaction: discord.Interaction):
        command_logger(interaction.user, '/fijarcanal', interaction.channel)
        set_traked_channel(interaction.channel_id)
        await interaction.response.send_message(f"Este canal ahora recibira notificaciones de guerra!", ephemeral=True)


async def setup(bot: commands.Bot):
    bot.tree.add_command(Warnotifs(name="warnotifs", description="Añade notificaciones de conquistas de territorios."))
