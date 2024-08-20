import customtkinter as ctk
from ..utils.constant import BLUE_GRAY_TEST,BLUE_GRAY
from ..utils.session_manager import session_manager
from datetime import date


class Log(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=BLUE_GRAY,corner_radius=0)
        self.current_user = session_manager.get_current_user()
        self.columnconfigure((0,1),weight = 1)
        self.rowconfigure((0,1,2,3,4,5,6), weight=1)
        self.top_level_window = None
        self.create_widgets()
        self.place_widgets()
        
    def create_widgets(self):
        self.breakfast = MealFrame_left(self,'Breakfast')
        self.lunch = MealFrame_right(self,'Lunch')
        self.dinner = MealFrame_left(self,'Dinner')
        self.sleep_step = Stepsleep(self)
        self.breakfast.add_button.configure(command = self.add_command)
        self.lunch.add_button.configure(command = self.add_command)
        self.dinner.add_button.configure(command = self.add_command)
       

    def place_widgets(self):
        self.breakfast.grid(row=0, column =0, sticky='nswe',padx=10,pady=10)
        self.lunch.grid(row=1, column =0, sticky='nswe',padx=10,pady=10)
        self.dinner.grid(row=2, column =0, sticky='nswe',padx=10,pady=10)
        self.sleep_step.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)

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

class Stepsleep(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master, fg_color=BLUE_GRAY_TEST,width=50,corner_radius=10)
        self.type = type
        self.current_user = session_manager.get_current_user()
        self.rowconfigure((0,1), weight=1)
        self.columnconfigure((0,1,2,3,4),weight=1, uniform='b')
        self.columnconfigure(2, weight=1, uniform='b')
        self.output_string_step = ctk.StringVar()
        self.output_string_sleep = ctk.StringVar()
        self.starting_step = ctk.IntVar(value = 200)
        self.starting_sleep = ctk.IntVar(value = 8)
        self.update_step_sleep()



        self.step_label = ctk.CTkLabel(self, text=f'Steps', font=('Microsoft Yahei UI Light', 20, 'bold'),text_color='white')
        self.sleep_label = ctk.CTkLabel(self, text=f'Sleep', font=('Microsoft Yahei UI Light', 20, 'bold'),text_color='white')

        self.minus_button_step = ctk.CTkButton(self, text='-', fg_color = BLUE_GRAY_TEST, text_color='white',font=('Microsoft Yahei UI Light', 20, 'bold'),
                                               command=lambda: self.update_step_sleep(info=('minus','step')))
        self.plus_button_step = ctk.CTkButton(self, text='+', fg_color = BLUE_GRAY_TEST, text_color='white',font=('Microsoft Yahei UI Light', 20, 'bold'),
                                            command=lambda: self.update_step_sleep(info=('plus','step')))
        
        self.minus_button_sleep = ctk.CTkButton(self, text='-', fg_color = BLUE_GRAY_TEST, text_color='white',font=('Microsoft Yahei UI Light', 20, 'bold'),
                                                command=lambda: self.update_step_sleep(info=('minus','sleep')))
        self.plus_button_sleep = ctk.CTkButton(self, text='+', fg_color = BLUE_GRAY_TEST, text_color='white',font=('Microsoft Yahei UI Light', 20, 'bold'),
                                               command=lambda: self.update_step_sleep(info=('plus','sleep')))

        self.update_button = ctk.CTkButton(self, text='Update', font=('Microsoft Yahei UI Light', 17, 'bold'), command=self.update_steps_db)
        self.output_label_step = ctk.CTkLabel(self, textvariable = self.output_string_step, text_color='white', font=('Microsoft Yahei UI Light', 17, 'bold'))
        self.output_label_sleep = ctk.CTkLabel(self, textvariable = self.output_string_sleep, text_color='white', font=('Microsoft Yahei UI Light', 17, 'bold'))

        self.step_label.grid(row=0, column =0, sticky='nsw', padx=10,pady=10)
        self.sleep_label.grid(row=1, column =0, sticky='nsw', padx=10,pady=10)

        self.minus_button_step.grid(row=0, column = 1, sticky='nsw', padx=8, pady=8)
        self.output_label_step.grid(row=0, column = 2)

        self.output_label_sleep.grid(row=1, column = 2)
        self.plus_button_step.grid(row=0, column =3,sticky='nsw', padx=8, pady=8 )

        self.minus_button_sleep.grid(row=1, column = 1, sticky='nsw', padx=8, pady=8)
        self.plus_button_sleep.grid(row=1, column= 3,sticky='nsw', padx=8, pady=8 )

        self.update_button.grid(row=1, column =4, sticky='nsw',padx = 8, pady=8)


    def update_step_sleep(self, info = None):
        if info:
            if info[1] == 'step':
                if info[0] == 'plus':
                    self.starting_step.set(self.starting_step.get() + 1)
                    self.output_string_step.set(f'{self.starting_step.get()}')
                else:
                    self.starting_step.set(self.starting_step.get() - 1)
                    self.output_string_step.set(f'{self.starting_step.get()}')
            else:
                if info[0] == 'plus':
                    self.starting_sleep.set(self.starting_sleep.get() + 1)
                    self.output_string_sleep.set(f'{self.starting_sleep.get()}')
                else:
                    self.starting_sleep.set(self.starting_sleep.get() - 1)
                    self.output_string_sleep.set(f'{self.starting_sleep.get()}')
        else:
            self.output_string_step.set(value=f'{self.starting_step.get()}')
            self.output_string_sleep.set(value=f'{self.starting_sleep.get()}')


    def update_steps_db(self):
        to_day = date.today().isoformat()
        new_step = int(self.output_string_step.get())
        new_sleep = int(self.output_string_sleep.get())
        self.current_user.update_step_sleep_record(steps = new_step, sleep = new_sleep, date = to_day)


       

 
        

    



class MealEntryTopLevel(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master, fg_color=BLUE_GRAY)
        self.current_user = session_manager.get_current_user()
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
                                            command=self.enter_command)
    
    def place_widgets(self):
        self.foodName_entry.grid(row=0, column=0,padx = 20,pady=10, sticky='nw')
        self.amount_entry.grid(row=0, column=1, padx=20,pady=10,sticky='nw')
        self.carbs_entry.grid(row=1,column=0, padx = 20,pady=10, sticky='nw')
        self.protein_entry.grid(row=2, column =0, padx = 20,pady=10, sticky='nw')
        self.fat_entry.grid(row=3, column=0, padx = 20,pady=10,sticky='nw')
        self.enter_button.grid(row=4,column=0, padx = 60,pady=20, sticky='e')

    def enter_command(self):
        to_day = date.today().isoformat()
        carbs = int(self.carbs_entry.get())
        protein = int(self.protein_entry.get())
        fat = int(self.fat_entry.get())
        self.current_user.update_food_record(carbs = carbs, protein = protein, fat = fat, date = to_day)
        self.destroy()
  
        

