class Character():
    def __init__(self):
        self.name = ""
        self.level = 0
        self.proficiency_bonus = 0

        self.str_saving = False
        self.dex_saving = False
        self.con_saving = False
        self.int_saving = False
        self.wis_saving = False
        self.cha_saving = False
        
        self.acrobatics = False
        self.animal_handling = False
        self.arcana = False
        self.atlhetics = False
        self.deception = False
        self.history = False
        self.insight = False
        self.intimidation = False
        self.investigation = False
        self.medice = False
        self.nature = False
        self.perception = False
        self.perfomance = False
        self.persuasion = False
        self.religion = False
        self.sleight_of_hand = False
        self.stealth = False
        self.survival = False

        self.strength = 10
        self.dextery = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10

        self.age = 0
        self.alignment = "neutral"
        self.order = "neutral"
        self.speed = 9
        self.darkvision = False
        
        self.life = 0
        self.armor = 10
        self.initiative = 0
        self.passive_perception = 0
        
        self.personality_traits = ""
        self.ideals = ""
        self.bonds = ""
        self.flaws = ""
        self.languages = []
        self.special_abilities = []
        self.items= []
        self.armor_item = []
        self.weapons = []

        
        self.warrior = 0
        self.bard = 0 
        self.wizard = 0 
        self.druid = 0 
        self.rogue = 0 
        self.barbarian = 0 
        self.monk = 0 
        self.paladin = 0 
        self.warlock = 0 
        self.sorcerer = 0
        

    class itens():
        def __init__(self,cost,weight):
            self.cost = cost
            self.weight = weight
    class weapon (itens):
        def __init__(self, cost, weight, damage, properties):
            super().__init__(cost, weight)
            self.damage = damage
            self. properties = properties
    class armor_shield (itens):
        #stren = strength need to use the armor, and stealthd if the armor has desadvantage in stealth
        def __init__(self, cost, weight,armorclass,stren,stealthd):
            super().__init__(cost, weight)
            self.armorclass = armorclass
            self.stren= stren
            self.stealthd= stealthd

        