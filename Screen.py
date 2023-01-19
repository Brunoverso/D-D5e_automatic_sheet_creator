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

     
        


        





        


