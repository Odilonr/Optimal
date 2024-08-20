import customtkinter as ctk
from ..utils.constant import BLUE_GRAY
from ..utils.session_manager import session_manager
from ..data.database_manager import database
from CTkMessagebox  import CTkMessagebox
import tkinter


class Profile(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=BLUE_GRAY,corner_radius=0)
        self.master = master
        self.columnconfigure((0,1,3), weight=1)
        self.rowconfigure((0,1,2,3,4,5,6,7,8),weight=1)
        self.master = master
        self.font_title = ctk.CTkFont(family = 'Microsoft Yahei UI Light', size = 25, weight = 'bold')
        self.font_title_small = ctk.CTkFont(family = 'Microsoft Yahei UI Light', size = 15, weight = 'bold')
        self.font_fields = ctk.CTkFont(family = 'Microsoft Yahei UI', size = 13)
        self.current_user = session_manager.get_current_user()
        self.create_widgets()
        self.place_widgets()
        self.entry_tiles(['Username','Age','Height(ft,in)','Weight(lbs)','Activity','Phase'],
                         ['Calories','Carbs(g)','Protein(g)','Fat(g)','Steps','Sleep(hrs)'])
        
    def create_widgets(self):
        self.profile = ctk.CTkLabel(self,text = 'Profile', font=self.font_title, text_color= "#F2F2F2")

        self.username = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields,placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=self.current_user.username),
                                       state='disabled')
        
        
        self.age = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields,placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=self.current_user.age),
                                       state='disabled')
        
        current_height = self.current_user.inches_to_ftinch(self.current_user.height)
        
        self.height_feet_entry = ctk.CTkEntry(self, width=50, height=50, fg_color='white', text_color='black', 
                                         border_width=2,font=self.font_fields,placeholder_text='feet',
                                         placeholder_text_color='#050000',state='disabled',
                                         textvariable=tkinter.StringVar(value=current_height['feet']))
        
        self.height_inches_entry = ctk.CTkEntry(self, width=50, height=50, fg_color='white', text_color='black', 
                                         border_width=2,font=self.font_fields,placeholder_text='inches',
                                         placeholder_text_color='#050000',state='disabled',
                                         textvariable=tkinter.StringVar(value=current_height['inches']))
        

        self.weight = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields, placeholder_text='Weight',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=self.current_user.weight),
                                       state='disabled')
        
        self.activity = ctk.CTkOptionMenu(self, width=180, height=50,button_color='white', fg_color='white', 
                                          dropdown_fg_color='white', values=['Sedentary','Active','Moderate','Very Active'], text_color='black', 
                                          dropdown_text_color='black', button_hover_color='#e6f0ef',state='disabled')
        self.activity.set(self.current_user.activity)
        
        self.phase = ctk.CTkOptionMenu(self, width=180, height=50,button_color='white', fg_color='white', 
                                          dropdown_fg_color='white', values=['Cut', 'Bulk'], text_color='black', 
                                          dropdown_text_color='black', button_hover_color='#e6f0ef',state='disabled')
        self.phase.set(self.current_user.phase)

        self.goals = ctk.CTkLabel(self,text = 'Daily Goals', font=self.font_title, text_color= "#F2F2F2")

        self.calorie_goal = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields,placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=self.current_user.calorie_goal),
                                       state='disabled')
        
        
        self.carb_goal = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields,placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=self.current_user.carb_goal),
                                       state='disabled')
        
        self.protein_goal = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields,placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=self.current_user.protein_goal),
                                       state='disabled')
        
        self.fat_goal = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields,placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=self.current_user.fat_goal),
                                       state='disabled')
        
        self.step_goal = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields,placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=self.current_user.step_goal),
                                       state='disabled')
        
        self.sleep_goal = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields,placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=self.current_user.sleep_goal),
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
        self.height_inches_entry.grid(row=3, column = 0, padx=190, sticky='ne')
        self.protein_goal.grid(row=3, column = 3, padx=100, sticky='ne')
        self.weight.grid(row=4, column=0, padx=100,sticky='nw')
        self.fat_goal.grid(row=4, column = 3, padx=100, sticky='ne')
        self.activity.grid(row=5,column=0, padx=100, sticky='nw')
        self.step_goal.grid(row=5, column = 3, padx=100, sticky='ne')
        self.phase.grid(row=6, column=0, padx=100, sticky='nw')
        self.sleep_goal.grid(row=6, column = 3, padx=100, sticky='ne')
        self.edit.grid(row=8, column=0, padx=10, sticky='e')

    def edit_command(self):
        self.edit.grid_forget()
        self.save.grid(row=8, column=0, padx=10, sticky='e')

        attributes = [self.username, self.age, self.height_feet_entry,
                             self.height_inches_entry,self.weight, self.activity, self.phase,
                             self.calorie_goal,self.calorie_goal,self.carb_goal,
                             self.protein_goal,self.fat_goal,self.step_goal,self.sleep_goal]

        for attribute in attributes:
            attribute.configure(state='normal')

    def save_command(self):
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
        activity_num = database.determine_activity(activity)
        maintenance_calories = database.maintenace_calories(activity=activity_num,age=age,
                                                          gender=self.current_user.gender,height=height,weight=weight)

        step_goal = int(self.step_goal.get())
        sleep_goal = int(self.sleep_goal.get())
        calorie_goal = float(self.calorie_goal.get())
        protein_goal = int(self.protein_goal.get())
        carb_goal = int(self.carb_goal.get())
        fat_goal = int(self.fat_goal.get())

        if phase == 'Cut':
            calorie_difference = maintenance_calories - calorie_goal
        else:
            calorie_difference = maintenance_calories + calorie_goal
            
        self.current_user.update_main(
            username=username,
            age=age,
            height=height,
            weight=weight,
            activity=activity,
            phase=phase,
            calorie_difference=calorie_difference,
            step_goal=step_goal,
            sleep_goal=sleep_goal,
            calorie_goal=calorie_goal,
            protein_goal=protein_goal,
            carb_goal=carb_goal,
            fat_goal=fat_goal   
        )

        updated_user = database.get_athlete_edited(username=username,age=age)
        session_manager.update_current_user(updated_user)

        self.master.refresh_all_frames()
        
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

    
    def show(self):
        self.grid(row=0,column=1,sticky='wnse',columnspan=2)
    
    def hide(self):
        self.grid_forget()



