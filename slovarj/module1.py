def loe_failist(file:str)->list:
    """Loeme failist read ja lisame järjendisse
    :param str f: faili nimetus
    """
    fail=open(f,"r",encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
def uus_sona(file:str,x:str):
    """Loeme failist read ja lisame järjendisse
    :param str f: faili nimetus
    """
    mas=[]
    with open(file,"a") as f:
        f.write(x+"\n")
    mas=loe_failist(file)
    return mas

