class Character():
    last_id = 0
    def __init__(self):
        Character.last_id = Character.last_id + 1
        self.character_id = Character.last_id
        self.name = ""
        self.level = 0
        self.proficiency_bonus = 0
        self.race = ""
        self.resistence = []
        
        

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

        self.strength = 8
        self.dextery = 8
        self.constitution = 8
        self.intelligence = 8
        self.wisdom = 8
        self.charisma = 8

        self.strength_mod = 0
        self.dextery_mod = 0
        self.constitution_mod = 0
        self.intelligence_mod = 0
        self.wisdom_mod = 0
        self.charisma_mod = 0
    

        self.age = 0
        self.alignment = "neutral"
        self.order = "neutral"
        self.speed = 9
        self.darkvision = False
        self.darkvision_range = ""
        
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
        self.spells = []

        
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
    def __init__(self, cost, weight, damage, properties, range):
        super().__init__(cost, weight)
        self.damage = damage
        self. properties = properties
        self.range = range
class armor_shield (itens):
    #stren = strength needed to use the armor, and stealthd = if the armor has desadvantage in stealth
    def __init__(self, cost, weight,armorclass,stren,stealthd):
        super().__init__(cost, weight)
        self.armorclass = armorclass
        self.stren= stren
        self.stealthd= stealthd
class magic_attacks():
    def __init__(self,level, time, school, C, Range, save, damage):
        self.level = level
        self.time = time
        self.school = school
        self.C = C
        self.range = Range
        self.save = save
        self.damage = damage
        