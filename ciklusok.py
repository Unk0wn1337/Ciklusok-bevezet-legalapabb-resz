def ciklusok():
    index: int = 1
    while index <= 10:
        print(f"{index}Többé nem kések, mert lemaradok fontos információkról")
        index += 1
    index: int = 0
    print(index, " A ciklusan után")


def eloltesztelos_ciklus():
    szam: int = int(input("Adjon meg 10-nel nagyobb szám"))
    while szam <= 10:
        print("10 nél nagyobb számot")
        szam: int = int(input("Adjon meg egz 10-nél nagyobb számot"))
    print("Sikerult, kijutnu a gettóból")


def szamolasEgymasAla():
    index: int = 1
    while index < 11:
        print(index, end=",")
        index += 1


def szamEgymasAlaHuszEsHarminc():
    index: int = 20
    while index < 31:
        print(index, end=",")
        index += 1


def szamTizenotEsHuszonotKozott():
    index: int = 15
    szam: int = 2
    while index < 26:
        if index % szam == 0:
            print(index, end=",")
        index += 1

def szamTizenotEsHarminc():
    index: int = 12
    while index < 31:
       print(index, end = ",")
       index+=1

