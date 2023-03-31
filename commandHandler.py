from discord.ext import commands
from os import listdir
from utils import logger


def get_command_modules():
    commands = []
    for file in listdir("./slashCommands"):
        if file.endswith(".py"):
            commands.append(file[:-3])

    return commands


async def command_handler(bot: commands.Bot):
    for command in get_command_modules():
        await bot.load_extension(f"slashCommands.{command}")
    try:
        synced = await bot.tree.sync()
        logger(f"Se han sincronizado {len(synced)} archivos de comandos.")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    print(get_command_modules())