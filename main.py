from R2D2 import R2D2
import random

R2D2ArrayYoung = []
R2D2ArrayAdult = []
R2D2ArrayOld = []
deathcounter = []
newBorn = []
R2D2arraystring = []


#Creating those cuties
def CreateR2D2(loop):
    x = 0
    while x < loop:
        r1 = R2D2("Jung")
        R2D2ArrayYoung.append(r1)
        r1 = R2D2("Erwachsen")
        R2D2ArrayAdult.append(r1)
        r1 = R2D2("Alt")
        R2D2ArrayOld.append(r1)
        x += 1


#Creating those cuties
def createYoung(loop):
    counter = 0
    while counter < loop:
        r1 = R2D2("Jung")
        R2D2ArrayYoung.append(r1)
        counter += 1


#Getting Old
def Aging():
    while len(R2D2ArrayOld) > 0:
        r2d2 = R2D2ArrayOld.pop()
        children = r2d2.reproduced()
        newBorn.append(children)
        #print("Galaktische Zerstörung")
        deathcounter.append(1)

    while len(R2D2ArrayAdult) > 0:
        r2d2 = R2D2ArrayAdult.pop()
        children = r2d2.reproduced()
        newBorn.append(children)
        rand_num = random.randrange(0, 100)
        if rand_num >= 67:
            r2d2.set_age("Alt")
            R2D2ArrayOld.append(r2d2)
        else:
            #print("Galaktische Zerstörung")
            deathcounter.append(1)

    while len(R2D2ArrayYoung) > 0:
        r2d2 = R2D2ArrayYoung.pop()
        rand_num = random.randrange(0, 100)
        if rand_num >= 50:
            r2d2.set_age("Erwachsen")
            R2D2ArrayAdult.append(r2d2)
        else:
            #print("Galaktische Zerstörung")
            deathcounter.append(1)

    newborns = sum(newBorn)
    print("Reproduktion: " + str(newborns))
    createYoung(newborns)
    newBorn.clear()


#Provides Data from Arrays
def Analysis():
    print("Anzahl an Jungen R2D2s: " + str(len(R2D2ArrayYoung)))
    print("Anzahl an Erwachsenen R2D2s: " + str(len(R2D2ArrayAdult)))
    print("Anzahl an Alten R2D2s: " + str(len(R2D2ArrayOld)))
    deaths = sum(deathcounter)
    print(f"Insgesamt sind {deaths} R2D2s der Galaktischen zerstörung zum Opfer gefallen!")


def Error(msg):
    print(msg)


#Initializer for starting amount of R2D2s
def Initialize():
    try:
        anzahlR2D2s = int(input("Bitte Anzahl an Start R2D2s angeben "))
        CreateR2D2(anzahlR2D2s)
    except Exception:
        Error("Bitte einen Integer angeben")
        breakpoint()


#Algorithm itself
def Main():
    gen = 0
    Initialize()
    Analysis()
    while gen <= 30:
        Aging()
        print(f"Aktuelle Generation: {gen} ")
        Analysis()
        gen += 1


Main()
