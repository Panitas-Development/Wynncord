import discord
from discord.ext import commands
from discord import app_commands
from utils import command_logger
from guilds import get_guild
from warnotifsdata.json_data import add_tracking, rm_tracking


class Warnotifs(app_commands.Group):
    @app_commands.command(name='trackguild', description="Adds a new guild to the tracking list for notifications.")
    @app_commands.describe(guild="Name of the guild to be tracked.")
    async def track_guild(self, interaction: discord.Interaction, guild: str):
        command_logger(interaction.user, '/trackguild', interaction.channel)
        data = get_guild(guild)
        if not data:
            await interaction.response.send_message(f'Guild "{guild}" not found.')
        else:
            add_tracking(data.name, interaction.channel_id)
            await interaction.response.send_message(f'Guild "{data.name}" has been successfully added to the tracking list.')

    @app_commands.command(name='untrackguild', description="Removes a guild from the tracking list.")
    @app_commands.describe(guild="Name of the guild to be removed.")
    async def untrack_guild(self, interaction: discord.Interaction, guild: str):
        command_logger(interaction.user, '/untrackguild', interaction.channel)
        if rm_tracking(guild):
            await interaction.response.send_message(f'Guild "{guild}" has been successfully removed.')
        else:
            await interaction.response.send_message(f'Guild "{guild}" is not in the tracking list of the channel.')


async def setup(bot: commands.Bot):
    bot.tree.add_command(Warnotifs(
        name="war", description="Adds notifications of territory conquests."))
