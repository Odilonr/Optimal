import customtkinter as ctk
from ..utils.constant import BLUE_GRAY_TEST,BLUE_GRAY
class Log(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=BLUE_GRAY,corner_radius=0)
        self.columnconfigure((0,1),weight = 1)
        self.rowconfigure((0,1,2,3), weight=1)
        self.top_level_window = None
        self.create_widgets()
        self.place_widgets()
        

    def create_widgets(self):
        self.breakfast = MealFrame_left(self,'Breakfast')
        self.lunch = MealFrame_right(self,'Lunch')
        self.dinner = MealFrame_left(self,'Dinner')
        self.snack = MealFrame_right(self,'Snack')
        self.breakfast.add_button.configure(command=self.add_command)
        self.lunch.add_button.configure(command= self.add_command)
        self.dinner.add_button.configure(command= self.add_command)
        self.snack.add_button.configure(command= self.add_command)
       

    def place_widgets(self):
        self.breakfast.grid(row=0, column =0, sticky='nswe',padx=10,pady=10)
        self.lunch.grid(row=1, column =0, sticky='nswe',padx=10,pady=10)
        self.dinner.grid(row=2, column =0, sticky='nswe',padx=10,pady=10)
        self.snack.grid(row=3, column =0, sticky='nswe',padx=10,pady=10)

    def add_command(self):
        if self.top_level_window is None or not self.top_level_window.winfo_exists():
            self.top_level_window = MealEntryTopLevel(master=self)
        else:
            self.top_level_window.focus()


    def show(self):
        self.grid(row=0,column=1,sticky='wnse',columnspan=2)
    
    def hide(self):
        self.grid_forget()


class MealFrame_left(ctk.CTkFrame):
    def __init__(self,master, type):
        super().__init__(master, fg_color=BLUE_GRAY_TEST,width=50,corner_radius=10)
        self.type = type
        self.rowconfigure((0,1), weight=1)
        self.columnconfigure((0,1,2,3,4,5),weight=1)
        self.create_widgets()
        self.place_widgets()

    def create_widgets(self):
        self.title = ctk.CTkLabel(self, text=f'{self.type}', font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')
        self.add_button = ctk.CTkButton(self, text='+Add', font=('Microsoft Yahei UI Light', 17, 'bold'),
                                        corner_radius=20,width=45)

    def place_widgets(self):
        self.title.grid(row=0, column =0, sticky='w', padx=10,pady=10)
        self.add_button.grid(row=1, column=0, sticky='sw',padx=10,pady=10)

class MealFrame_right(ctk.CTkFrame):
    def __init__(self,master,type):
        super().__init__(master, fg_color=BLUE_GRAY_TEST,width=50,corner_radius=10)
        self.type = type
        self.rowconfigure((0,1), weight=1)
        self.columnconfigure((0,1,2,3,4,5),weight=1)
        self.create_widgets()
        self.place_widgets()

    def create_widgets(self):
        self.title = ctk.CTkLabel(self, text=f'{self.type}', font=('Microsoft Yahei UI Light', 20, 'bold'),text_color='white')
        self.add_button = ctk.CTkButton(self, text='+Add', font=('Microsoft Yahei UI Light', 17, 'bold'),
                                        corner_radius=20, width=45)

    def place_widgets(self):
        self.title.grid(row=0, column =5, sticky='e', padx=10,pady=10)
        self.add_button.grid(row=1, column=5, sticky='se',padx=10, pady=10)

class MealEntryTopLevel(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master, fg_color=BLUE_GRAY)
        self.title = 'Meal Entry'
        x = master.winfo_x()  + master.winfo_width() - self.winfo_width()
        y = master.winfo_y()  + master.winfo_height() - self.winfo_height()
        self.wait_visibility()
        self.geometry(f'+{x}+{y}')
        self.resizable(False,False)
        self.font_fields = ctk.CTkFont(family = 'Microsoft Yahei UI', size = 13)
        self.grab_set()

        self.columnconfigure((0,1), weight=1)
        self.rowconfigure((0,1,2,3,4), weight=1)
        
        self.create_widgets()
        self.place_widgets()

    def create_widgets(self):
        self.foodName_entry = ctk.CTkEntry(self, width=100,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields, placeholder_text='Food',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black')
        self.amount_entry = ctk.CTkEntry(self, width=50,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields, placeholder_text='g',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black')
        self.carbs_entry = ctk.CTkEntry(self, width=100,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields, placeholder_text='Carbs',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black')
        self.protein_entry = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields, placeholder_text='Protein',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black')
        self.fat_entry = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields, placeholder_text='Fat',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black')
        self.enter_button = ctk.CTkButton(self, text='Enter',width=140, height=50,border_width=1, border_color='white',fg_color=BLUE_GRAY,
                                            text_color='white',hover_color='#0c1545', font=self.font_fields, corner_radius=0,
                                            )
    
    def place_widgets(self):
        self.foodName_entry.grid(row=0, column=0,padx = 20,pady=10, sticky='nw')
        self.amount_entry.grid(row=0, column=1, padx=20,pady=10,sticky='nw')
        self.carbs_entry.grid(row=1,column=0, padx = 20,pady=10, sticky='nw')
        self.protein_entry.grid(row=2, column =0, padx = 20,pady=10, sticky='nw')
        self.fat_entry.grid(row=3, column=0, padx = 20,pady=10,sticky='nw')
        self.enter_button.grid(row=4,column=0, padx = 60,pady=20, sticky='e')
  
        

