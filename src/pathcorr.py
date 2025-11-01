import pathlib
def to_correct(cmd: str) -> str:
    """
    приводит путь к стандартному виду  с помощью функций из pathlib
    далее проверка на абсолютный и относительный путь 
    """
    path = cmd.strip()
    pyti = pathlib.Path(path)
    if pyti.is_absolute():
        return str(pyti.resolve())
    if path.startswith('~'):
        pyti = pathlib.Path(path).expanduser()
    elif path.startswith(('.', '..')) or not path.startswith('/'):
        pyti = pathlib.Path.cwd() / path 
    return str(pyti.resolve())
