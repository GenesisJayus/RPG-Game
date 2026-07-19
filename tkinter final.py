from tkinter import *
import time

#Player Status
name = "Jack"
ap = 10
#-----
nap = 10

#Player atributes
stre = 0 #extra damage you do 
dfs = 0 #less damage you take
agi = 5 #chance of evading a hit
vit = 100 #your HP
itl = 60 #your mana
dex = 10 #your energy
#---------------------------
nstre = 0 #extra damage you do 
ndfs = 0 #less damage you take
nagi = 0 #chance of evading a hit
nvit = 0 #your HP
nitl = 0 #your mana
ndex = 0 #your energy


window = Tk()
window.geometry("720x480")
window.title("Text Based RPG Game")

def start():
    wc.pack()
    wcb.pack()

def dadael(*widgets):
    for widget in widgets:
        widget.destroy()

def subName():
    global name
    name = nameEnter.get()
    confirmed = Label(window, text = f"welcome to RPG Game {name}")
    confBut = Button(window, text = "click to continue", command = lambda: (dadael(confirmed, confBut), atribUp()))
    confirmed.pack()
    confBut.pack()

    


def Phase2():
    cc.pack() 
    nameEnter.pack()
    nameOk.pack()

#------Phase 1--------
wc = Label(window, text = "Welcome to the RPG Game ^^ \n \n Click the button below to Start the game")
wcb = Button(window, text = "Start Game ->", command = lambda: (dadael(wc, wcb), Phase2()))

#-------Phase 2--------

#-------2a-------
cc = Label(window, text = "May I know your name Player?")
nameEnter = Entry(window)
nameOk = Button(window, text = "Confirm", command = lambda: (subName(), dadael(cc, nameEnter, nameOk)))

#-------2b-------
#-------------------------------


def noAp():
    noAp = Label(window, text="You don't have enough atribute points")
    noAp.grid(column= 3, row=10, columnspan = 6, sticky= "se")
    window.after(1500, lambda: dadael(noAp))

atribPoints = Label(window, text=f"Atrribute Points Remaining {ap}")

#---strength---

def strPlus():
    global stre, nstre, ap
    if ap != 0:
        nstre += 1
        ap -= 1
        stronk.config(text=f"+ {nstre}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
    else:
        noAp()

def strMinu():
    global stre, nstre, ap
    if nstre >= 2:
        nstre -= 1
        ap += 1
        stronk.config(text=f"+ {nstre}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
    elif nstre == 1:
        nstre -= 1
        ap += 1
        stronk.config(text="")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
    
    

strPls = Button(window, text="strength +1", command=strPlus)
strMin = Button(window, text="strength -1", command=strMinu)
streStat = Label(window, text = f"Strength: {stre}")
stronk = Label(window, text=f"")

#---defense---

def dfsPlus():
    global dfs, ndfs, ap
    if ap != 0:
        ndfs += 1
        ap -= 1
        tanky.config(text=f"+ {ndfs}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
    else:
        noAp()

def dfsMinu():
    global dfs, ndfs, ap
    if ndfs >= 2:
        ndfs -= 1
        ap += 1
        tanky.config(text=f"+ {ndfs}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
    elif ndfs == 1:
        ndfs -= 1
        ap += 1
        tanky.config(text=f"")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
    

dfsPls = Button(window, text="Defense +1", command=dfsPlus)
dfsMin = Button(window, text="Defense -1", command=dfsMinu)
dfsStat = Label(window, text = f"Defense: {dfs}")
tanky = Label(window, text=f"")


#---agility---

def agiPlus():
    global agi, nagi, ap
    if ap != 0:
        nagi += 1
        ap -= 1
        nimble.config(text=f"+ {nagi}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
    else:
        noAp()

def agiMinu():
    global agi, nagi, ap
    if nagi >= 2:
        nagi -= 1
        ap += 1
        nimble.config(text=f"+ {nagi}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
    elif nagi == 1:
        nagi -= 1
        ap += 1
        nimble.config(text=f"")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")

agiPls = Button(window, text="Agility +1", command=agiPlus)
agiMin = Button(window, text="Agility -1", command=agiMinu)
agiStat = Label(window, text= f"Agility: {agi}")
nimble = Label(window, text=f"")


#---vitality---

def vitPlus():
    global vit, nvit, ap
    if ap != 0:
        nvit += 1
        ap -= 1
        healthy.config(text=f"+ {nvit}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
    else:
        noAp()

def vitMinu():
    global vit, nvit, ap
    if nvit >= 2:
        nvit -= 1
        ap += 1
        healthy.config(text=f"+ {nvit}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
    elif nvit == 1:
        nvit -= 1
        ap += 1
        healthy.config(text=f"")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")


vitPls = Button(window, text="Vitality +1", command=vitPlus)
vitMin = Button(window, text="Vitality -1", command=vitMinu)
vitStat = Label(window, text = f"Vitality: {vit}")
healthy = Label(window, text=f"")


#---intelligence---

def itlPlus():
    global itl, nitl, ap
    if ap != 0:
        nitl += 1
        ap -= 1
        smart.config(text=f"+ {nitl}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
    else:
        noAp()

def itlMinu():
    global itl, nitl, ap
    if nitl >= 2:
        nitl -= 1
        ap += 1
        smart.config(text=f"+ {nitl}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
    elif nitl == 1:
        nitl -= 1
        ap += 1
        smart.config(text=f"")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
    

itlPls = Button(window, text="Intelligence +1", command=itlPlus)
itlMin = Button(window, text="Intelligence -1", command=itlMinu)
itlStat = Label(window, text = f"Intelligence: {itl}")
smart = Label(window, text=f"")


#---dexterity---

def dexPlus():
    global dex, ndex, ap
    if ap != 0:
        ndex += 1
        ap -= 1
        dodgy.config(text=f"+ {ndex}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
    else:
        noAp()

def dexMinu():
    global dex, ndex, ap
    if ndex >= 2:
        ndex -= 1
        ap += 1
        dodgy.config(text=f"+ {ndex}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
    elif ndex == 1:
        ndex -= 1
        ap += 1
        dodgy.config(text=f"")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
    

dexPls = Button(window, text="Dexterity +1", command=dexPlus)
dexMin = Button(window, text="Dexterity -1", command=dexMinu)
dexStat = Label(window, text = f"Dexterity: {dex}")
dodgy = Label(window, text=f"")

#--------------------------------------
def atribUp():

    window.columnconfigure((2), weight = 2)
    window.columnconfigure((1,3,4,5,6), weight = 1)
    window.rowconfigure((1,2,3,4,5,6,7,8,9), weight = 1)
    window.rowconfigure(10, minsize= 40 , weight= 1)

    atribPoints.grid(column = 1, row = 1, columnspan= 2, sticky = "nw")

    streStat.grid(column = 2, row = 2, sticky = "snw")
    stronk.grid(column = 3, row = 2, sticky = "nsw")
    strPls.grid(column = 4, row = 2, sticky = "nse")
    strMin.grid(column = 5, row = 2, sticky = "nsw")

    dfsStat.grid(column = 2, row = 3, sticky = "nsw")
    tanky.grid(column = 3, row = 3, sticky = "nsw")
    dfsPls.grid(column = 4, row = 3, sticky = "nse")
    dfsMin.grid(column = 5, row = 3, sticky = "nsw")

    agiStat.grid(column = 2, row = 4, sticky = "nsw")
    nimble.grid(column = 3, row = 4, sticky = "nsw")
    agiPls.grid(column = 4, row = 4, sticky = "nse")
    agiMin.grid(column = 5, row = 4, sticky = "nsw")

    vitStat.grid(column = 2, row = 5, sticky = "nsw")
    healthy.grid(column = 3, row = 5, sticky = "nsw")
    vitPls.grid(column = 4, row = 5, sticky = "nse")
    vitMin.grid(column = 5, row = 5, sticky = "nsw")

    itlStat.grid(column = 2, row = 6, sticky = "nsw")
    smart.grid(column = 3, row = 6, sticky = "nsw")
    itlPls.grid(column = 4, row = 6, sticky = "nse")
    itlMin.grid(column = 5, row = 6, sticky = "nsw")

    dexStat.grid(column = 2, row = 7, sticky = "nsw")
    dodgy.grid(column = 3, row = 7, sticky = "nsw")
    dexPls.grid(column = 4, row = 7, sticky = "nse")
    dexMin.grid(column = 5, row = 7, sticky = "nsw")

start()

window.mainloop()

# --------------------------------------

def AttribConfirm():
    global ap
    attCon.grid_forget()
    if ap == 0:
        a = Label(window, text = "Confirm Stats?")
    elif ap != 1:
        a = Label(window, text= f"You have {ap} attribute points left, are you sure?")

    def yes():
        global stre, dfs, agi, itl, dex, vit, ap
        global nstre, ndfs, nagi, nitl, ndex, nvit, nap
        dadael(a, b, c, atribPoints, attCon, streStat, stronk, strPls, strMin, dfsStat, tanky, dfsMin, dfsPls, vitStat, vitMin, vitPls, healthy, dexStat, dexPls, dexMin, dodgy, agiStat, agiMin, agiPls, nimble, itlStat, itlPls, itlMin, smart )
        dfs = dfs + ndfs
        stre = stre + nstre
        agi = agi + nagi
        vit = vit + nvit
        itl = itl + nitl
        dex = dex + ndex
        ndfs = 0
        nstre = 0
        nagi = 0
        nvit = 0
        nitl = 0
        ndex = 0
        d = Label(window, text="confirmed")
        d.grid(column= 2, row= 10, rowspan= 2, sticky= "swe")
        window.after(1500, lambda: dadael(d))
        e = Label(window, text=f"Your Stats are now: \n Strength: {stre} \n Defense: {dfs} \n Agility: {agi} \n Vitality: {vit} \n Intelligence: {itl} \n Dexterity: {dex}")
        window.after(1500, lambda: e.grid())

    def no():
        dadael(a, b, c)
        attCon.grid(column= 2, row= 10, rowspan= 2, sticky= "swe")
   
    b = Button(window, text = "yes", command=yes)
    c = Button(window, text= "no", command=no)

    a.grid()
    b.grid()
    c.grid()


attCon = Button(window, text="Confirm", command= lambda: AttribConfirm())




"""
Phase 1 = Welcome screen, welcomes player /
Phase 2 = character creation 
    2a - name of character /
    2b - attributes 
    2c - story line **
Phase 3 = game start **
"""