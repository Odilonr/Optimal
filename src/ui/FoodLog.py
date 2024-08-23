import customtkinter as ctk
from ..utils.constant import BLUE_GRAY_TEST,BLUE_GRAY
from ..utils.session_manager import session_manager
from ..data.database_manager import database
import itertools
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
        self.breakfast = MealFrame(self,'breakfast')
        self.lunch = MealFrame(self,'lunch')
        self.dinner = MealFrame(self,'dinner')
        self.sleep_step = Stepsleep(self)
        self.breakfast.add_button.configure(command = lambda: self.add_command(type='breakfast'))
        self.lunch.add_button.configure(command = lambda: self.add_command(type='lunch'))
        self.dinner.add_button.configure(command = lambda: self.add_command(type='dinner'))
       

    def place_widgets(self):
        self.breakfast.grid(row=0, column =0, sticky='nswe',padx=10,pady=10)
        self.lunch.grid(row=1, column =0, sticky='nswe',padx=10,pady=10)
        self.dinner.grid(row=2, column =0, sticky='nswe',padx=10,pady=10)
        self.sleep_step.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)

    def add_command(self, type):
        if self.top_level_window is None or not self.top_level_window.winfo_exists():
            self.top_level_window = MealEntryTopLevel(master=self, type=type)
        else:
            self.top_level_window.focus()

    def show(self):
        self.grid(row=0,column=1,sticky='wnse',columnspan=2)
    
    def hide(self):
        self.grid_forget()

    def refresh_user(self, selected_date = None):
        if selected_date is None:
            selected_date = self.master.get_selected_date()

        self.breakfast.refresh_user(date=selected_date)
        self.lunch.refresh_user(date=selected_date)
        self.dinner.refresh_user(date=selected_date)


class MealFrame(ctk.CTkFrame):
    def __init__(self,master, type):
        super().__init__(master, fg_color=BLUE_GRAY_TEST,width=50,corner_radius=10)
        self.type = type
        self.current_user = session_manager.get_current_user()
        self.food_labels = []
        self.rowconfigure((0,1), weight=1)
        self.columnconfigure((0,1,2,3,4,5),weight=1, uniform='b')
        self.columnconfigure(2, weight=1, uniform='b')
        self.create_widgets()
        self.place_widgets()


    def create_widgets(self):
        self.title = ctk.CTkLabel(self, text=f'{self.type}', font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')
        self.add_button = ctk.CTkButton(self, text='+Add', font=('Microsoft Yahei UI Light', 17, 'bold'),
                                        corner_radius=20,width=45)
        
        self.empty_label_one = ctk.CTkLabel(self,font=('Microsoft Yahei UI Light', 12, 'bold'), text_color='white')
        self.empty_label_two = ctk.CTkLabel(self,font=('Microsoft Yahei UI Light', 12, 'bold'), text_color='white')
        self.empty_label_three = ctk.CTkLabel(self,font=('Microsoft Yahei UI Light', 12, 'bold'), text_color='white')
        self.empty_label_four = ctk.CTkLabel(self,font=('Microsoft Yahei UI Light', 12, 'bold'), text_color='white')
        self.empty_label_five = ctk.CTkLabel(self, font=('Microsoft Yahei UI Light', 12, 'bold'), text_color='white')
        self.empty_label_six = ctk.CTkLabel(self, font=('Microsoft Yahei UI Light', 12, 'bold'), text_color='white')
        self.empty_label_seven = ctk.CTkLabel(self, font=('Microsoft Yahei UI Light', 12, 'bold'), text_color='white')
        self.empty_label_height = ctk.CTkLabel(self, font=('Microsoft Yahei UI Light', 12, 'bold'), text_color='white')

    def place_widgets(self):
        self.title.grid(row=0, column =0, sticky='w', padx=10,pady=10)
        self.add_button.grid(row=1, column=0, sticky='sw',padx=10,pady=10)
        

    def clear_items(self):
        if self.food_labels:
            for label in self.food_labels:
                label.destroy()
        self.food_labels = []


    def refresh_user(self, date):
        self.clear_items()

        list_food = database.grab_food(athlete_id=self.current_user.id, date=date, meal_type=self.type)
        myfunc = itertools.cycle([0,1]).__next__
        if list_food:
            for i, food in enumerate(list_food):
                food_string = f'{food[0]}, {food[1]}'
                label = ctk.CTkLabel(self, text = f"{food_string}",font=('Microsoft Yahei UI Light', 10, 'bold'),
                                     text_color='white')
                label.grid(row = myfunc(), column=(i//2) % 3 + 1, sticky = 'w', pady =10)
                self.food_labels.append(label)
            print('Record today')
        else:
            print('no record fot that day!')
            return
        


class Stepsleep(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master, fg_color=BLUE_GRAY_TEST,width=50,corner_radius=10)
        self.master = master
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
                                               command=lambda: self.update_step_sleep(info=('minus','step')), state='disabled')
        self.plus_button_step = ctk.CTkButton(self, text='+', fg_color = BLUE_GRAY_TEST, text_color='white',font=('Microsoft Yahei UI Light', 20, 'bold'),
                                            command=lambda: self.update_step_sleep(info=('plus','step')),state='disabled')
        
        self.minus_button_sleep = ctk.CTkButton(self, text='-', fg_color = BLUE_GRAY_TEST, text_color='white',font=('Microsoft Yahei UI Light', 20, 'bold'),
                                                command=lambda: self.update_step_sleep(info=('minus','sleep')), state='disabled')
        self.plus_button_sleep = ctk.CTkButton(self, text='+', fg_color = BLUE_GRAY_TEST, text_color='white',font=('Microsoft Yahei UI Light', 20, 'bold'),
                                               command=lambda: self.update_step_sleep(info=('plus','sleep')), state='disabled')

        self.save_button_steps = ctk.CTkButton(self, text='Save', font=('Microsoft Yahei UI Light', 17, 'bold'), command = lambda: self.update_steps_db(info='step'))
        self.update_button_steps = ctk.CTkButton(self, text='Update', font=('Microsoft Yahei UI Light', 17, 'bold'), command = lambda: self.update_trigger(info='step'))

        self.save_button_sleep = ctk.CTkButton(self, text='Save', font=('Microsoft Yahei UI Light', 17, 'bold'), command = lambda: self.update_steps_db(info='sleep'))
        self.update_button_sleep = ctk.CTkButton(self, text='Update', font=('Microsoft Yahei UI Light', 17, 'bold'), command = lambda: self.update_trigger(info='sleep'))

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

        self.update_button_steps.grid(row=0, column =4, sticky='nsw',padx = 8, pady=8)
        self.update_button_sleep.grid(row = 1, column = 4, sticky = 'nsw', padx = 8, pady = 8)


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


    def update_steps_db(self, info):
        date = self.master.current_date
        ##to_day = date.today().isoformat()
        if info == 'step':
            new_step = int(self.output_string_step.get())
            new_sleep = 0
            self.save_button_steps.grid_forget()
            self.update_button_steps.grid(row=0, column =4, sticky='nsw',padx = 8, pady=8)
            self.plus_button_step.configure(state='disabled')
            self.minus_button_step.configure(state='disabled')
        elif info == 'sleep':
            new_sleep = int(self.output_string_sleep.get())
            new_step = 0
            self.save_button_sleep.grid_forget()
            self.update_button_sleep.grid(row=1, column =4, sticky='nsw',padx = 8, pady=8)
            self.plus_button_sleep.configure(state='disabled')
            self.minus_button_sleep.configure(state='disabled')
        else:
            return

        self.current_user.update_step_sleep_record(steps = new_step, sleep = new_sleep, date = date)

    
    def update_trigger(self, info):
        if info == 'step':
            self.update_button_steps.grid_forget()
            self.save_button_steps.grid(row=0, column =4, sticky='nsw',padx = 8, pady=8)
            self.plus_button_step.configure(state='normal')
            self.minus_button_step.configure(state='normal')
        elif info == 'sleep':
            self.update_button_sleep.grid_forget()
            self.save_button_sleep.grid(row=1, column =4, sticky='nsw',padx = 8, pady=8)
            self.plus_button_sleep.configure(state='normal')
            self.minus_button_sleep.configure(state='normal')
        else:
            return


class MealEntryTopLevel(ctk.CTkToplevel):
    def __init__(self, master, type):
        super().__init__(master, fg_color=BLUE_GRAY)
        self.master = master
        self.type = type
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
        self.amount_entry = ctk.CTkEntry(self, width=64,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields, placeholder_text='amount',placeholder_text_color='#050000',
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
        
        self.units_options = ctk.CTkOptionMenu(self, values = ['g', 'oz', 'tbsp', 'fl oz'], width=50, height=50, fg_color='white',
                                          text_color='black', corner_radius=0, dropdown_fg_color='white', dropdown_text_color='black',
                                          button_hover_color='#e6f0ef', button_color='white')
        
        self.enter_button = ctk.CTkButton(self, text='Enter',width=140, height=50,border_width=1, border_color='white',fg_color=BLUE_GRAY,
                                            text_color='white',hover_color='#0c1545', font=self.font_fields, corner_radius=0,
                                            command=self.enter_command)
        
    
    def place_widgets(self):
        self.foodName_entry.grid(row=0, column=0,padx = 20,pady=10, sticky='nw')
        self.amount_entry.grid(row=1, column=1, padx=20,pady=10,sticky='nw')
        self.units_options.grid(row =0, column =1, padx = 20, pady= 10, sticky ='nw')
        self.carbs_entry.grid(row=1,column=0, padx = 20,pady=10, sticky='nw')
        self.protein_entry.grid(row=2, column =0, padx = 20,pady=10, sticky='nw')
        self.fat_entry.grid(row=3, column=0, padx = 20,pady=10,sticky='nw')
        self.enter_button.grid(row=4,column=0, padx = 60,pady=20, sticky='e')

    def enter_command(self):
        date = self.master.master.get_current_date()
        ##to_day = date.today().isoformat()
        try:
            carbs = int(self.carbs_entry.get())
        except Exception as e:
            carbs = 0
        try:
            protein = int(self.protein_entry.get())
        except Exception as e:
            protein = 0
        try:
            fat = int(self.fat_entry.get())
        except:
            fat = 0
        try:
            amount_entry = f"{self.amount_entry.get()}{self.units_options.get()}"
        except:
            amount_entry = ''

        database.add_food(self.current_user.id,meal_type=self.type,date=date,food_name=f'{self.foodName_entry.get()}',
                          amount=amount_entry,carbs=carbs, protein=protein, 
                          fat=fat)
        
        self.current_user.update_food_record(carbs = carbs, protein = protein, fat = fat, date = date)

        self.master.refresh_user(date)
       
        self.destroy()

    
  
        

