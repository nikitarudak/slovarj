def loe_failist(f):
    """Loeme failist read ja lisame järjendisse
    """
    fail=open(f,"r",encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
