import os.path
import os 
import pathlib
def to_correct(cmd: str) -> str:
    path = cmd.strip()
    pyti = pathlib.Path(path)
    if pyti.is_absolute():
        return str(pyti.resolve())
    if path.startswith('~'):
        pyti = pathlib.Path(path).expanduser()
    elif path.startswith(('.', '..')) or not path.startswith('/'):
        pyti = pathlib.Path.cwd() / path 
    return str(pyti.resolve())
s=input()
print(to_correct(s))