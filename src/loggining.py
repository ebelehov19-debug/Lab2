from logging import*
basicConfig(level=INFO, filename="shell.log",filemode="w",
                    format="[%(asctime)s] %(levelname)s: %(message)s")
def logcom(comnd=str,fl=bool,err=str)->None:
    if(fl): 
        info(comnd) 
    else:
        info(f'ERROR:{err}')


