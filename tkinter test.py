from tkinter import *
import time

#Player Status
name = ""
ap = 10
#-----
nap = 10

'''
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
'''

def dadael(*widgets):
    for widget in widgets:
        widget.destroy()
def lipat(*widgets):
    for widget in widgets:
        widget.grid_forget()
def wipe():
    for widget in window.winfo_children():
        widget.destroy()

window = Tk()
window.geometry("720x480")
window.title("Text Based RPG Game")
window.resizable(False, False)

'''
frame = Frame(window, width= "500", height= "300", bg="grey")

welcome = Label(window, text = "Welcome to [insert place]")
nextPage = Label(window, text = "This is the next page")

def conti():
    welcome.forget()
    nextPage.pack()
    cont.forget()

cont = Button(window, text = "Click Here to Continue", command = conti)

inputBox = Entry(window)
inputStart = Label(window, text = "Please enter your name")
inputLabel = Label(window, text = "")

def submitName():
    a = inputBox.get()
    inputLabel.config(text = f"Welcome {a}")
    inputStart.forget()
    inputLabel.pack()
    inputBox.forget()
    inputButton.forget()
    inputStart.forget()
    
inputButton = Button(window, text = "confirm", command=submitName)

#welcome.pack()
#cont.pack()
#inputBox.pack()
#inputStart.pack()
#inputButton.pack()

# ------ Live update Button ------

strength = 0
def strPlus():
    global strength
    strength += 1
    stre.config(text=f"Strength = {strength}")

def strMin():
    global strength
    strength -= 1
    stre.config(text=f"Strength = {strength}")
    

strPls = Button(window, text="strength +1", command=strPlus)
strMin = Button(window, text="strength -1", command=strMin)

stre = Label(window, text=f"Strength = {strength}")

#stre.pack()
#strPls.pack()
#strMin.pack()


#-------------------------------
acl = Label(window, text="")
bcl = Label(window, text="")
ccl = Label(window, text="")

def noAp():
    noAp = Label(frame, text="You don't have enough\n atribute points")
    noAp.grid(column= 3, row=10, columnspan = 3, rowspan= 2, sticky= 'e', padx= (0,20))
    frame.after(1500, lambda: dadael(noAp))

atribPoints = Label(frame, text=f"Atrribute Points Remaining {ap}")

#---strength---

def strPlus():
    global stre, nstre, ap, acl, bcl, ccl
    if ap != 0:
        nstre += 1
        ap -= 1
        stronk.config(text=f"+ {nstre}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')
    else:
        noAp()
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')

def strMinu():
    global stre, nstre, ap, acl, bcl, ccl
    if nstre >= 2:
        nstre -= 1
        ap += 1
        stronk.config(text=f"+ {nstre}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')
    elif nstre == 1:
        nstre -= 1
        ap += 1
        stronk.config(text="")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')
    
    

strPls = Button(frame, text="strength +1", command=strPlus)
strMin = Button(frame, text="strength -1", command=strMinu)
streStat = Label(frame, text = f"Strength: {stre}")
stronk = Label(frame, text=f"")

#---defense---

def dfsPlus():
    global dfs, ndfs, ap, acl, bcl, ccl
    if ap != 0:
        ndfs += 1
        ap -= 1
        tanky.config(text=f"+ {ndfs}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')
    else:
        noAp()
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')

def dfsMinu():
    global dfs, ndfs, ap, acl, bcl, ccl
    if ndfs >= 2:
        ndfs -= 1
        ap += 1
        tanky.config(text=f"+ {ndfs}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')
    elif ndfs == 1:
        ndfs -= 1
        ap += 1
        tanky.config(text=f"")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')
    

dfsPls = Button(frame, text="Defense +1", command=dfsPlus)
dfsMin = Button(frame, text="Defense -1", command=dfsMinu)
dfsStat = Label(frame, text = f"Defense: {dfs}")
tanky = Label(frame, text=f"")

#---agility---

def agiPlus():
    global agi, nagi, ap, acl, bcl, ccl
    if ap != 0:
        nagi += 1
        ap -= 1
        nimble.config(text=f"+ {nagi}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')
    else:
        noAp()
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')

def agiMinu():
    global agi, nagi, ap, acl, bcl, ccl
    if nagi >= 2:
        nagi -= 1
        ap += 1
        nimble.config(text=f"+ {nagi}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')
    elif nagi == 1:
        nagi -= 1
        ap += 1
        nimble.config(text=f"")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')

agiPls = Button(frame, text="Agility +1", command=agiPlus)
agiMin = Button(frame, text="Agility -1", command=agiMinu)
agiStat = Label(frame, text= f"Agility: {agi}")
nimble = Label(frame, text=f"")


#---vitality---

def vitPlus():
    global vit, nvit, ap, acl, bcl, ccl
    if ap != 0:
        nvit += 1
        ap -= 1
        healthy.config(text=f"+ {nvit}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')
    else:
        noAp()
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')

def vitMinu():
    global vit, nvit, ap, acl, bcl, ccl
    if nvit >= 2:
        nvit -= 1
        ap += 1
        healthy.config(text=f"+ {nvit}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')
    elif nvit == 1:
        nvit -= 1
        ap += 1
        healthy.config(text=f"")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')


vitPls = Button(frame, text="Vitality +1", command=vitPlus)
vitMin = Button(frame, text="Vitality -1", command=vitMinu)
vitStat = Label(frame, text = f"Vitality: {vit}")
healthy = Label(frame, text=f"")


#---intelligence---

def itlPlus():
    global itl, nitl, ap, acl, bcl, ccl
    if ap != 0:
        nitl += 1
        ap -= 1
        smart.config(text=f"+ {nitl}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')
    else:
        noAp()
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')

def itlMinu():
    global itl, nitl, ap, acl, bcl, ccl
    if nitl >= 2:
        nitl -= 1
        ap += 1
        smart.config(text=f"+ {nitl}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')
    elif nitl == 1:
        nitl -= 1
        ap += 1
        smart.config(text=f"")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')
    

itlPls = Button(frame, text="Intelligence +1", command=itlPlus)
itlMin = Button(frame, text="Intelligence -1", command=itlMinu)
itlStat = Label(frame, text = f"Intelligence: {itl}")
smart = Label(frame, text=f"")


#---dexterity---

def dexPlus():
    global dex, ndex, ap, acl, bcl, ccl
    if ap != 0:
        ndex += 1
        ap -= 1
        dodgy.config(text=f"+ {ndex}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')
    else:
        noAp()
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')

def dexMinu():
    global dex, ndex, ap, acl, bcl, ccl
    if ndex >= 2:
        ndex -= 1
        ap += 1
        dodgy.config(text=f"+ {ndex}")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')
    elif ndex == 1:
        ndex -= 1
        ap += 1
        dodgy.config(text=f"")
        atribPoints.config(text=f"Atrribute Points Remaining {ap}")
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')
    

dexPls = Button(frame, text="Dexterity +1", command=dexPlus)
dexMin = Button(frame, text="Dexterity -1", command=dexMinu)
dexStat = Label(frame, text = f"Dexterity: {dex}")
dodgy = Label(frame, text=f"")

#--------------------------------------
def atribUp():

    frame.place(relx=0.5, y=200, anchor="center")
    frame.grid_propagate(False)
    frame.columnconfigure((6), weight = 0)
    frame.columnconfigure((1), weight = 3)
    frame.columnconfigure((0,2,3,4,5), weight = 1, minsize= 25)
    frame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight = 1)
    frame.rowconfigure(11, minsize= 40 , weight= 1)

    atribPoints.grid(row = 1, column=0, columnspan= 6)
    attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')

    streStat.grid(column = 1, row = 2, columnspan= 2, sticky = "w")
    stronk.grid(column = 4, row = 2)
    strPls.grid(column = 3, row = 2, sticky = "e")
    strMin.grid(column = 5, row = 2, sticky = "w")

    dfsStat.grid(column = 1, row = 3, columnspan= 2, sticky = "w")
    tanky.grid(column = 4, row = 3,)
    dfsPls.grid(column = 3, row = 3, sticky = "e")
    dfsMin.grid(column = 5, row = 3, sticky = "w")

    agiStat.grid(column = 1, row = 4, columnspan= 2, sticky = "w")
    nimble.grid(column = 4, row = 4,)
    agiPls.grid(column = 3, row = 4, sticky = "e")
    agiMin.grid(column = 5, row = 4, sticky = "w")

    vitStat.grid(column = 1, row = 5, columnspan= 2, sticky = "w")
    healthy.grid(column = 4, row = 5,)
    vitPls.grid(column = 3, row = 5, sticky = "e")
    vitMin.grid(column = 5, row = 5, sticky = "w")

    itlStat.grid(column = 1, row = 6, columnspan= 2, sticky = "w")
    smart.grid(column = 4, row = 6,)
    itlPls.grid(column = 3, row = 6, sticky = "e")
    itlMin.grid(column = 5, row = 6, sticky = "w")

    dexStat.grid(column = 1, row = 7, columnspan= 2, sticky = "w")
    dodgy.grid(column = 4, row = 7,)
    dexPls.grid(column = 3, row = 7, sticky = "e")
    dexMin.grid(column = 5, row = 7, sticky = "w")

# --------------------------------------

def AttribConfirm():
    global ap, acl, bcl, ccl
    attCon.grid_forget()

    def yes():
        global stre, dfs, agi, itl, dex, vit, ap
        global nstre, ndfs, nagi, nitl, ndex, nvit, nap
        dadael(acl, bcl, ccl, atribPoints, attCon, streStat, stronk, strPls, strMin, dfsStat, tanky, dfsMin, dfsPls, vitStat, vitMin, vitPls, healthy, dexStat, dexPls, dexMin, dodgy, agiStat, agiMin, agiPls, nimble, itlStat, itlPls, itlMin, smart )
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
        frame.destroy()
        d = Label(window, text="confirmed")
        window.columnconfigure((0,1,2), weight= 1, minsize="100")
        window.rowconfigure((0,1,2,3,4), weight=1)
        d.grid(column= 1, row= 1)
        window.after(1500, lambda: dadael(d))
        e = Label(window, text=f"Your Stats are now: \n Strength: {stre} \n Defense: {dfs} \n Agility: {agi} \n Vitality: {vit} \n Intelligence: {itl} \n Dexterity: {dex}")
        window.after(1500, lambda: e.grid(column=1, row=1))

    def no():
        dadael(acl, bcl, ccl)
        attCon.grid(row = 10, column = 1, rowspan= 2, sticky= 'w')

    bcl = Button(frame, text = "yes", command=yes)
    ccl = Button(frame, text= "no", command=no)

    if ap == 0:
        acl = Label(frame, text = "Confirm Stats?")
        bcl.grid(column= 2, row= 10, rowspan= 2, sticky= "w", padx= (0,25))
        ccl.grid(column= 2, row= 10, rowspan= 2)
    elif ap >= 0:
        acl = Label(frame, text= f"You have {ap} attribute points left,\n are you sure?")
        bcl.grid(column= 3, row= 10, rowspan= 2, sticky= "w", padx= (15,0))
        ccl.grid(column= 3, row= 10, rowspan= 2)

    acl.grid(row = 10, column = 1, rowspan= 2, columnspan=4, sticky= 'w')



attCon = Button(frame, text="Confirm", command= lambda: AttribConfirm())
'''


def Phase2():
    global name
    window.columnconfigure((0), weight= 1)
    window.rowconfigure((0), weight= 1)
    ccPhotob.place(x=0, y=0, relheight=1, relwidth=1)
    cc.grid(column= 0, row=0, padx= (180,0), pady= (263,0)) 
    nameEnter.grid(column= 0, row=0, padx= (408,0), pady= (263,0), ipady=2)
    charDes.grid(column= 0, row= 0, padx= (346,0), pady= (0,320))
    Char.grid(column= 0, row= 0, padx= (0,360), pady= (360, 0))
    charDes2.grid(column= 0, row= 0, padx= (346,0), pady= (0,120))
    bcBut.grid(column= 0, row= 0, padx= (0,555), pady= (360, 0))
    nxBut.grid(column= 0, row= 0, padx= (0,165), pady= (360, 0))
    nameOk.grid(column= 0, row= 0, padx= (346,0), pady= (348,0))


boy = PhotoImage(file= "boy.png")
girl = PhotoImage(file= "girl.png")
ccPhotob = Label(window, image=boy)
ccPhotog = Label(window, image=girl)
cc = Label(window, text = "Name: ", font= ("Enchanted Land", 20))
nameEnter = Entry(window,  font= ("Enchanted Land", 20))
nameOk = Button(window, text = "Confirm",font=("ancient", 12) , command = lambda: (takeName(), checkName()))
charDes = Label(window, text = "Male Character", font = ("Enchanted Land", 15), bg = "#5e4004", fg = "white")
charDes2 = Label(window, text= "Male Characters get the following \n additional attributes: \n\n +5 strength\n +5 defense\n +20 vitality", font = ("Enchanted Land", 15), bg = "#5e4004", fg = "white")

def nextBut():
    ccPhotob.place_forget()
    ccPhotog.place(x=0, y=0, relheight=1, relwidth=1)
    charDes.config(text="Female Character")
    charDes2.config(text="Female Characters get the following \n additional attributes: \n\n +10 agility \n +10 intelligence")
def backBut():
    ccPhotog.place_forget()
    ccPhotob.place(x=0, y=0, relheight=1, relwidth=1)
    charDes.config(text="Male Character")
    charDes2.config(text="Male Characters get the following \n additional attributes: \n\n +5 strength\n +5 defense\n +20 vitality")

Char = Label(window, text="Choose Character", font=("Enchanted Land", 20))
nxBut = Button(window, text=">", command=nextBut,font=("ancient", 20))
bcBut = Button(window, text="<", command=backBut,font=("ancient", 20))

def takeName():
    global name
    name = nameEnter.get()

def checkName():
    global name
    if name == "":
        def flash(blink):
            if blink <6:
                if blink % 2 == 0:
                    nameEnter.config(bg='red')
                else:
                    nameEnter.config(bg='white')
                window.after(200, lambda: flash(blink + 1))
        flash(0)
    else:
        wipe()
        attribUp()


#Button(window, text=">")
#Button(window, text="<")

Phase2()

window.mainloop()


"""
Phase 1 = Welcome screen, welcomes player
Phase 2 = character creation
    2a - name of character
    2b - attributes
    2c - story line
Phase 3 = game start
"""