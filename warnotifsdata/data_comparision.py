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


def get_coordinates(location: Location):
    coordinateX = (location.startX + location.endX) / 2
    coordinateY = (location.startY + location.endY) / 2

    return coordinateX, coordinateY


def get_time_captured(newdate: datetime, olddate: datetime):
    time_captured = newdate - olddate
    # Convertimos la diferencia de tiempo a días, horas, minutos y segundos
    dias = time_captured.days
    horas, segundos = divmod(time_captured.seconds, 3600)
    minutos, segundos = divmod(segundos, 60)

    # Creamos una lista con los componentes que queremos incluir en el resultado final
    componentes = [("días", dias), ("horas", horas), ("minutos", minutos), ("segundos", segundos)]

    # Creamos una lista con los componentes que tienen un valor distinto de cero
    componentes_no_cero = [f"{valor} {nombre}" for nombre, valor in componentes if valor != 0]

    # Imprimimos el resultado en formato "días:horas:minutos:segundos"
    resultado = " ".join(componentes_no_cero)

    return resultado


def embed_territorio(new_territory: Territory, old_territory: Territory, perdida: bool):
    coordinateX, coordinateY = get_coordinates(new_territory.location)

    color = 0x0fb31a
    if perdida: color = 0xf21c1c

    embed = discord.Embed(title=f"Capturado por: {new_territory.guild}",
                          url=f"https://www.wynncraft.com/stats/guild/{new_territory.guild.replace(' ', '%20')}",
                          color=color)
    embed.set_author(name=f'{new_territory.territory}',
                     url=f"https://map.wynncraft.com/#/{coordinateX}/64/{coordinateY}/-1/wynn-main/Wynncraft")
    embed.set_thumbnail(url="https://cdn.wynncraft.com/nextgen/wynncraft_icon.png")
    embed.add_field(name="Capturado hace:", value=discord.utils.format_dt(new_territory.acquired, style='R'),
                    inline=False)
    embed.add_field(name="Antiguo dueño:", value=old_territory.guild, inline=True)
    embed.add_field(name="Tiempo capturado:", value=get_time_captured(new_territory.acquired, old_territory.acquired),
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
            # Si el territorio es del mismo nombre y no tiene la misma guild
            if territory.territory == old_territory.territory and territory.guild != old_territory.guild:
                # si la guild del antiguo o nuevo territorio esta en los trackeos
                if territory.guild in tracked_guilds or old_territory.guild in tracked_guilds:
                    if territory.guild in tracked_guilds:
                        lost = False
                    elif old_territory in tracked_guilds:
                        lost = True
                    await bot.get_channel(track_channel).send(embed=embed_territorio(territory, old_territory, lost))

    old_data = data
