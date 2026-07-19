import time
import random

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
nagi = 5 #chance of evading a hit
nvit = 100 #your HP
nitl = 60 #your mana
ndex = 10 #your energy

def bs(): # creates a blank space in the output
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


def character_creation():
    global name
    print("Welcome to the Character Creation!")
    name = input("Enter your character's name: ")
    time.sleep(1)
    print(f"Welcome to [insert game name] {name}")
    time.sleep(2)
    bs()

def selecAttrib():
    global stre, dfs, agi, itl, dex, vit, ap
    global nstre, ndfs, nagi, nitl, ndex, nvit, nap

    while ap != 0:
        print(f"Choose where to allocate your attribute points \nYou have {ap} ability points left:")
        print(" 1.) Strength \n 2.) Agility \n 3.) Vitality \n 4.) Defense \n 5.) Intelligence \n 6.) Dexterity")
        a = input("Enter what the attriute number here: ")
        if a == "1":
            nstre += 2
            ap -= 1
        elif a == "2":
            nagi += 1
            ap -= 1
        elif a == "3":
            nvit += 10
            ap -= 1
        elif a == "4":
            ndfs += 5
            ap -= 1
        elif a == "5":
            nitl += 5
            ap -= 1
        elif a == "6":
            ndex += 1
            ap -= 1
        else:
            print("That is not a valid attribute")
            time.sleep(2)
        bs()
    attribConfirm()

def attribConfirm():
    global stre, dfs, agi, itl, dex, vit, ap
    global nstre, ndfs, nagi, nitl, ndex, nvit, nap


    a = 1
    while a == 1:
        print(f"""Your new stats will now be: \nstrength: {nstre}\n defense: {ndfs}\n agility: {nagi}\n vitality: {nvit}\n inteligence: {nitl}\n dexterity: {ndex}""")
        b = input("confirm? y/n: ")
        if b == "y":
            dfs = ndfs
            stre = nstre
            agi = nagi
            vit = nvit
            itl = nitl
            dex = ndex
            a = 0
            print("stats confirmed")
            time.sleep(2)
        elif b == "n":
            ndfs = dfs
            nstre = stre
            nagi = agi
            nvit = vit
            nitl = itl
            ndex = dex
            ap = nap
            print("Attributes not saved, will redirect to attribute selection")
            time.sleep(2)
            bs()
            selecAttrib()
            a = 0
        else:
            print("that is not a valid response")
            time.sleep(2)
        bs()    

    
    



#character_creation()
selecAttrib()
