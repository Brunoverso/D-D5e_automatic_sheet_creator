from tkinter import *
from tkinter import ttk
from Character import *
from tktooltip import ToolTip

    


class Screen():
    def __init__(self,name,size,position, posi):
        self.name = name
        self.root = Tk()
        self.size = size
        self.position = position
        self.posi = posi
        self.screen_config()
        if self.posi == 1:
            self.main_screen_frame()
        self.root.mainloop()
        #Essa variavel é necessária para fazer contagem entre funções no futuro.
        self.counter = 0
        

    def screen_config(self):
        self.root.title(self.name)
        self.root.configure(background = 'white')
        self.root.geometry(self.size+self.position)
        self.root.resizable(True,True)
        self.root.minsize(width= 400, height= 300)

    def main_screen_frame(self):
        #Criando o Frame 1
        self.frame1 = Frame(self.root)
        self.frame1.place(relx = 0.02, rely = 0.02, relwidth= 0.96, relheight= 0.46)

        #CRIANDO OS LABELS
        #criando o label para o "code"
        self.label_code = Label(self.frame1, text ="code")
        self.label_code.place(relx=0.02,rely=0.05)
        #criando a entry para o "code"
        self.entry_code = Entry(self.frame1)
        self.entry_code.place(relx=0.02,rely=0.10, relwidth= 0.07)
        #criando o label para "name"
        self.label_name = Label(self.frame1, text ="name")
        self.label_name.place(relx=0.02, rely=0.29)
        #criando a entry para "name"
        self.entry_name = Entry(self.frame1)
        self.entry_name.place(relx=0.02,rely=0.34, relwidth= 0.5)
        #criando o label para "level"
        self.label_level = Label(self.frame1, text ="level")
        self.label_level.place(relx=0.02, rely=0.17)
        #criando a entry para "level"
        self.entry_level = Entry(self.frame1)
        self.entry_level.place(relx=0.02,rely=0.22, relwidth=0.07)
        #criando o label para "class"
        self.label_class = Label(self.frame1, text ='class or classes, use "," to separete each one')
        self.label_class.place(relx=0.02, rely=0.41)
        #criando a entry para "class"
        self.entry_class = Entry(self.frame1)
        self.entry_class.place(relx=0.02,rely=0.46, relwidth= 0.5)

        
        #CRIANDO OS BOTÕES
        #Criando o botão "new"
        self.bt_new = Button(self.frame1, text="new",command=self.create_new_character)
        self.bt_new.place(relx = 0.6, rely= 0.18, relwidth=0.07)
        #Criando o botão "delete"
        self.bt_delete = Button(self.frame1, text="delete")
        self.bt_delete.place(relx = 0.68, rely= 0.18, relwidth=0.07)
        #Criando o botão "modify"
        self.bt_modify = Button(self.frame1, text="modify")
        self.bt_modify.place(relx = 0.76, rely= 0.18, relwidth= 0.07)
        #criando o botão "search"
        self.bt_search = Button(self.frame1, text="search")
        self.bt_search.place(relx = 0.3, rely= 0.18, relwidth= 0.07)
        #criando o botão "clear"
        self.bt_clear = Button(self.frame1, text="clear", command=self.clear_fields)
        self.bt_clear.place(relx = 0.38, rely= 0.18, relwidth= 0.07)
        
        
        
        
        #CRIANDO O FRAME 2
        self.frame2 = Frame(self.root)
        self.frame2.place(relx = 0.02, rely = 0.52, relwidth= 0.96, relheight= 0.46)
        #criando as colunas da aba de pesquisa
        self.listcha = ttk.Treeview(self.frame2, height= 3, columns=("code","name","level","Class or Classes"))
        self.listcha.heading("#0", text="")
        self.listcha.heading("#1", text="code")
        self.listcha.heading("#2", text="name")
        self.listcha.heading("#3", text="level")
        self.listcha.heading("#4", text="class or classes")

        self.listcha.column("#0", width=1, stretch= NO)
        self.listcha.column("#1", width=20)
        self.listcha.column("#2", width=160)
        self.listcha.column("#3", width=20)
        self.listcha.column("#4", width=300)
        
        self.listcha.place(relx= 0.00, rely=0.00,relheight=1, relwidth=1)

    #criando a barra de rolagem
        scroll_bar = Scrollbar(self.frame2)
        scroll_bar.pack(side = 'right', fill = 'y')

        self.listcha.config(yscrollcommand = scroll_bar.set)
        scroll_bar.config(command = self.listcha.yview)
    
    
    
    #Criando as funções dos botões 
    def clear_fields(self):
        self.entry_code.delete(0, END)
        self.entry_name.delete(0, END)
        self.entry_level.delete(0, END)
        self.entry_class.delete(0, END)
    
    def create_new_character(self):
        self.new_character_window = Toplevel(self.root)
        self.new_character_window.title("New Character")
        self.new_character_window.geometry("300x300")
        self.new_character_window.resizable(False,False)
        #Label e Entry para o nome e o level do personagem
        self.label_name2 = Label(self.new_character_window, text="Name:")
        self.label_name2.place(relx=0.1, rely=0.1)
        self.entry_name2 = Entry(self.new_character_window)
        self.entry_name2.place(relx=0.3, rely=0.1, relwidth=0.6)
        self.label_level2 = Label(self.new_character_window, text="Level:")
        self.label_level2.place(relx=0.1, rely=0.4)
        self.entry_level2 = Entry(self.new_character_window)
        self.entry_level2.place(relx=0.3, rely=0.4, relwidth=0.6)

        #criando o botão done
        self.bt_done = Button(self.new_character_window, text="Done", command=self.save_initial_data)
        self.bt_done.place(relx=0.7, rely=0.8)

    def save_initial_data(self):
        new_character = Character()
        new_character.name = self.entry_name2.get()
        new_character.level = int(self.entry_level2.get())
        #Quando os dados são salvos a janela é apagada
        self.new_character_window.destroy()
        #E é aberto uma nova
        self.customization_screen()
        if new_character.level <= 4:
            new_character.proficiency_bonus = 2
        if new_character.level <= 8 and new_character.level > 4:
            new_character.proficiency_bonus = 3
        if new_character.level <= 12 and new_character.level > 8:
            new_character.proficiency_bonus = 4
        if new_character.level <= 16 and new_character.level > 12:
            new_character.proficiency_bonus = 5
        if new_character.level <= 20 and new_character.level > 16:
            new_character.proficiency_bonus = 6

    
        self.new_character = new_character



    def customization_screen(self):
        self.customization_window = Toplevel(self.root)
        self.customization_window.title("Customization")
        self.customization_window.geometry("300x300")
        self.customization_window.resizable(False, False)
        # Variável para armazenar os pontos restantes
        self.points_remaining = 27
        self.points_label = Label(self.customization_window, text = f"Points remaning: {self.points_remaining}")
        self.points_label.pack()
        

        # Criação dos labels para os atributos
        self.label_strength = Label(self.customization_window, text="Strength:")
        self.label_strength.place(relx=0.1, rely=0.1)
        self.label_dexterity = Label(self.customization_window, text="Dexterity:")
        self.label_dexterity.place(relx=0.1, rely=0.2)
        self.label_constitution = Label(self.customization_window, text="Constitution:")
        self.label_constitution.place(relx=0.1, rely=0.3)
        self.label_intelligence = Label(self.customization_window, text="Intelligence:")
        self.label_intelligence.place(relx=0.1, rely=0.4)
        self.label_wisdom = Label(self.customization_window, text="Wisdom:")
        self.label_wisdom.place(relx=0.1, rely=0.5)
        self.label_charisma = Label(self.customization_window, text="Charisma:")
        self.label_charisma.place(relx=0.1, rely=0.6)

        #Criação das entrys para os atributos
        self.strength_entry = Entry(self.customization_window, validate="focusout")
        self.strength_entry.place(relx=0.4, rely=0.1)
        self.dexterity_entry = Entry(self.customization_window, validate="focusout")
        self.dexterity_entry.place(relx=0.4, rely=0.2)
        self.constitution_entry = Entry(self.customization_window, validate="focusout")
        self.constitution_entry.place(relx=0.4, rely=0.3)
        self.intelligence_entry = Entry(self.customization_window, validate="focusout")
        self.intelligence_entry.place(relx=0.4, rely=0.4)
        self.wisdom_entry = Entry(self.customization_window, validate="focusout")
        self.wisdom_entry.place(relx=0.4, rely=0.5)
        self.charisma_entry = Entry(self.customization_window, validate="focusout")
        self.charisma_entry.place(relx=0.4, rely=0.6)
        #O parâmetro "validatecommand" espera receber uma tupla de dois elementos, onde o primeiro é uma função e o segundo é uma string. A função é chamada quando o evento de validação ocorre e a string é passada como argumento para a função.
        #A primeira parte da tupla é a função "self.strength_entry.register(self.validate)" que é uma função que foi registrada para ser chamada quando a validação ocorre. Ela é passada para o método "register" do objeto Entry, e essa função retorna outra função que é capaz de ser chamada com o parâmetro "%P"
        # A segunda parte da tupla é a string "%P" que é passada como argumento para a função "validate" quando é chamada. Essa string representa o novo valor digitado pelo usuário e é passada como argumento para a função "validate"

        self.strength_entry.config(validatecommand=(self.strength_entry.register(self.validate_number),'%P','strength')) 
        self.strength_entry.insert(END, 8)
        self.dexterity_entry.config(validatecommand=(self.dexterity_entry.register(self.validate_number),'%P','dexterity')) 
        self.dexterity_entry.insert(END, 8)
        self.constitution_entry.config(validatecommand=(self.constitution_entry.register(self.validate_number),'%P','constitution')) 
        self.constitution_entry.insert(END, 8)
        self.intelligence_entry.config(validatecommand=(self.intelligence_entry.register(self.validate_number),'%P','intelligence')) 
        self.intelligence_entry.insert(END, 8)
        self.wisdom_entry.config(validatecommand=(self.wisdom_entry.register(self.validate_number),'%P','wisdom')) 
        self.wisdom_entry.insert(END, 8)
        self.charisma_entry.config(validatecommand=(self.charisma_entry.register(self.validate_number),'%P','charisma')) 
        self.charisma_entry.insert(END, 8)

        #criando o botão done2
        self.bt_done2 = Button(self.customization_window, text="Done", command=self.customization_screen2)
        self.bt_done2.place(relx=0.7, rely=0.8)
        

    
   

    def customization_screen2(self):
        self.customization_window.destroy()
        self.customization_window2 = Toplevel(self.root)
        self.customization_window2.title("Race Customization")
        self.customization_window2.geometry("800x800")
        self.customization_window2.resizable(False, False)
        text = Label(self.customization_window2, text="Choose one of the races")
        text.pack()
        
        #Criando as opções de raça
        self.dragonborn_button= Button (self.customization_window2, text="Dragonborn", command=self.dragonborn_choose)
        self.dragonborn_button.pack()
        
        self.dwarf_button= Button (self.customization_window2, text="Dwarf", command=self.dwarf_choose)
        self.dwarf_button.pack()

        self.elf_button = Button (self.customization_window2, text="Elf", command=self.elf_choose)
        self.elf_button.pack()

        self.gnome_button = Button(self.customization_window2, text="Gnome", command=self.gnome_choose)
        self.gnome_button.pack()

        self.half_elf_button = Button(self.customization_window2, text="Half-Elf", command=self.half_elf_choose)
        self.half_elf_button.pack()

        self.half_orc_button = Button(self.customization_window2, text="Half-Orc", command=self.half_orc_choose)
        self.half_orc_button.pack()

        
        
        
        
        
    
        #adicionando os tooltip
        ToolTip(self.dragonborn_button, msg= "Str +2; Cha +1; Draconic Ancestry; Breath Weapon; Damage resistence; Languages = Commom and Draconic")
        ToolTip(self.dwarf_button, msg= "Str +2; Con +2; Dark Vision; Dwarven Resilience; Dwarven Combat Training; Toll Proficiency; Stone Cunning; Languages = Commom and Dwarvish")
        ToolTip(self.elf_button, msg= "Dex +2; Dark Vision; Keen Senses; Fey Ancestry; Trance; Languages = Common and Elvish")
        ToolTip(self.gnome_button, msg= "Int +2; Dark Vision; Gnome Cunning; Languages = Common and Gnomish")
        ToolTip(self.half_elf_button, msg= "Cha +2; Choose any other two unique +1; Dark Vision; Fey Ancestry; SKill Versatility; Languages = Common, Elvish and one extra language of your choise")
        ToolTip(self.half_orc_button, msg= "Str +2; Con +1; Dark Vision; Menacing; Relentless Endurance; Savage Attacks; Languages = Common, Orc")





    def dragonborn_choose(self):
        self.new_character.race = "Dragonborn"
        self.new_character.strength += 2
        self.new_character.charisma += 1
        self.new_character.languages += ["Commom","Draconic"]
        self.customization_window2.destroy()
        self.dragonborn_window = Toplevel (self.root)
        text_dragonborn = Label(self.dragonborn_window, text="Choose one of the colors")
        text_dragonborn.pack()
        
        #Calculando o dano do ataque da baforada
        if self.new_character.level <=5:
            damage = "2d6"
        elif self.new_character.level <=10:
            damage = "3d6"
        elif self.new_character.level <=15:
            damage = "4d6"
        else:
            damage = "5d6"

        
        #Seleção do elemento:
        self.black_button= Button(self.dragonborn_window, text="Black", command=lambda: self.dragonborn_color_choose("Black", damage))
        self.black_button.pack()
        ToolTip(self.black_button, msg= "Damage type = Acid; 5 by 30 ft. line (Dex. save); gain resistence to acid")

        self.blue_button= Button(self.dragonborn_window, text="Blue", command=lambda: self.dragonborn_color_choose("Blue", damage))
        self.blue_button.pack()
        ToolTip(self.blue_button, msg= "Damage type = Lightning; 5 by 30 ft. line (Dex. save); gain resistence to lightning")

        self.brass_button= Button(self.dragonborn_window, text="Brass", command=lambda: self.dragonborn_color_choose("Brass", damage))
        self.brass_button.pack()
        ToolTip(self.brass_button, msg= "Damage type = Fire; 5 by 30 ft. line (Dex. save); gain resistence to fire")
        
        self.bronze_button= Button(self.dragonborn_window, text="Bronze", command=lambda: self.dragonborn_color_choose("Bronze", damage))
        self.bronze_button.pack()
        ToolTip(self.bronze_button, msg= "Damage type = Lightning; 5 by 30 ft. line (Dex. save); resistence to Lightning")

        self.copper_button= Button(self.dragonborn_window, text="Copper", command=lambda: self.dragonborn_color_choose("Copper", damage))
        self.copper_button.pack()
        ToolTip(self.copper_button, msg= "Damage type = Acid; 5 by 30 ft. line (Dex. save); gain resistence to acid")

        self.gold_button= Button(self.dragonborn_window, text="Gold", command=lambda: self.dragonborn_color_choose("Gold", damage))
        self.gold_button.pack()
        ToolTip(self.gold_button, msg= "Damage type = 15 ft. cone (Dex. save); gain resistence to fire")

        self.green_button= Button(self.dragonborn_window, text="Green", command=lambda: self.dragonborn_color_choose("Green", damage))
        self.green_button.pack()
        ToolTip(self.green_button, msg= "Damage type = 15 ft. cone (Con. save); gain resistence to poison")

        self.red_button= Button(self.dragonborn_window, text="Red", command=lambda: self.dragonborn_color_choose("Red", damage))
        self.red_button.pack()
        ToolTip(self.red_button, msg= "Damage type = 15 ft. cone (Dex. save); gain resistence to fire")

        self.silver_button= Button(self.dragonborn_window, text="Silver", command=lambda: self.dragonborn_color_choose("Silver", damage))
        self.silver_button.pack()
        ToolTip(self.silver_button, msg= "Damage type = 15 ft. cone (Con. save); gain resistence to cold")

        self.white_button= Button(self.dragonborn_window, text="White", command=lambda: self.dragonborn_color_choose("White", damage))
        self.white_button.pack()
        ToolTip(self.white_button, msg= "Damage type = 15 ft. cone (Con. save); gain resistence to cold")

        
    def dragonborn_color_choose (self,color,damage):
        if color == "Black":
            breath_weapon = magic_attacks(0,"action","none","none","5 by 30 ft. line", 8 + self.new_character.constitution_mod + self.new_character.proficiency_bonus, damage)
            self.new_character.resistence.append("Acid")
            self.new_character.spells.append(breath_weapon)
            self.dragonborn_window.destroy()
            self.customization_screen3()
        elif color == "Blue":
            breath_weapon = magic_attacks(0,"action","none","none","5 by 30 ft. line", 8 + self.new_character.constitution_mod + self.new_character.proficiency_bonus, damage)
            self.new_character.resistence.append("Lightning")
            self.new_character.spells.append(breath_weapon)
            self.dragonborn_window.destroy()
            self.customization_screen3()
        elif color == "Brass":
            breath_weapon = magic_attacks(0,"action","none","none","5 by 30 ft. line", 8 + self.new_character.constitution_mod + self.new_character.proficiency_bonus, damage)
            self.new_character.resistence.append("Fire")
            self.new_character.spells.append(breath_weapon)
            self.dragonborn_window.destroy()
            self.customization_screen3()
        elif color == "Bronze":
            breath_weapon = magic_attacks(0,"action","none","none","5 by 30 ft. line", 8 + self.new_character.constitution_mod + self.new_character.proficiency_bonus, damage)
            self.new_character.resistence.append("Lightning")
            self.new_character.spells.append(breath_weapon)
            self.dragonborn_window.destroy()
            self.customization_screen3()
        elif color == "Copper":
            breath_weapon = magic_attacks(0,"action","none","none","5 by 30 ft. line", 8 + self.new_character.constitution_mod + self.new_character.proficiency_bonus, damage)
            self.new_character.resistence.append("Acid")
            self.new_character.spells.append(breath_weapon)
            self.dragonborn_window.destroy()
            self.customization_screen3()
        elif color == "Gold":
            breath_weapon = magic_attacks(0,"action","none","none","15 ft. cone", 8 + self.new_character.constitution_mod + self.new_character.proficiency_bonus, damage)
            self.new_character.resistence.append("Fire")
            self.new_character.spells.append(breath_weapon)
            self.dragonborn_window.destroy()
            self.customization_screen3()
        elif color == "Green":
            breath_weapon = magic_attacks(0,"action","none","none","15 ft. cone", 8 + self.new_character.constitution_mod + self.new_character.proficiency_bonus, damage)
            self.new_character.resistence.append("Poison")
            self.new_character.spells.append(breath_weapon)
            self.dragonborn_window.destroy()
            self.customization_screen3()
        elif color == "Red":
            breath_weapon = magic_attacks(0,"action","none","none","15 ft. cone", 8 + self.new_character.constitution_mod + self.new_character.proficiency_bonus, damage)
            self.new_character.resistence.append("Fire")
            self.new_character.spells.append(breath_weapon)
            self.dragonborn_window.destroy()
            self.customization_screen3()
        elif color == "Silver":
            breath_weapon = magic_attacks(0,"action","none","none","15 ft. cone", 8 + self.new_character.constitution_mod + self.new_character.proficiency_bonus, damage)
            self.new_character.resistence.append("Cold")
            self.new_character.spells.append(breath_weapon)
            self.dragonborn_window.destroy()
            self.customization_screen3()
        elif color == "White":
            breath_weapon = magic_attacks(0,"action","none","none","15 ft. cone", 8 + self.new_character.constitution_mod + self.new_character.proficiency_bonus, damage)
            self.new_character.resistence.append("Cold")
            self.new_character.spells.append(breath_weapon)
            self.dragonborn_window.destroy()
            self.customization_screen3()

    
    
    def dwarf_choose(self):
        self.new_character.race = "Dwarf"
        self.new_character.speed = 25
        self.new_character.strength += 2
        self.new_character.languages += ["Commom","Dwarvish"]
        self.new_character.darkvision = True
        self.new_character.darkvision_range = "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light."
        self.new_character.resistence.append("Poison")
        self.new_character.special_abilities.append("You have advantage on saving throws against poison")
        self.new_character.special_abilities.append("Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.")
        self.customization_window2.destroy()
        self.dwarf_window = Toplevel (self.root)
        text_dwarf = Label(self.dwarf_window, text="Choose one of the subraces")
        text_dwarf.pack()


        #seleção da subraça
        self.hill_button= Button(self.dwarf_window, text="Hill", command=self.dwarf_hill_choose)
        self.hill_button.pack()
        ToolTip(self.hill_button, msg= "Dwarven Toughness. Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.")

        self.mountain_button= Button(self.dwarf_window, text="Mountain", command=self.dwarf_mountain_choose)
        self.mountain_button.pack()
        ToolTip(self.mountain_button, msg= "Dwarven Armor Training. You have proficiency with light and medium armor.")

    def dwarf_hill_choose(self):
        self.new_character.life += self.new_character.level
        self.dwarf_window.destroy()
        self.customization_screen3()
    def dwarf_mountain_choose(self):
        self.new_character.special_abilities.append("You have proficiency with light and medium armor")
        self.dwarf_window.destroy()
        self.customization_screen3()

    
    def elf_choose(self):
        self.new_character.race = "Elf"
        self.new_character.dextery += 2
        self.new_character.languages += ["Commom","Elvish"]
        self.new_character.darkvision = True
        self.new_character.darkvision_range = "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light."
        self.new_character.resistence.append("Charmed")
        self.new_character.perception = self.new_character.proficiency_bonus
        self.new_character.special_abilities.append("You have advantage on saving throws against been charmed")
        self.new_character.special_abilities.append("magic can't put you to sleep, Elves don't need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day, After resting in this way, you gain the same benefit that a human does from 8 hours of sleep")
        self.customization_window2.destroy()
        self.elf_window = Toplevel (self.root)
        text_elf = Label(self.elf_window, text="Choose one of the subraces")
        text_elf.pack()

         #seleção da subraça
        self.drow_button= Button(self.elf_window, text="Drow", command=self.elf_drow_choose)
        self.drow_button.pack()
        ToolTip(self.drow_button, msg= "Sunlight Sensitivity: You have disadvantage on attack rolls and on Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight; Drow Magic. You know the dancing lights cantrip. When you reach 3rd level, you can cast the faerie fire spell once with this trait; you regain the ability to cast it when you finish a long rest. When you reach 5th level, you can also cast the darkness spell once per day with this trait; you regain the ability to cast it when you finish a long rest. Charisma is your spellcasting ability for these spells;  Drow Weapon Training: You have proficiency with rapiers, shortswords, and hand crossbows.")

        self.high_button= Button(self.elf_window, text="High", command=self.elf_high_choose)
        self.high_button.pack()
        ToolTip(self.high_button, msg= "Elf Weapon Training. You have proficiency with the longsword, shortsword, shortbow, and longbow; Cantrip. You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it.")

        self.wood_button= Button(self.elf_window, text="Wood", command=self.elf_wood_choose)
        self.wood_button.pack()
        ToolTip(self.wood_button, msg= "Elf Weapon Training. You have proficiency with the longsword, shortsword, shortbow, and longbow; Fleet of Foot: Your base walking speed increases to 35 feet; Mask of the Wild. You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.")

    def elf_drow_choose (self):
        self.new_character.charisma += 1
        self.new_character.special_abilities.append("Sunlight Sensitivity. You have disadvantage on attack rolls and on Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight.")
        self.new_character.special_abilities.append("Drow Magic. You know the dancing lights cantrip. When you reach 3rd level, you can cast the faerie fire spell once with this trait; you regain the ability to cast it when you finish a long rest. When you reach 5th level, you can also cast the darkness spell once per day with this trait; you regain the ability to cast it when you finish a long rest. Charisma is your spellcasting ability for these spells.")
        self.elf_window.destroy()
        self.customization_screen3()
        self.new_character.special_abilities.append("Drow Weapon Training. You have proficiency with rapiers, shortswords, and hand crossbows.")
    def elf_high_choose (self):
        self.new_character.intelligence += 1
        self.new_character.special_abilities.append("Elf Weapon Training. You have proficiency with the longsword, shortsword, shortbow, and longbow.")
        #self.choose_cantrip():
        #self.choose_language():
        self.elf_window.destroy()
        self.customization_screen3()
    def elf_wood_choose (self):
        self.new_character.wisdom += 1
        self.new_character.special_abilities.append("Elf Weapon Training. You have proficiency with the longsword, shortsword, shortbow, and longbow.")
        self.new_character.speed = 35
        self.new_character.special_abilities.append("Mask of the Wild. You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.")
        self.elf_window.destroy()
        self.customization_screen3()


    def gnome_choose(self):
        self.new_character.race = "Gnome"
        self.new_character.speed = 25
        self.new_character.intelligence += 2
        self.new_character.languages += ["Commom","Gnomish"]
        self.new_character.darkvision = True
        self.new_character.darkvision_range = "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light."
        self.new_character.special_abilities.append("Gnome Cunning. You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic.")
        self.customization_window2.destroy()
        self.gnome_window = Toplevel (self.root)
        text_gnome = Label(self.gnome_window, text="Choose one of the subraces")
        text_gnome.pack()

        #seleção da subraça
        self.forest_button= Button(self.gnome_window, text="Forest", command=self.gnome_forest_choose)
        self.forest_button.pack()
        ToolTip(self.forest_button, msg= "Natural Illusionist: You know the minor illusion cantrip. Intelligence is your spellcasting ability for it; Speak with Small Beasts: Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts. Forest gnomes love animals and often keep squirrels, badgers, rabbits, moles, woodpeckers, and other creatures as beloved pets. ")

        self.rock_button= Button(self.gnome_window, text="Rock", command=self.gnome_rock_choose)
        self.rock_button.pack()
        ToolTip(self.rock_button, msg= "Artificer's Lore: Whenever you make an Intelligence (History) check related to magic items, alchemical objects, or technological devices, you can add twice your proficiency bonus, instead of any proficiency bonus you normally apply; Tinker: You have proficiency with artisan's tools (tinker's tools). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time; Clockwork Toy: This toy is a clockwork animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier. When placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents; Fire Starter: The device produces a miniature flame, which you can use to light a candle, torch, or campfire. Using the device requires your action; Music Box: When opened, this music box plays a single song at a moderate volume. The box stops playing when it reaches the song's end or when it is closed. ")

    def gnome_forest_choose(self):
        self.new_character.dextery += 1
        #self.new_character.spells
        self.new_character.special_abilities.append("Speak with Small Beasts. Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts. Forest gnomes love animals and often keep squirrels, badgers, rabbits, moles, woodpeckers, and other creatures as beloved pets.")
        self.gnome_window.destroy()
        self.customization_screen3()
    def gnome_rock_choose(self):
        self.new_character.constitution += 1
        self.new_character.special_abilities.append("Artificer's Lore. Whenever you make an Intelligence (History) check related to magic items, alchemical objects, or technological devices, you can add twice your proficiency bonus, instead of any proficiency bonus you normally apply.")
        self.new_character.special_abilities.append("Tinker. You have proficiency with artisan's tools (tinker's tools). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time. When you create a device, choose one of the following options: Clockwork Toy. This toy is a clockwork animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier. When placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents; Fire Starter: The device produces a miniature flame, which you can use to light a candle, torch, or campfire. Using the device requires your action; Music Box: When opened, this music box plays a single song at a moderate volume. The box stops playing when it reaches the song's end or when it is closed.")
        self.gnome_window.destroy()
        self.customization_screen3()


    def half_elf_choose(self):
        self.new_character.race = "Half-Elf"
        self.new_character.charisma += 2
        self.new_character.languages += ["Commom","Elvish"]
        self.new_character.darkvision = True
        self.new_character.darkvision_range = "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light."
        self.new_character.resistence.append("Charmed")
        self.proficiency_choose()
        self.language_choose()
        self.new_character.special_abilities.append("You have advantage on saving throws against been charmed")
        self.new_character.special_abilities.append("magic can't put you to sleep, Elves don't need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day, After resting in this way, you gain the same benefit that a human does from 8 hours of sleep")
        self.customization_window2.destroy()
        #self.half_elf_window = Toplevel (self.root)
        #text_half_elf = Label(self.half_elf_window, text="Choose two of the attributes")
        #text_half_elf.pack()
        self.atributtes_choose(2,"Charisma")
        


    def half_orc_choose(self):
        self.new_character.race = "Half-Orc"
        self.new_character.strength += 2
        self.new_character.languages += ["Commom","Elvish"]
        self.new_character.darkvision = True
        self.new_character.darkvision_range = "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light."
        self.new_character.resistence.append("Charmed")
        self.proficiency_choose()
        self.language_choose()
        self.new_character.special_abilities.append("You have advantage on saving throws against been charmed")
        self.new_character.special_abilities.append("magic can't put you to sleep, Elves don't need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day, After resting in this way, you gain the same benefit that a human does from 8 hours of sleep")
        self.customization_window2.destroy()
        self.customization_screen3()

    def customization_screen3(self):
        self.customization_window2.destroy()
        self.customization_window3 = Toplevel(self.root)
        self.customization_window3.title("Class Customization")
        self.customization_window3.geometry("800x800")
        self.customization_window3.resizable(False, False)

    def validate_number(self, new_value, attribute):
        if not new_value.isdigit():
            return False
        if int(new_value) < 8 or int(new_value) > 15:
            return False
        
        if attribute == "strength":
            delta = self.calculate_skill_points(int(new_value)) - self.calculate_skill_points(int(self.new_character.strength))
            self.points_remaining = self.points_remaining - delta
            self.new_character.strength = new_value
            self.new_character.strength_mod = new_value // 2
        
        elif attribute == "dexterity":
            delta = self.calculate_skill_points(int(new_value)) - self.calculate_skill_points(int(self.new_character.dextery))
            self.points_remaining = self.points_remaining - delta
            self.new_character.dextery = new_value
            self.new_character.dextery_mod = new_value // 2

        elif attribute == "constitution":
            delta = self.calculate_skill_points(int(new_value)) - self.calculate_skill_points(int(self.new_character.constitution))
            self.points_remaining = self.points_remaining - delta
            self.new_character.constitution = new_value
            self.new_character.constitution_mod = new_value // 2

        elif attribute == "intelligence":
            delta = self.calculate_skill_points(int(new_value)) - self.calculate_skill_points(int(self.new_character.intelligence))
            self.points_remaining = self.points_remaining - delta
            self.new_character.intelligence = new_value
            self.new_character.intelligence_mod = new_value // 2
        
        elif attribute == "wisdom":
            delta = self.calculate_skill_points(int(new_value)) - self.calculate_skill_points(int(self.new_character.wisdom))
            self.points_remaining = self.points_remaining - delta
            self.new_character.wisdom = new_value
            self.new_character.wisdom_mod = new_value // 2
        
        elif attribute == "charisma":
            delta = self.calculate_skill_points(int(new_value)) - self.calculate_skill_points(int(self.new_character.charisma))
            self.points_remaining = self.points_remaining - delta
            self.new_character.charisma = new_value
            self.new_character.charisma_mod = new_value // 2
        else:
            return False

        self.points_label.config(text = f"Points available: {self.points_remaining}")
        return True

    def calculate_skill_points(self,points):
        atribute_coast = {8:0, 9:1, 10:2, 11:3, 12:4, 13:5, 14:7, 15:9}
        cost = atribute_coast[points]
        return cost

    def proficiency_choose(self):
        return
    
    def language_choose(self):
        return
      
    def atributtes_choose(self,repeat,atributte):
        self.counter = 0
        while repeat > 0:

            self.atributte_choose_window = Toplevel(self.root)
            #seleção dos atributos
            if atributte != "Strength" and self.counter != 1:
                self.str_increase_button= Button(self.atributte_choose_window, text="Strength", command=self.increase_strength)
                self.str_increase_button.pack()
                
            if atributte != "Dexterity" and self.counter != 2:
                self.dex_increase_button= Button(self.atributte_choose_window, text="Dexterity", command=self.increase_dexterity)
                self.dex_increase_button.pack()
                
            if atributte != "Constitution" and self.counter != 3:
                self.con_increase_button= Button(self.atributte_choose_window, text="Constitution", command=self.increase_constitution)
                self.con_increase_button.pack()
               
            if atributte != "Intelligence" and self.counter != 4:
                self.int_increase_button= Button(self.atributte_choose_window, text="Intelligence", command=self.increase_intelligence)
                self.int_increase_button.pack()
                
            if atributte != "Wisdom" and self.counter != 5:
                self.wis_increase_button= Button(self.atributte_choose_window, text="Wisdom", command=self.increase_wisdom)
                self.wis_increase_button.pack()
                
            if atributte != "Charisma" and self.counter != 6:
                self.cha_increase_button= Button(self.atributte_choose_window, text="Charisma", command=self.increase_charisma)
                self.cha_increase_button.pack()
                
            repeat = repeat -1
            self.root.wait_window(self.atributte_choose_window)
            print(self.counter)
            
            

                
            
            
            

    def increase_strength(self):
        self.new_character.strength += 1
        self.atributte_choose_window.destroy()
        self.counter = 1
    def increase_dexterity(self):
        self.new_character.dextery += 1
        self.atributte_choose_window.destroy()
        self.counter = 2
    def increase_constitution(self):
        self.new_character.constitution += 1
        self.atributte_choose_window.destroy()
        self.counter = 3
    def increase_intelligence(self):
        self.new_character.intelligence += 1
        self.atributte_choose_window.destroy()
        self.counter = 4
    def increase_wisdom(self):
        self.new_character.wisdom += 1
        self.atributte_choose_window.destroy()
        self.counter = 5
    def increase_charisma(self):
        self.new_character.charisma += 1
        self.atributte_choose_window.destroy()
        self.counter = 6
        


