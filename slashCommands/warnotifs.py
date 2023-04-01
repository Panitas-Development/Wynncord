import discord
from discord.ext import commands
from discord import app_commands
from utils import command_logger
from guilds import get_guild
from warnotifsdata.data_comparision import tracked_guilds, set_traked_channel


class Warnotifs(app_commands.Group):
    @app_commands.command(name='track_guild', description="Adds a new guild to the tracking list for notifications.")
    @app_commands.describe(guild="Name of the guild to be tracked.")
    async def track_guild(self, interaction: discord.Interaction, guild: str):
        command_logger(interaction.user, '/track_guild', interaction.channel)
        data = get_guild(guild)
        if not data:
            await interaction.response.send_message(f'Guild "{guild}" not found.')
        else:
            tracked_guilds.append(data.name)
            await interaction.response.send_message(f'Guild "{data.name}" has been successfully added to the tracking list.')

    @app_commands.command(name='untrack_guild', description="Removes a guild from the tracking list.")
    @app_commands.describe(guild="Name of the guild to be removed.")
    async def untrack_guild(self, interaction: discord.Interaction, guild: str):
        command_logger(interaction.user, '/untrack_guild', interaction.channel)
        if guild in tracked_guilds:
            tracked_guilds.remove(guild)
            await interaction.response.send_message(f'Guild "{guild}" has been successfully removed.')
        else:
            await interaction.response.send_message(f'Guild "{guild}" is not in the tracking list.')

    @app_commands.command(name="set_channel",
                          description="Sets the channel in which to send war notifications.")
    async def set_channel(self, interaction: discord.Interaction):
        command_logger(interaction.user, '/set_channel', interaction.channel)
        set_traked_channel(interaction.channel_id)
        await interaction.response.send_message(f"This channel will now receive war notifications!", ephemeral=True)


async def setup(bot: commands.Bot):
    bot.tree.add_command(Warnotifs(
        name="warnotifs", description="Adds notifications of territory conquests."))
