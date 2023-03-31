import discord
from datetime import datetime
from territories import get_territories
from territories.get_territories import Territory, Location


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

    embed = discord.Embed(title=f"Capturado por: {new_territory.guild}", url="https://www.instagram.com/p/CpoUOnDtlWB/",
                          color=color)
    embed.set_author(name="Temple of Legends",
                     url=f"https://map.wynncraft.com/#/{coordinateX}/64/{coordinateY}/-1/wynn-main/Wynncraft")
    embed.set_thumbnail(url="https://cdn.wynncraft.com/nextgen/wynncraft_icon.png")
    embed.add_field(name=".", value=".", inline=False)
    embed.add_field(name="Capturado hace:", value=discord.utils.format_dt(new_territory.acquired, style='R'),
                    inline=False)
    embed.add_field(name="Antiguo dueño:", value=old_territory.guild, inline=True)
    embed.add_field(name="Tiempo capturado:", value=get_time_captured(new_territory.acquired, old_territory.acquired),
                    inline=True)

    return embed


tracked_guilds = []
track_channel = ""
old_data = []


def data_comparision():
    new_data_comp = []
    old_data_comp = []

    global old_data
    data = get_territories()

    if len(old_data) == 0: old_data = data
    if data == old_data: return

    for territory in data:
        for old_territory in old_data:
            if territory.guild != old_territory.guild:
                if territory.guild in tracked_guilds or old_territory.guild in tracked_guilds:
                    new_data_comp.append(territory)
                    old_data_comp.append(old_territory)

    for i in range(len(new_data_comp)):
        if new_data_comp[i].guild in tracked_guilds:
            embed_territorio(new_data_comp[i], old_data_comp[i], perdida=False)

        if old_data_comp[i].guild in tracked_guilds:
            embed_territorio(new_data_comp[i], old_data_comp[i], perdida=True)
