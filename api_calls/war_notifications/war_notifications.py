import requests as requests


class Location:
    def __init__(self, startX: int, startY: int, endX: int, endY: int):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY


class Territory:
    def __init__(self, territory: str, guild: str, guildPrefix: str, acquired: str, location: Location):
        self.territory = territory
        self.guild = guild
        self.guildPrefix = guildPrefix
        self.acquired = acquired
        self.location = location


class Territory2:
    def __init__(self, territory: str, guild: str, guildPrefix: str, acquired: str, location: dict):
        self.territory = territory
        self.guild = guild
        self.guildPrefix = guildPrefix
        self.acquired = acquired
        self.location = Location(**location)


tracked_guild = 'Taberna Hispana'
request = requests.get('https://api.wynncraft.com/public_api.php?action=territoryList').json()
territories = request['territories']
data = [Territory2(**territories[name]) for name in territories]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for territory in data:
        print(territory.guild)