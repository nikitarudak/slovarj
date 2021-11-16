from module1 import *
rus_list=loe_failist("rus.txt")
est_list=loe_failist("est.txt")
print(rus_list)
print(est_list)

while True:
    menu=input("Tõlgida - T,\nUus sõna - U\nViga - V\nKontroll - K\nLõpp - L\n")
    if menu.upper()=="T":
        pass
    elif menu.upper()=="U":
        rus_list=uus_sona("rus.txt",input("Новое слово: "))
        est_list=uus_sona("est.txt",input("Uus sõna: "))
        pass
    elif menu.upper()=="V":
        pass
    elif menu.upper()=="K":
        pass
    else:
        break