import customtkinter as ctk
from ..utils.constant import BLUE_GRAY
import tkinter as tk
from ..utils.session_manager import session_manager
from ..data.database_manager import database
from datetime import date
import math
    
class DayNumbers(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=BLUE_GRAY, width=300, height=200)
        self.master = master
        self.current_user = session_manager.get_current_user()
        current_date = self.master.date_selector.get_date()
        current_daily_record = self.current_user.current_daily_record(current_date)
        self.grid(row = 2, column =0 ,rowspan =4,sticky='nswe',padx = 10, pady = 10)
        self.columnconfigure((0,1,2), weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        


        self.current_calorie_remaing = ctk.StringVar(value=f'{current_daily_record[3]}')
        self.current_steps = ctk.StringVar(value='0')
        self.current_sleep = ctk.StringVar(value='0')

        self.calorie_bar = CircleProgressBar(self, width=190, height = 190, fg_color='#50c878', label='Calories remaining',
                                             progress=0)
        self.calorie_bar.grid(row = 0, column = 0)
        self.calorie_bar.set_progress(0, self.current_calorie_remaing)
        
        self.step_bar = CircleProgressBar(self, width=190, height = 190, fg_color='#50c878', label='Steps',
                                          progress=0)
        self.step_bar.grid(row = 0, column = 1)
        self.step_bar.set_progress(0, self.current_steps)

        self.sleep_bar = CircleProgressBar(self, width=190, height = 190,fg_color='#50c878', label='Sleep',
                                           progress=0)
        self.sleep_bar.grid(row = 0, column = 2)
        self.sleep_bar.set_progress(0, self.current_sleep)



        self.current_carb_goal = ctk.StringVar(value=f'{current_daily_record[11]}')
        self.current_protein_goal = ctk.StringVar(value=f"{current_daily_record[13]}")
        self.current_fat_goal = ctk.StringVar(value=f'{current_daily_record[15]}')



        self.macros = ctk.CTkFrame(self, fg_color=BLUE_GRAY)
        self.macros.grid(row = 0, column=3, sticky='nswe')
        self.macros.columnconfigure((0,1),weight=1)
        self.macros.rowconfigure((0,1,2,4,5), weight=1)

        self.carbs = ctk.CTkLabel(self.macros, text='Carbs', font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')
        self.carbs.grid(row = 0, column = 0, sticky='nw')
        self.carb_goal = ctk.CTkLabel(self.macros,textvariable = self.current_carb_goal, font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')
        self.carb_goal.grid(row = 0, column =0, sticky= 'e')
        self.carbs_progress = ctk.CTkProgressBar(self.macros, orientation='horizontal',width=300,height=20, progress_color='#50c878',corner_radius=0,
                                                 mode = "determinate")
        self.carbs_progress.grid(row=1,column=0, sticky='w',pady=10)

        self.protein = ctk.CTkLabel(self.macros, text='Protein', font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')
        self.protein.grid(row =2, column = 0, sticky='nw')
        self.protein_goal = ctk.CTkLabel(self.macros, textvariable = self.current_protein_goal, font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')
        self.protein_goal.grid(row = 2, column =0, sticky= 'e')
        self.protein_progress = ctk.CTkProgressBar(self.macros, orientation='horizontal',width=300,height=20, progress_color='#50c878',corner_radius=0)
        self.protein_progress.grid(row=3,column=0,sticky='w',pady=10)

        self.fat = ctk.CTkLabel(self.macros, text='Fat', font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')
        self.fat.grid(row =4, column = 0, sticky='nw')
        self.fat_goal = ctk.CTkLabel(self.macros, textvariable = self.current_fat_goal, font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')
        self.fat_goal.grid(row = 4, column =0, sticky= 'e')
        self.fat_progress = ctk.CTkProgressBar(self.macros, orientation='horizontal',width=300,height=20, progress_color='#50c878',corner_radius=0)
        self.fat_progress.grid(row=5,column=0,sticky='w',pady=10)

        

    def progress_update(self, selected_date,carb_goal, protein_goal, fat_goal):  
        self.current_user = session_manager.get_current_user()
        current_daily_record = self.current_user.current_daily_record(selected_date)

        if current_daily_record:
            value_carbs = current_daily_record[10]/ carb_goal
            value_protein = current_daily_record[12] / protein_goal
            value_fat = current_daily_record[14] / fat_goal
            self.carbs_progress.set(value=value_carbs)
            self.protein_progress.set(value=value_protein)
            self.fat_progress.set(value=value_fat)
        else:
            self.carbs_progress.set(value=0)
            self.protein_progress.set(value=0)
            self.fat_progress.set(value=0)


    def refresh_user(self, selected_date):
        self.current_user = session_manager.get_current_user()
        current_goal_numbers = self.current_user.current_daily_record(selected_date)
        if current_goal_numbers:
            self.current_carb_goal.set(f'{current_goal_numbers[11]}')
            self.current_protein_goal.set(f'{current_goal_numbers[13]}')
            self.current_fat_goal.set(f'{current_goal_numbers[15]}')
            self.progress_update(selected_date=selected_date, carb_goal=current_goal_numbers[11],
                                protein_goal=current_goal_numbers[13], fat_goal=current_goal_numbers[15])
            
            self.update_steps_sleep_cals(selected_date=selected_date, cal_goal = current_goal_numbers[3],
                                        step_goal=current_goal_numbers[7], sleep_goal=current_goal_numbers[9])
        else:
            self.current_carb_goal.set(f'None')
            self.current_protein_goal.set(f'None')
            self.current_fat_goal.set(f'None')
            self.calorie_bar.set_progress(0, f'None')
            self.step_bar.set_progress(0, f'0')
            self.sleep_bar.set_progress(0, f'0')
            self.carbs_progress.set(value=0)
            self.protein_progress.set(value=0)
            self.fat_progress.set(value=0)


    def update_steps_sleep_cals(self, selected_date,cal_goal, step_goal, sleep_goal):
        self.current_user = session_manager.get_current_user()
        current_daily_record = self.current_user.current_daily_record(selected_date)

        if current_daily_record:

            calories_consumed = current_daily_record[4]
            cals_percentage = (calories_consumed /cal_goal) * 100
            self.calorie_bar.set_progress(cals_percentage, f'{current_daily_record[5]}')

            steps_percentage = (current_daily_record[6] / step_goal) * 100
            self.step_bar.set_progress(steps_percentage, f'{current_daily_record[6]}')

            sleep_percentage = (current_daily_record[8] / sleep_goal) * 100
            self.sleep_bar.set_progress(sleep_percentage, f'{current_daily_record[8]}')
        
        else:
            self.calorie_bar.set_progress(0, f'{cal_goal}')
            self.step_bar.set_progress(0, f'0')
            self.sleep_bar.set_progress(0, f'0')




class CurrentWeightAHeight(ctk.CTkFrame):
    
    def __init__(self, master):
        super().__init__(master, fg_color=BLUE_GRAY, width=100, height=100)
        self.current_user = session_manager.get_current_user()
        self.current_date = self.master.date_selector.get_date()
        self.grid(row=6, column =0, sticky='we',padx = 10, pady = 10)
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1,2,3,4,5,6), weight=5)
        
        self.create_widgets()
        self.place_widgets()

    def create_widgets(self):
        current_age_height = self.current_user.current_athlete_record()
        current_height = self.current_user.inches_to_ftinch(current_age_height[4])
        weight = self.current_user.current_daily_record(self.current_date)[16]
        formated_height = f"{current_height["feet"]}\'{current_height["inches"]}\'\'"
        self.age = ctk.CTkLabel(self, text=f'Age: {current_age_height[3]}', font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')
        self.height = ctk.CTkLabel(self, text= f'Height: {formated_height}', font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')
        self.weight = ctk.CTkLabel(self, text= f'Weight: {weight}', font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')


    def place_widgets(self):
        self.age.grid(row=0, column=2, sticky='nsw')
        self.height.grid(row=0, column=3,sticky='nsw')
        self.weight.grid(row=0, column=4,sticky='nsw')

    def refresh_user(self):
        self.current_user = session_manager.get_current_user()
        current_age_height = self.current_user.current_athlete_record()
        current_height = self.current_user.inches_to_ftinch(current_age_height[4])
        weight = self.current_user.current_daily_record(self.current_date)[16]
        formated_height = f"{current_height["feet"]}\'{current_height["inches"]}\'\'"
        self.age.configure(text=f'Age: {current_age_height[3]}')
        self.height.configure(text=f'Height: {formated_height}')
        self.weight.configure(text=f'Weight: {weight}')



        
class CircleProgressBar(ctk.CTkFrame):
    def __init__(self, master, width=200, height=200, progress=0, fg_color='#50c878', bg_color='#9298a1', 
                 text='', text_color='white', font=None, label = ''):
        super().__init__(master, width=width, height=height, fg_color='transparent')

        self.label = ctk.CTkLabel(self, text=label, font=('Microsoft Yahei UI Light', 17, 'bold'), text_color='white')
        self.label.pack(pady=(0, 10))

        self.canvas = tk.Canvas(self, width=width, height=height, bg=master.cget('fg_color'), highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)

        self.width = width
        self.height = height
        self.fg_color = fg_color
        self.bg_color = bg_color

        self.progress = progress
        self.start_angle = 90
        self.thickness = 12

        self.draw_background()
        self.draw_progress()

        self.label = self.canvas.create_text(width/2, height/2, text=text, fill=text_color, font=font)

    def draw_background(self):
        self.canvas.create_oval(self.thickness, self.thickness, 
                                self.width - self.thickness, self.height - self.thickness, 
                                outline=self.bg_color, width=self.thickness, fill=self.canvas['bg'])
        
    def draw_progress(self):
        angle = 360 * (self.progress / 100)
        rad = math.radians(angle)
        if self.progress >= 100:
            self.canvas.create_oval(self.thickness, self.thickness, 
                                    self.width - self.thickness, self.height - self.thickness, 
                                    outline=self.fg_color, width=self.thickness)
        else:
            self.canvas.create_arc(self.thickness, self.thickness, 
                                   self.width - self.thickness, self.height - self.thickness, 
                                   start=self.start_angle, extent=angle, 
                                   outline=self.fg_color, width=self.thickness, style='arc')
            
    def set_progress(self, progress, text=''):
        self.progress = progress
        self.canvas.delete('all')
        self.draw_background()
        self.draw_progress()
        self.label = self.canvas.create_text(self.width/2, self.height/2, text=text, fill='white', font=('Microsoft Yahei UI Light', 15, 'bold'))



    
        
       


    

