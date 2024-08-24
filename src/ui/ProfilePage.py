import customtkinter as ctk
from ..utils.constant import BLUE_GRAY
from ..utils.session_manager import session_manager
from ..data.database_manager import database
from CTkMessagebox  import CTkMessagebox
from ..data.helper_functions import determine_activity, macros_goal, maintenace_calories
import tkinter
from datetime import date


class Profile(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=BLUE_GRAY,corner_radius=0)
        self.master = master
        self.current_date = self.master.home.date_selector.get_date()
        self.current_user = session_manager.get_current_user()
        self.current_records_athlete = self.current_user.current_athlete_record()
        self.current_records_daily = self.current_user.current_daily_record(self.current_date)
        self.columnconfigure((0,1,3), weight=1)
        self.rowconfigure((0,1,2,3,4,5,6,7,8),weight=1)
        self.master = master
        self.font_title = ctk.CTkFont(family = 'Microsoft Yahei UI Light', size = 25, weight = 'bold')
        self.font_title_small = ctk.CTkFont(family = 'Microsoft Yahei UI Light', size = 13, weight = 'bold')
        self.font_fields = ctk.CTkFont(family = 'Microsoft Yahei UI', size = 13)
        self.current_user = session_manager.get_current_user()
        self.create_widgets()
        self.place_widgets()
        self.entry_tiles(['Username','Age','Height(ft,in)','Weight(lbs)','Activity','Phase'],
                         ['Calories','Carbs(g)','Protein(g)','Fat(g)','Steps','Sleep(hrs)'])
        
    def create_widgets(self):
        self.profile = ctk.CTkLabel(self,text = 'Profile', font=self.font_title, text_color= "#F2F2F2")

        current_username = self.current_records_athlete[1]
        self.username = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields,placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=current_username),
                                       state='disabled')
        
        current_age = self.current_records_athlete[3]
        self.age = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields,placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=current_age),
                                       state='disabled')
        
        current_height = self.current_user.inches_to_ftinch(self.current_records_athlete[4])

        
        self.height_feet_entry = ctk.CTkEntry(self, width=50, height=50, fg_color='white', text_color='black', 
                                         border_width=2,font=self.font_fields,placeholder_text='feet',
                                         placeholder_text_color='#050000',state='disabled',
                                         textvariable=tkinter.StringVar(value=current_height['feet']))
        
        self.height_inches_entry = ctk.CTkEntry(self, width=50, height=50, fg_color='white', text_color='black', 
                                         border_width=2,font=self.font_fields,placeholder_text='inches',
                                         placeholder_text_color='#050000',state='disabled',
                                         textvariable=tkinter.StringVar(value=current_height['inches']))
        
        current_weight = self.current_records_daily[16]
        self.weight = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields, placeholder_text='Weight',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=current_weight),
                                       state='disabled')
        
        current_activity = self.current_records_daily[17]
        self.activity = ctk.CTkOptionMenu(self, width=180, height=50,button_color='white', fg_color='white', 
                                          dropdown_fg_color='white', values=['Sedentary','Active','Moderate','Very Active'], text_color='black', 
                                          dropdown_text_color='black', button_hover_color='#e6f0ef',state='disabled')
        self.activity.set(current_activity)
        
        current_phase = self.current_records_daily[18]
        self.phase = ctk.CTkOptionMenu(self, width=180, height=50,button_color='white', fg_color='white', 
                                          dropdown_fg_color='white', values=['Cut', 'Bulk'], text_color='black', 
                                          dropdown_text_color='black', button_hover_color='#e6f0ef',state='disabled')
        self.phase.set(current_phase)

        self.goals = ctk.CTkLabel(self,text = 'Daily Goals', font=self.font_title, text_color= "#F2F2F2")

        current_calgoal = self.current_records_daily[3]
        self.calorie_goal = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields,placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=current_calgoal),
                                       state='disabled')
        
        
        current_carbgoal = self.current_records_daily[11]
        self.carb_goal = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields,placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=current_carbgoal),
                                       state='disabled')
        

        current_protgoal = self.current_records_daily[13]
        self.protein_goal = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields,placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=current_protgoal),
                                       state='disabled')
        
        current_fatgoal = self.current_records_daily[15]
        self.fat_goal = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields,placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=current_fatgoal),
                                       state='disabled')
        
        current_stepgoal = self.current_records_daily[7]
        self.step_goal = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields,placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=current_stepgoal),
                                       state='disabled')
        
        current_sleepgoal = self.current_records_daily[9]
        self.sleep_goal = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields,placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=current_sleepgoal),
                                       state='disabled')
        

        self.edit = ctk.CTkButton(self, text='Edit',width=200, height=50,border_width=1, border_color='white',fg_color=BLUE_GRAY,
                                            text_color='white',hover_color='#0c1545', font=self.font_title, corner_radius=0,
                                            command=self.edit_command)
        
        self.save = ctk.CTkButton(self, text='Save',width=200, height=50,border_width=1, border_color='white',fg_color=BLUE_GRAY,
                                            text_color='white',hover_color='#0c1545', font=self.font_title, corner_radius=0,
                                            command=self.save_command)
        
        
    def place_widgets(self):
        self.profile.grid(row=0, column=0,padx = 10,pady=10, sticky='nw')
        self.goals.grid(row = 0, column=3, padx =10, pady= 10, sticky='nw')
        self.username.grid(row = 1, column =0, padx=100,sticky='nw')
        self.calorie_goal.grid(row=1, column = 3, padx=100, sticky='ne')
        self.age.grid(row=2, column=0, padx=100,sticky='nw')
        self.carb_goal.grid(row=2, column = 3, padx=100, sticky='ne')
        self.height_feet_entry.grid(row=3, column =0, padx=100, sticky='nw')
        self.height_inches_entry.grid(row=3, column = 0, padx=200, sticky='ne')
        self.protein_goal.grid(row=3, column = 3, padx=100, sticky='ne')
        self.weight.grid(row=4, column=0, padx=100,sticky='nw')
        self.fat_goal.grid(row=4, column = 3, padx=100, sticky='ne')
        self.activity.grid(row=5,column=0, padx=100, sticky='nw')
        self.step_goal.grid(row=5, column = 3, padx=100, sticky='ne')
        self.phase.grid(row=6, column=0, padx=100, sticky='nw')
        self.sleep_goal.grid(row=6, column = 3, padx=100, sticky='ne')
        self.edit.grid(row=8, column=0, padx=10, sticky='e')


    def edit_command(self):
        to_day = date.today()
        
        attributes = [self.username, self.age, self.height_feet_entry,
                             self.height_inches_entry,self.weight, self.activity, self.phase,
                             self.calorie_goal,self.calorie_goal,self.carb_goal,
                             self.protein_goal,self.fat_goal,self.step_goal,self.sleep_goal]

        if self.master.home.date_selector.get_date() == to_day:
            print(to_day)
            print(self.current_date)
            self.edit.grid_forget()
            self.save.grid(row=8, column=0, padx=10, sticky='e')
            for attribute in attributes:
                attribute.configure(state='normal')
        else:
            return
        
      


    def save_command(self):
        self.current_records_daily = self.current_user.current_daily_record(self.current_date)
        self.current_records_athlete = self.current_user.current_athlete_record() 
        attributes_entries = [self.username, self.age, self.height_feet_entry,
                             self.height_inches_entry,self.weight, self.activity, self.phase,
                             self.calorie_goal,self.calorie_goal,self.protein_goal,self.fat_goal,
                             self.step_goal,self.sleep_goal]
        for attribute in attributes_entries:
            if attribute.get() == '':
                CTkMessagebox(self, title='Error',
                            message='Cannot leave empty spots',icon ='cancel',text_color='white')
                return
            
        username = self.username.get().lower()
        age = int(self.age.get())
        feet = int(self.height_feet_entry.get())
        inches = int(self.height_inches_entry.get())
        height = self.current_user.ftinch_to_inches(feet, inches)
        weight = float(self.weight.get())
        activity = self.activity.get()
        phase = self.phase.get()
        activity_num = determine_activity(activity)
        maintenance_calories = maintenace_calories(gender=self.current_records_athlete[5], 
                                                   weight=weight, height=height, age=age, activity=activity_num)
            
        old_caloriegoal = self.current_records_daily[3]

        if old_caloriegoal != int(self.calorie_goal.get()):
            calorie_goal = int(self.calorie_goal.get())
        else:
            if phase == 'Cut':
                calorie_goal = int(maintenance_calories) - 500
            else:
                calorie_goal = int(maintenance_calories) + 500

        new_macros = macros_goal(calorie_goal=calorie_goal, phase=phase)

        if (int(self.carb_goal.get()) == self.current_records_daily[11] and
             int(self.protein_goal.get()) == self.current_records_daily[13] and
             int(self.fat_goal.get()) == self.current_records_daily[15]):
            carb_goal = new_macros['carb_goal']
            protein_goal = new_macros['protein_goal']
            fat_goal = new_macros['fat_goal']
        else:
            carb_goal = self.carb_goal.get()
            protein_goal = self.protein_goal.get()
            fat_goal = self.fat_goal.get()

        step_goal = int(self.step_goal.get())
        sleep_goal = int(self.sleep_goal.get())

        self.current_user.update_main(
            username=username,
            age=age,
            height=height, 
        )
        
        password = self.current_records_athlete[2]
        athlete_id = self.current_records_athlete[0]
        updated_user = database.get_athlete(username=username,password=password)
        session_manager.update_current_user(updated_user)

        database.update_daily_record(athlete_id=athlete_id, date = self.current_date, 
                                     calorie_goal=calorie_goal,step_goal=step_goal, sleep_goal = sleep_goal, carb_goal = carb_goal,
                                     protein_goal= protein_goal,fat_goal = fat_goal, weight = weight, 
                                     activity = activity, phase=phase)
    
        current_daily_record = self.current_user.current_daily_record(self.current_date)
        new_remaining = current_daily_record[3] - current_daily_record[4]

        database.update_daily_record(athlete_id=athlete_id, date=self.current_date,
                                      calories_remaining = new_remaining)

        self.master.refresh_all_frames(self.current_date)
        
        for attribute in attributes_entries:
            attribute.configure(state='disabled')

        self.save.grid_forget()
        self.edit.grid(row=8, column=0, padx=10, sticky='e')

        CTkMessagebox(self, title='Success',
                            message='Update succesfully',icon ='check',text_color='white')
        

    def entry_tiles(self, left_titles, right_titles):
        for i, entry_one in enumerate(left_titles):
            title_one = ctk.CTkLabel(self,text = entry_one, font=self.font_title_small, text_color= "#F2F2F2")
            title_one.grid(row=i+1, column =0,padx=10,sticky='nw')

        for j , entry_two in enumerate(right_titles):
            title_two = ctk.CTkLabel(self,text = entry_two, font=self.font_title_small, text_color= "#F2F2F2")
            title_two.grid(row=j+1, column =3,padx=10,sticky='nw')

    def refresh_user(self, selected_date=None):
        if selected_date is None:
            selected_date = self.current_date
        current_athlete_record = self.current_user.current_athlete_record()
        current_daily_record = self.current_user.current_daily_record(selected_date)
        if current_daily_record:
            self.username.configure(textvariable = tkinter.StringVar(value=current_athlete_record[1]))
            self.age.configure(textvariable = tkinter.StringVar(value=current_athlete_record[3]))
            height = self.current_user.inches_to_ftinch(current_athlete_record[4])
            self.height_feet_entry.configure(textvariable = tkinter.StringVar(value=height['feet']))
            self.height_inches_entry.configure(textvariable = tkinter.StringVar(value=height['inches']))
            self.weight.configure(textvariable = tkinter.StringVar(value=current_daily_record[16]))
            self.activity.set(current_daily_record[17])
            self.phase.set(current_daily_record[18])
            self.calorie_goal.configure(textvariable = tkinter.StringVar(value=current_daily_record[3]))
            self.carb_goal.configure(textvariable = tkinter.StringVar(value=current_daily_record[11]))
            self.protein_goal.configure(textvariable = tkinter.StringVar(value=current_daily_record[13]))
            self.fat_goal.configure(textvariable = tkinter.StringVar(value=current_daily_record[15]))
            self.step_goal.configure(textvariable = tkinter.StringVar(value=current_daily_record[7]))
            self.sleep_goal.configure(textvariable = tkinter.StringVar(value=current_daily_record[9]))
        else:
            self.username.configure(textvariable = tkinter.StringVar(value=current_athlete_record[1]))
            self.age.configure(textvariable = tkinter.StringVar(value=current_athlete_record[3]))
            height = self.current_user.inches_to_ftinch(current_athlete_record[4])
            self.height_feet_entry.configure(textvariable = tkinter.StringVar(value=height['feet']))
            self.height_inches_entry.configure(textvariable = tkinter.StringVar(value=height['inches']))
            self.weight.configure(textvariable = tkinter.StringVar(value='None'))
            self.activity.set('Non')
            self.phase.set('None')
            self.calorie_goal.configure(textvariable = tkinter.StringVar(value='None'))
            self.carb_goal.configure(textvariable = tkinter.StringVar(value='None'))
            self.protein_goal.configure(textvariable = tkinter.StringVar(value='None'))
            self.fat_goal.configure(textvariable = tkinter.StringVar(value='None'))
            self.step_goal.configure(textvariable = tkinter.StringVar(value='None'))
            self.sleep_goal.configure(textvariable = tkinter.StringVar(value='None'))


    
    def show(self):
        self.grid(row=0,column=1,sticky='wnse',columnspan=2)
    
    def hide(self):
        self.grid_forget()



