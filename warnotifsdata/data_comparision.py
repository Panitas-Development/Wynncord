import discord
from discord.ext import commands
from datetime import datetime
from territories import get_territories
from territories.get_territories import Territory, Location

tracked_guilds = []
track_channel = None
old_data = []


def set_traked_channel(id: int):
    global track_channel
    track_channel = id


def get_web_coordinates(location: Location):
    coordinateX = (location.startX + location.endX) / 2
    coordinateY = (location.startY + location.endY) / 2

    return coordinateX, coordinateY


def get_time_captured(newdate: datetime, olddate: datetime):
    time_captured = newdate - olddate
    # Convert the time difference into days, hours, minutes, and seconds
    days = time_captured.days
    hours, seconds = divmod(time_captured.seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    # Create a list with the components we want to include in the final result
    components = [("days", days), ("hours", hours), ("minutes", minutes), ("seconds", seconds)]

    # Create a list with the components that have a non-zero value
    non_zero_components = [f"{value} {name}" for name, value in components if value != 0]

    # Print the result in the format "days:hours:minutes:seconds"
    result = " ".join(non_zero_components)

    return result


def embed_territory(new_territory: Territory, old_territory: Territory, loss: bool):
    coordinateX, coordinateY = get_coordinates(new_territory.location)

    color = 0x0fb31a
    if loss: 
        color = 0xf21c1c

    embed = discord.Embed(title=f"Captured by: {new_territory.guild}",
                          url=f"https://www.wynncraft.com/stats/guild/{new_territory.guild.replace(' ', '%20')}",
                          color=color)
    embed.set_author(name=f'{new_territory.territory}',
                     url=f"https://map.wynncraft.com/#/{coordinateX}/64/{coordinateY}/-1/wynn-main/Wynncraft")
    embed.set_thumbnail(url="https://cdn.wynncraft.com/nextgen/wynncraft_icon.png")
    embed.add_field(name="Captured at:", value=discord.utils.format_dt(new_territory.acquired, style='R'),
                    inline=False)
    embed.add_field(name="Former owner:", value=old_territory.guild, inline=True)
    embed.add_field(name="Time captured:", value=get_time_captured(new_territory.acquired, old_territory.acquired),
                    inline=True)

    return embed



async def data_comparision(bot: commands.Bot):
    if track_channel is None:
        return

    global old_data
    data = get_territories()
    if len(old_data) == 0: old_data = data

    for territory in data:
        for old_territory in old_data:
            if territory.territory == old_territory.territory and territory.guild != old_territory.guild:
                if territory.guild in tracked_guilds or old_territory.guild in tracked_guilds:
                    if territory.guild in tracked_guilds:
                        lost = False
                    elif old_territory.guild in tracked_guilds:
                        lost = True
                    await bot.get_channel(track_channel).send(embed=embed_territory(territory, old_territory, lost))

    old_data = data
