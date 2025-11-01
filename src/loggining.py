from logging import*
"""
Базовые настройки логгирования и функция для логгирования 
"""
basicConfig(level=INFO, filename="shell.log",filemode="w",
                    format="[%(asctime)s] %(levelname)s: %(message)s")
def logcom(comnd=str,fl=bool,err=str)->None:
    """
    логгирует либо на уровне info при удачном выполнении или error при неверном выполнении 
    """
    if(fl): 
        info(comnd) 
    else:
        error(f'{err}')


