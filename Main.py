#Character Sheet Creator by Trevor Noelke
#This will be the main center of the program that will initialize multiple classes to create a fully
#descriptive charactrer sheet for D&D. 
#Note: The characters will only be LVL 1 for now

import random
import CharacterClasses
import tkinter

def main():
    #base
    main_window = tkinter.Tk()
    main_window.title("New Character Sheet")
    main_window.geometry('800x1000')
    canvas1 = tkinter.Canvas(main_window, width=800, height=1000)
    canvas1.place(x=0, y=0)
    
    #grid
    line = canvas1.create_line(265, 0, 265, 1000, width=1, fill="black")
    line2 = canvas1.create_line(0, 300, 800, 300, width=1, fill="black")
    line3 = canvas1.create_line(265, 70, 800, 70, width=1, fill="black")
    line4 = canvas1.create_line(530, 300, 530, 1000, width=1, fill="black")

    #Labels 
    AttackL = tkinter.Label(main_window,text='Attacks / Spells', font='Helvetica 10 bold')
    AttackL.place(x=0, y=305)
    InventoryL = tkinter.Label(main_window,text='Inventory', font='Helvetica 10 bold')
    InventoryL.place(x=266, y=305)
    FeatsL = tkinter.Label(main_window,text='Feats / Skills', font='Helvetica 10 bold')
    FeatsL.place(x=531, y=305)

    #First things first, we are going to need some stats, right?? 
    #we'll use random number generators for that! (and set them to gui variables)
    strStat = genStat()
    strVal = tkinter.StringVar()
    strVal.set(strStat)
    dexStat = genStat()
    dexVal = tkinter.StringVar()
    dexVal.set(dexStat)
    innit = int(round(((dexStat - 10) / 2),0))
    conStat = genStat()
    conVal = tkinter.StringVar()
    conVal.set(conStat)
    intStat = genStat()
    intVal = tkinter.StringVar()
    intVal.set(intStat)
    wisStat = genStat()
    wisVal = tkinter.StringVar()
    wisVal.set(wisStat)
    chaStat = genStat()
    chaVal = tkinter.StringVar()
    chaVal.set(chaStat) 
    statList = [strStat, dexStat, conStat, intStat, wisStat, chaStat]
    
    #then we will need to use those stats to determine potential class and race
    #alignment could be randomized
    classPick = determineClass(statList)

    #The class would then determine starting equip, skills, and inventory
    myClass = setClass(classPick)

    innitative = tkinter.StringVar()
    innitative.set(innit)
    classVal = tkinter.StringVar()
    classVal.set(classPick)

    #Info Bracket
    name = tkinter.Label(main_window,text='Character Name:', font='Helvetica 10 bold')
    name.place(x=0, y=0)
    race = tkinter.Label(main_window,text='Race: Human')
    race.place(x=266, y=0)
    level = tkinter.Label(main_window,text='Level: 1')
    level.place(x=266, y=20)
    innit = tkinter.Label(main_window,text='Innitiative:',)
    innit.place(x=266, y=40)
    innitVal = tkinter.Label(main_window, textvariable=innitative)
    innitVal.place(x=326, y=41)
    classL = tkinter.Label(main_window,text='Class: ')
    classL.place(x=532, y=0)
    classL2 = tkinter.Label(main_window,textvariable=classVal)
    classL2.place(x=565, y=0)
    alignL = tkinter.Label(main_window,text='Alignment: Nuetral Good')
    alignL.place(x=532, y=20)
    profL = tkinter.Label(main_window,text='Proficiency Bonus: +2')
    profL.place(x=532, y=40)

    #Stat Bracket
    statL = tkinter.Label(main_window,text='Character Stats', font='Helvetica 10 bold')
    statL.place(x=0, y=60)
    strLabel = tkinter.Label(main_window,textvariable=strVal)
    strLabel.place(x=40, y=80)
    strL = tkinter.Label(main_window,text='STR:', font='Helvetica 10 bold')
    strL.place(x=0, y=80)
    dexLabel = tkinter.Label(main_window,textvariable=dexVal)
    dexLabel.place(x=40, y=100)
    dexL = tkinter.Label(main_window,text='DEX:', font='Helvetica 10 bold')
    dexL.place(x=0, y=100)
    conLabel = tkinter.Label(main_window,textvariable=conVal)
    conLabel.place(x=40, y=120)
    conL = tkinter.Label(main_window,text='CON:', font='Helvetica 10 bold')
    conL.place(x=0, y=120)
    intLabel = tkinter.Label(main_window,textvariable=intVal)
    intLabel.place(x=40, y=140)
    intL = tkinter.Label(main_window,text='INT:', font='Helvetica 10 bold')
    intL.place(x=0, y=140)
    wisLabel = tkinter.Label(main_window,textvariable=wisVal)
    wisLabel.place(x=40, y=160)
    wisL = tkinter.Label(main_window,text='WIS:', font='Helvetica 10 bold')
    wisL.place(x=0, y=160)
    chaLabel = tkinter.Label(main_window,textvariable=chaVal)
    chaLabel.place(x=40, y=180)
    chaL = tkinter.Label(main_window,text='CHA:', font='Helvetica 10 bold')
    chaL.place(x=0, y=180)

    #let's throw all the inventory for the class on the sheet!    
    inv = myClass.get_equip()
    invPlace = 330
    for i in range(len(inv)):
        item = inv[i]
        invtemp = tkinter.Label(main_window,text=item)
        invtemp.place(x=266, y=invPlace)
        invPlace += 20

    #Add in the skills and feats we have at level 1
    sk = myClass.get_skills()
    skPlace = 330
    for s in range(len(sk)):
        skill = sk[s]
        sktemp = tkinter.Label(main_window,text=skill)
        sktemp.place(x=531, y=skPlace)
        skPlace += 20

    #And add in some attacks
    atk = myClass.get_attacks()
    atkPlace = 330
    for a in range(len(atk)):
        attack = atk[a]
        atktemp = tkinter.Label(main_window,text=attack)
        atktemp.place(x=0, y=atkPlace)
        atkPlace += 20


    tkinter.mainloop()


def genStat():
    result = [  # Generate n_dice numbers between [1, dice_rank]
        random.randint(1, 6)
        for n
        in range(4)
    ]
    result.remove(min(result))
    return sum(result)

#this section is gross, I know, but its the best I could do for now
def determineClass(list1):
    tempList = list1.copy()
    tempList.sort(reverse=True)
    stat1 = tempList[0]
    stat2 = tempList[1]

    randClass = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

    index1 = list1.index(stat1)
    index2 = list1.index(stat2)

    if index1 == 0:
        if index2 == 1:
            classPick = 'Fighter'
        elif index2 == 2:
            classPick = 'Barbarian'
        elif index2 == 5:
            classPick = 'Paladin'
        else:
            coinflip = random.randint(1,2)
            if coinflip == 1:
                classPick = 'Fighter'
            elif coinflip == 2:
                classPick = 'Barbarian'
    elif index1 == 1:
        if index2 == 0:
            classPick = 'Fighter'
        elif index2 == 4:
            coinflip = random.randint(1,2)
            if coinflip == 1:
                classPick = 'Monk'
            elif coinflip == 2:
                classPick = 'Ranger'
        else:
            classPick = 'Rogue'
    elif index1 == 2:
        if index2 == 0:
            classPick = 'Barbarian'
        elif index2 == 5:
            classPick = 'Paladin'
        else:
            pick = random.randint(1,12)
            classPick = randClass[pick]
    elif index1 == 3:
        classPick = 'Wizard'
    elif index1 == 4:
        if index2 == 1:
            coinflip = random.randint(1,2)
            if coinflip == 1:
                classPick = 'Monk'
            elif coinflip == 2:
                classPick = 'Ranger'
        elif index2 == 3:
            classPick = 'Druid'
        elif index2 == 5:
            classPick = 'Cleric'
        else:
            coinflip = random.randint(1,2)
            if coinflip == 1:
                classPick = 'Cleric'
            elif coinflip == 2:
                classPick = 'Druid'
    elif index1 == 5:
        if index2 == 1:
            classPick = 'Bard'
        elif index2 == 0:
            classPick = 'Paladin'
        elif index2 == 2:
            classPick = 'Sorcerer'
        elif index2 == 4:
            classPick = 'Warlock'
        else:
            coinflip = random.randint(0,3)
            section5 = ['Bard', 'Paladin', 'Sorcerer','Warlock']
            classPick = section5[coinflip]
    else:
        pick = random.randint(1,12)
        classPick = randClass[pick]
          
    return(classPick) 

def setClass(classPick):
    pick = classPick

    if pick == 'Barbarian':
        return CharacterClasses.Barbarian(12, 'stuff', 'more stuff', 'swinging')
    elif pick == 'Bard':
        return CharacterClasses.Bard(8, 'stuff', 'more stuff', 'swinging')
    elif pick == 'Cleric':
        return CharacterClasses.Cleric(8, 'stuff', 'more stuff', 'swinging')
    elif pick == 'Druid':
        return CharacterClasses.Druid(8, 'stuff', 'more stuff', 'swinging')
    elif pick == 'Fighter':
        return CharacterClasses.Fighter(10, 'stuff', 'more stuff', 'swinging')
    elif pick == 'Monk':
        return CharacterClasses.Monk(8, 'stuff', 'more stuff', 'swinging')
    elif pick == 'Paladin':
        return CharacterClasses.Paladin(10, 'stuff', 'more stuff', 'swinging')
    elif pick == 'Ranger':
        return CharacterClasses.Ranger(10, 'stuff', 'more stuff', 'swinging')
    elif pick == 'Rogue':
        return CharacterClasses.Rogue(8, 'stuff', 'more stuff', 'swinging')
    elif pick == 'Sorcerer':
        return CharacterClasses.Sorcerer(6, 'stuff', 'more stuff', 'swinging')
    elif pick == 'Warlock':
        return CharacterClasses.Warlock(8, 'stuff', 'more stuff', 'swinging')
    elif pick == 'Wizard':
        return CharacterClasses.Wizard(6, 'stuff', 'more stuff', 'swinging')



main()