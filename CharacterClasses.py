#The Job class represents the load build for the selected or predetermined job
#It will include starting equipment, skills, health stat, and attacks

class Job:
    def __init__(self, health, equip, skills, attacks):
       self.__health = health
       self.__equip = equip
       self.__skills = skills
       self.__attacks = attacks

    def get_health(self, health):
        return self.__health

    def get_equip(self):
        return self.__equip

    def get_skills(self):
        return self.__skills

    def get_attacks(self):
        return self.__attacks

class Barbarian(Job):
    def __init__(self, health, equip, skills, attacks):
        Job.__init__(self, health, equip, skills, attacks)

    def get_health(self):
        return(12)


    def get_equip(self):
        equip = ['Great Axe', 'Two Handaxes', 'Explorers Pack', 'Four Javelins']
        return(equip)

    def get_skills(self):
        return('Rage', 'Unarmored Defense')

    def get_attacks(self):
        return('Great Axe', ' - 1d12 Slashing', 'Hand Axe', ' - 1d6 Slashing', 'Javelin', ' - 1d6 Piercing')

class Bard(Job):
    def __init__(self, health, equip, skills, attacks):
        Job.__init__(self, health, equip, skills, attacks)

    def get_health(self):
        return(8)

    def get_equip(self):
        equip = ['Rapier', 'Entertainers Pack', 'Musical Instrument', 'Leather Armor']
        return(equip)

    def get_skills(self):
        return('Bardic Inspiration', 'Spell Casting')

    def get_attacks(self):
        return('Rapier', ' - 1d8 Piercing')    

class Cleric(Job):
    def __init__(self, health, equip, skills, attacks):
        Job.__init__(self, health, equip, skills, attacks)

    def get_health(self):
        return(8)

    def get_equip(self):
        equip = ['Mace', 'Scale Mail', 'Light Crossbow', 'Priest Pack', 'Sheild', 'Holy Symbol']
        return(equip)

    def get_skills(self):
        return('Divine Domain', 'Spell Casting')

    def get_attacks(self):
        return('Mace', ' - 1d6 Bludgeoning', 'Light Crossbow', ' - 1d8 Piercing')    

class Druid(Job):
    def __init__(self, health, equip, skills, attacks):
        Job.__init__(self, health, equip, skills, attacks)

    def get_health(self):
        return(8)

    def get_equip(self):
        equip = ['Wooden Shield', 'Scimitar', 'Leather Armor', 'Explorer Pack', 'Druidic Focus']
        return(equip)

    def get_skills(self):
        return('Druidic', 'Spell Casting')

    def get_attacks(self):
        return('Scimitar', ' - 1d6 Slashing')

class Fighter(Job):
    def __init__(self, health, equip, skills, attacks):
        Job.__init__(self, health, equip, skills, attacks)

    def get_health(self):
        return(10)

    def get_equip(self):
        equip = ['Chain Mail', 'Longsword', 'Shield', 'Light Crossbow', 'Dungeoneer Pack']
        return(equip)

    def get_skills(self):
        return('Fighting Style', 'Second Wind')

    def get_attacks(self):
        return('Long Sword', ' - 1d8 Slashing', 'Light Crossbow', ' - 1d8 Piercing')

class Monk(Job):
    def __init__(self, health, equip, skills, attacks):
        Job.__init__(self, health, equip, skills, attacks)

    def get_health(self):
        return(8)

    def get_equip(self):
        equip = ['Shortsword', 'Dungeoneer Pack', 'Quarterstaff']
        return(equip)

    def get_skills(self):
        return('Unarmored Defense', 'Martial Arts')

    def get_attacks(self):
        return('Quarterstaff', ' - 1d6 Bludgeoning', 'Shortsword', ' - 1d6 Slashing')

class Paladin(Job):
    def __init__(self, health, equip, skills, attacks):
        Job.__init__(self, health, equip, skills, attacks)

    def get_health(self):
        return(10)

    def get_equip(self):
        equip = ['Chain Mail', 'Longsword', 'Shield', '5 x Javelins', 'Priest Pack', 'Holy Symbol']
        return(equip)

    def get_skills(self):
        return('Divine Sense', 'Lay on Hands')

    def get_attacks(self):
        return('Longsword', ' - 1d8 Slashing', 'Javelin', ' - 1d6 Piercing')

class Ranger(Job):
    def __init__(self, health, equip, skills, attacks):
        Job.__init__(self, health, equip, skills, attacks)

    def get_health(self):
        return(10)

    def get_equip(self):
        equip = ['Leather Armor', '2 x Shortswords', 'Explorer Pack', 'Long Bow']
        return(equip)

    def get_skills(self):
        return('Favored Enemy', 'Natural Explorer')

    def get_attacks(self):
        return('Long Bow', ' - 1d8 Piercing', 'Shortsword', ' - 1d6 Slashing')

class Rogue(Job):
    def __init__(self, health, equip, skills, attacks):
        Job.__init__(self, health, equip, skills, attacks)

    def get_health(self):
        return(8)

    def get_equip(self):
        equip = ['Rapier', 'Short Bow', 'Burglar Pack', 'Leather Armor', '2 x Daggers', 'Thief Tools']
        return(equip)

    def get_skills(self):
        return('Expertise', 'Sneak Attack', 'Thieves Cant')

    def get_attacks(self):
        return('Rapier', ' - 1d8 Piercing', 'Short Bow', ' - 1d6 Piercing', 'Dagger', ' - 1d4 Piercing')

class Sorcerer(Job):
    def __init__(self, health, equip, skills, attacks):
        Job.__init__(self, health, equip, skills, attacks)

    def get_health(self):
        return(6)

    def get_equip(self):
        equip = ['Light Crossbow', 'Arcane Focus', 'Dungeoneer Pack', '2 x Daggers']
        return(equip)

    def get_skills(self):
        return('Spell Casting', 'Sorcerous Origin')

    def get_attacks(self):
        return('Light Crossbow', ' - 1d8 Piercing', 'Dagger', ' - 1d4 Piercing')

class Warlock(Job):
    def __init__(self, health, equip, skills, attacks):
        Job.__init__(self, health, equip, skills, attacks)

    def get_health(self):
        return(8)

    def get_equip(self):
        equip = ['Light Crossbow', 'Arcane Focus', 'Scholar Pack', 'Leather Armor', 'Short Sword', '2 x Daggers']
        return(equip)

    def get_skills(self):
        return('Otherworldly Patron', 'Pact Magic')

    def get_attacks(self):
        return('Light Crossbow', ' - 1d8 Piercing', 'Shortsword', ' - 1d6 Slashing', 'Dagger', ' - 1d4 Piercing')

class Wizard(Job):
    def __init__(self, health, equip, skills, attacks):
        Job.__init__(self, health, equip, skills, attacks)

    def get_health(self):
        return(6)

    def get_equip(self):
        equip = ['Quarterstaff', 'Component Pouch', 'Scholar Pack', 'Spellbook']
        return(equip)

    def get_skills(self):
        return('Spell Casting', 'Arcane Recovery')

    def get_attacks(self):
        return('Quarterstaff', ' - 1d6 Bludgeoning')





