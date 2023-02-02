from tkinter import *
from tkinter import ttk
from Character import Character
    

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

        print(new_character.level)
        print(new_character.name)
        print(new_character.proficiency_bonus)
        print(new_character.character_id)
        print(new_character.strength)
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
        self.strength_entry = Entry(self.customization_window, validate="focusin")
        self.strength_entry.place(relx=0.4, rely=0.1)
        self.dexterity_entry = Entry(self.customization_window, validate="focusin")
        self.dexterity_entry.place(relx=0.4, rely=0.2)
        self.constitution_entry = Entry(self.customization_window, validate="focusin")
        self.constitution_entry.place(relx=0.4, rely=0.3)
        self.intelligence_entry = Entry(self.customization_window, validate="focusin")
        self.intelligence_entry.place(relx=0.4, rely=0.4)
        self.wisdom_entry = Entry(self.customization_window, validate="focusin")
        self.wisdom_entry.place(relx=0.4, rely=0.5)
        self.charisma_entry = Entry(self.customization_window, validate="focusin")
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
    
        


        

    def validate_number(self, new_value, attribute):
        if not new_value.isdigit():
            return False
        if int(new_value) < 8 or int(new_value) > 15:
            return False
        
        if attribute == "strength":
            old_value = self.new_character.strength
            delta = self.calculate_skill_points(int(new_value)) - self.calculate_skill_points(int(old_value))
            self.points_remaining = self.points_remaining - delta
            self.new_character.strength = new_value
        
        elif attribute == "dexterity":
            old_value = self.new_character.dextery
            delta = self.calculate_skill_points(int(new_value)) - self.calculate_skill_points(int(old_value))
            self.points_remaining = self.points_remaining - delta
            self.new_character.dextery = new_value

        elif attribute == "constitution":
            old_value = self.new_character.dextery
            delta = self.calculate_skill_points(int(new_value)) - self.calculate_skill_points(int(old_value))
            self.points_remaining = self.points_remaining - delta
            self.new_character.constitution = new_value

        elif attribute == "intelligence":
            old_value = self.new_character.intelligence
            delta = self.calculate_skill_points(int(new_value)) - self.calculate_skill_points(int(old_value))
            self.points_remaining = self.points_remaining - delta
            self.new_character.intelligence = new_value
        
        elif attribute == "wisdom":
            old_value = self.new_character.wisdom
            delta = self.calculate_skill_points(int(new_value)) - self.calculate_skill_points(int(old_value))
            self.points_remaining = self.points_remaining - delta
            self.new_character.wisdom = new_value
        
        elif attribute == "charisma":
            old_value = self.charisma_entry.get()
            delta = self.calculate_skill_points(int(new_value)) - self.calculate_skill_points(int(old_value))
            self.points_remaining = self.points_remaining - delta
            self.new_character.charisma = new_value

        else:
            return False

        self.points_label.config(text = f"Points available: {self.points_remaining}")
        return True

    def calculate_skill_points(self,points):
        atribute_coast = {8:0, 9:1, 10:2, 11:3, 12:4, 13:5, 14:7, 15:9}
        cost = atribute_coast[points]
        return cost


        


