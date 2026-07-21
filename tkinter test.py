from tkinter import *
import time

#Player Status
name = ""
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


def dadael(*widgets):
    for widget in widgets:
        widget.destroy()

def lipat(*widgets):
    for widget in widgets:
        widget.grid_forget()


window = Tk()
window.geometry("720x480")
window.title("Text Based RPG Game")
window.resizable(False, False)

frame = Frame(window, width= "500", height= "300", bg="#5e4004")

#-------------------------------
acl = Label(window, text="")
bcl = Label(window, text="")
ccl = Label(window, text="")

def noAp():
    noAp = Label(window, text="You don't have enough atribute points", font=('Enchanted Land', 15), bg="#5e4004", bd=2, relief="solid", padx= 4)
    noAp.place(relx=0.5, y=348, anchor='center')
    frame.after(1500, lambda: dadael(noAp))

atribPoints = Label(frame, text=f"Attribute Points Remaining:  {ap}", font=("Enchanted Land", 20, "bold"), bg="#5e4004")

#---strength---

def strPlus():
    global stre, nstre, ap, acl, bcl, ccl
    if ap != 0:
        nstre += 1
        ap -= 1
        stronk.config(text=f"+ {nstre}")
        atribPoints.config(text=f"Attribute Points Remaining: {ap}")
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')
    else:
        noAp()
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')

def strMinu():
    global stre, nstre, ap, acl, bcl, ccl
    if nstre >= 2:
        nstre -= 1
        ap += 1
        stronk.config(text=f"+ {nstre}")
        atribPoints.config(text=f"Attribute Points Remaining: {ap}")
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')
    elif nstre == 1:
        nstre -= 1
        ap += 1
        stronk.config(text="")
        atribPoints.config(text=f"Attribute Points Remaining: {ap}")
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')
    
    

strPls = Button(frame, text="+", font=("MedievalSharp", 12),bg="#81601c", bd=2, command=strPlus)
strMin = Button(frame, text="-", font=("MedievalSharp", 12),bg="#81601c", bd=2, command=strMinu)
streStat = Label(frame, text = f"Strength: {stre}", font=("Ancient", 17, 'bold'), bg="#5e4004")
stronk = Label(frame, text=f"", font=("MedievalSharp", 12, 'bold'),bg="#5e4004")

#---defense---

def dfsPlus():
    global dfs, ndfs, ap, acl, bcl, ccl
    if ap != 0:
        ndfs += 1
        ap -= 1
        tanky.config(text=f"+ {ndfs}")
        atribPoints.config(text=f"Attribute Points Remaining: {ap}")
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')
    else:
        noAp()
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')

def dfsMinu():
    global dfs, ndfs, ap, acl, bcl, ccl
    if ndfs >= 2:
        ndfs -= 1
        ap += 1
        tanky.config(text=f"+ {ndfs}")
        atribPoints.config(text=f"Attribute Points Remaining: {ap}")
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')
    elif ndfs == 1:
        ndfs -= 1
        ap += 1
        tanky.config(text=f"")
        atribPoints.config(text=f"Attribute Points Remaining: {ap}")
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')
    

dfsPls = Button(frame, text="+", font=("MedievalSharp", 12),bg="#81601c", bd=2, command=dfsPlus)
dfsMin = Button(frame, text="-", font=("MedievalSharp", 12),bg="#81601c", bd=2, command=dfsMinu)
dfsStat = Label(frame, text = f"Defense: {dfs}", font=("Ancient", 17, 'bold'), bg="#5e4004")
tanky = Label(frame, text=f"", font=("MedievalSharp", 12, 'bold'),bg="#5e4004")

#---agility---

def agiPlus():
    global agi, nagi, ap, acl, bcl, ccl
    if ap != 0:
        nagi += 1
        ap -= 1
        nimble.config(text=f"+ {nagi}")
        atribPoints.config(text=f"Attribute Points Remaining: {ap}")
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')
    else:
        noAp()
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')

def agiMinu():
    global agi, nagi, ap, acl, bcl, ccl
    if nagi >= 2:
        nagi -= 1
        ap += 1
        nimble.config(text=f"+ {nagi}")
        atribPoints.config(text=f"Attribute Points Remaining: {ap}")
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')
    elif nagi == 1:
        nagi -= 1
        ap += 1
        nimble.config(text=f"")
        atribPoints.config(text=f"Attribute Points Remaining: {ap}")
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')

agiPls = Button(frame, text="+", font=("MedievalSharp", 12),bg="#81601c", bd=2, command=agiPlus)
agiMin = Button(frame, text="-", font=("MedievalSharp", 12),bg="#81601c", bd=2, command=agiMinu)
agiStat = Label(frame, text= f"Agility: {agi}", font=("Ancient", 17, 'bold'), bg="#5e4004")
nimble = Label(frame, text=f"", font=("MedievalSharp", 12, 'bold'),bg="#5e4004")


#---vitality---

def vitPlus():
    global vit, nvit, ap, acl, bcl, ccl
    if ap != 0:
        nvit += 1
        ap -= 1
        healthy.config(text=f"+ {nvit}")
        atribPoints.config(text=f"Attribute Points Remaining: {ap}")
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')
    else:
        noAp()
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')

def vitMinu():
    global vit, nvit, ap, acl, bcl, ccl
    if nvit >= 2:
        nvit -= 1
        ap += 1
        healthy.config(text=f"+ {nvit}")
        atribPoints.config(text=f"Attribute Points Remaining: {ap}")
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')
    elif nvit == 1:
        nvit -= 1
        ap += 1
        healthy.config(text=f"")
        atribPoints.config(text=f"Attribute Points Remaining: {ap}")
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')


vitPls = Button(frame, text="+", font=("MedievalSharp", 12),bg="#81601c", bd=2, command=vitPlus)
vitMin = Button(frame, text="-", font=("MedievalSharp", 12),bg="#81601c", bd=2, command=vitMinu)
vitStat = Label(frame, text = f"Vitality: {vit}", font=("Ancient", 17, 'bold'), bg="#5e4004")
healthy = Label(frame, text=f"", font=("MedievalSharp", 12, 'bold'),bg="#5e4004")


#---intelligence---

def itlPlus():
    global itl, nitl, ap, acl, bcl, ccl
    if ap != 0:
        nitl += 1
        ap -= 1
        smart.config(text=f"+ {nitl}")
        atribPoints.config(text=f"Attribute Points Remaining: {ap}")
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')
    else:
        noAp()
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')

def itlMinu():
    global itl, nitl, ap, acl, bcl, ccl
    if nitl >= 2:
        nitl -= 1
        ap += 1
        smart.config(text=f"+ {nitl}")
        atribPoints.config(text=f"Attribute Points Remaining: {ap}")
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')
    elif nitl == 1:
        nitl -= 1
        ap += 1
        smart.config(text=f"")
        atribPoints.config(text=f"Attribute Points Remaining: {ap}")
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')
    

itlPls = Button(frame, text="+", font=("MedievalSharp", 12),bg="#81601c", bd=2, command=itlPlus)
itlMin = Button(frame, text="-", font=("MedievalSharp", 12),bg="#81601c", bd=2, command=itlMinu)
itlStat = Label(frame, text = f"Intelligence: {itl}", font=("Ancient", 17, 'bold'), bg="#5e4004")
smart = Label(frame, text=f"", font=("MedievalSharp", 12, 'bold'),bg="#5e4004")


#---dexterity---

def dexPlus():
    global dex, ndex, ap, acl, bcl, ccl
    if ap != 0:
        ndex += 1
        ap -= 1
        dodgy.config(text=f"+ {ndex}")
        atribPoints.config(text=f"Attribute Points Remaining: {ap}")
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')
    else:
        noAp()
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')

def dexMinu():
    global dex, ndex, ap, acl, bcl, ccl
    if ndex >= 2:
        ndex -= 1
        ap += 1
        dodgy.config(text=f"+ {ndex}")
        atribPoints.config(text=f"Attribute Points Remaining: {ap}")
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')
    elif ndex == 1:
        ndex -= 1
        ap += 1
        dodgy.config(text=f"")
        atribPoints.config(text=f"Attribute Points Remaining: {ap}")
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')
    

dexPls = Button(frame, text="+", font=("MedievalSharp", 12),bg="#81601c", bd=2, command=dexPlus)
dexMin = Button(frame, text="-", font=("MedievalSharp", 12),bg="#81601c", bd=2, command=dexMinu)
dexStat = Label(frame, text = f"Dexterity: {dex}", font=("Ancient", 17, 'bold'), bg="#5e4004")
dodgy = Label(frame, text=f"", font=("MedievalSharp", 12, 'bold'),bg="#5e4004")

#--------------------------------------

attribPic = PhotoImage(file="attrib.png")
AP = Label(window, image=attribPic)

#--------------------------------------
def atribUp():

    AP.place(x=0, y=0, relheight=1, relwidth=1)
    AP.lower()

    frame.place(relx=0.5, y=220, anchor="center")
    frame.grid_propagate(False)
    frame.columnconfigure((6), weight = 0)
    frame.columnconfigure((1), weight = 3)
    frame.columnconfigure((0,2,3,5), weight = 1, minsize= 30)
    frame.columnconfigure((4), weight=1, minsize= 40)
    frame.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight = 1)
    frame.rowconfigure(11, minsize= 40 , weight= 1)

    atribPoints.grid(row = 1, column=0, columnspan= 6)
    attCon.place(relx=0.5, y=430, anchor='center')

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
    attCon.place_forget()

    def yes():
        global stre, dfs, agi, itl, dex, vit, ap
        global nstre, ndfs, nagi, nitl, ndex, nvit, nap
        dadael(acl, bcl, ccl, atribPoints, attCon, streStat, stronk, strPls, strMin, dfsStat, tanky, dfsMin, dfsPls, vitStat, vitMin, vitPls, healthy, dexStat, dexPls, dexMin, dodgy, agiStat, agiMin, agiPls, nimble, itlStat, itlPls, itlMin, smart)
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
        d = Label(window, text="confirmed", bg= "#d1a87a", font=("Enchanted Land", 40), bd=0)
        window.columnconfigure((0,1,2), weight= 1, minsize="100")
        window.rowconfigure((0,1,2,3,4), weight=1)
        d.grid(column= 1, row= 1)
        window.after(1500, lambda: dadael(d))
        e = Label(window, text=f"Your Stats are now:", bg= "#d1a87a", font=("Enchanted Land", 30), bd=0)
        f = Label(window, text=f"Strength: {stre} \n Defense: {dfs} \n Agility: {agi} ", bg= "#d1a87a", font=("Enchanted Land", 30), bd=0, justify="right")
        g = Label(window, text=f"Vitality: {vit} \n Intelligence: {itl} \n Dexterity: {dex} ", bg= "#d1a87a", font=("Enchanted Land", 30), bd=0, justify="right")
        h = Button(window, text="Continue", bg= "#81601c", font=("Ancient", 20), bd=2)
        window.after(1500, lambda: (e.place(relx=0.5, y=110, anchor='center'), f.place(relx=0.3, y=150), g.place(relx=0.5, y=150), h.place(relx=0.5, y=328, anchor='center')))

    def no():
        dadael(acl, bcl, ccl)
        attCon.place(relx=0.5, y=430, anchor='center')

    bcl = Button(window, text = "Yes", font= ('Ancient', 15), command=yes, bg = "#81601c", bd=2)
    ccl = Button(window, text= "No", font= ('Ancient', 15), command=no, bg = "#81601c", bd=2)

    if ap == 0:
        acl = Label(window, text = "Confirm Stats?", font=("Enchanted Land", 15), bg="#5e4004", bd=2, relief="sunken", padx= 4)
        acl.lift
        bcl.place(relx=0.46, y=430, anchor='center')
        ccl.place(relx=0.54, y=430, anchor='center')
    elif ap >= 0:
        acl = Label(window, text= f"You have {ap} attribute points left, are you sure?", font=("Ancient", 15), bg="#5e4004", bd=2, relief="groove", padx= 4)
        acl.lift
        bcl.place(relx=0.46, y=430, anchor='center')
        ccl.place(relx=0.54, y=430, anchor='center')

    acl.place(relx=0.5, y=348, anchor='center')

attCon = Button(window, text="Confirm ->", font=("Old English Text MT", 15), command= lambda: AttribConfirm(), bg = "#81601c", bd=2)

def story():
    print('wait')



atribUp()

window.mainloop()


"""
Phase 1 = Welcome screen, welcomes player
Phase 2 = character creation
    2a - name of character
    2b - attributes
    2c - story line
Phase 3 = game start
"""