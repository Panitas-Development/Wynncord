import requests as requests
from utils import logger


class Location:
    def __init__(self, startX: int, startY: int, endX: int, endY: int):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY


class Territory:
    def __init__(self, territory: str, guild: str, guildPrefix: str, acquired: str, location: dict):
        self.territory = territory
        self.guild = guild
        self.guildPrefix = guildPrefix
        self.acquired = acquired
        self.location = Location(**location)


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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for territory in get_territories():
        print(territory.guild)