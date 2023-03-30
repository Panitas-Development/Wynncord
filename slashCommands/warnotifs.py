import discord
from discord.ext import commands
from discord import app_commands


class Warnotifs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="fijarcanal", description="Fija el canal en el que se ejecuta el comando para enviar las notificaciones de guerra.")
    async def fijarcanal(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"{interaction.channel.name} se ha definido para enviar notificaciones de guerra.")


async def setup(bot: commands.Bot):
    await bot.add_cog(Warnotifs(bot))
