import requests as requests
from utils import logger
from datetime import datetime
from dateutil import tz


class Location:
    def __init__(self, startX: int, startY: int, endX: int, endY: int):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY

    def __str__(self):
        return f"({self.startX}, {self.startY}) - ({self.endX}, {self.endY})"


class Territory:
    def __init__(self, territory: str, guild: str, guildPrefix: str, acquired: str, location: dict):
        self.territory = territory
        self.guild = guild
        self.guildPrefix = guildPrefix
        self.acquired = convert_datetime(datetime.strptime(acquired, '%Y-%m-%d %H:%M:%S'))
        self.location = Location(**location)

    def __str__(self):
        return f"{self.territory} ({self.guildPrefix} {self.guild}) acquired on {self.acquired} at {self.location}"


def convert_datetime(utc):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    utc = utc.replace(tzinfo=from_zone)

    return utc.astimezone(to_zone)


def get_territories():
    """
    Obtiene todos los territorios desde la api de Wynncraft.
    Retorna una lista de objetos con estos.
    """
    request = requests.get(
        'https://api.wynncraft.com/public_api.php?action=territoryList').json()
    territories = request['territories']
    data = [Territory(**territories[name]) for name in territories]
    logger("Funcion 'get_territories' ha llamado a la api con exito!.")
    return data
