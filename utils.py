def logger(text):
    """
    Genera un print anteponiendo '[Taberna Hispana]'
    """
    print(f'\x1b[0;30;45m[Taberna Hispana]\x1b[0m {text}')


def command_logger(usuario: str, comando: str, canal: str):
    """
    Genera un print especial para logs de comandos
    """
    logger(
        f'El usuario \x1b[5;37;41m{usuario}\x1b[0m ha usado el comando \x1b[5;37;41m{comando}\x1b[0m en el canal \x1b[5;37;41m{canal}\x1b[0m')
