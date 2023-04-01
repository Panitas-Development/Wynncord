def logger(text):
    """
    Returns a log with [Wynncord]
    """
    print(f'\x1b[0;30;45m[Wynncord]\x1b[0m {text}')


def command_logger(user: str, command: str, channel: str):
    """
    Generates a log with a command structure
    """
    logger(
        f'El usuario \x1b[5;37;41m{user}\x1b[0m ha usado el comando \x1b[5;37;41m{command}\x1b[0m en el canal \x1b[5;37;41m#{channel}\x1b[0m')
