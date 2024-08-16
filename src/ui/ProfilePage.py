import customtkinter as ctk
from ..utils.constant import BLUE_GRAY
from ..utils.session_manager import session_manager
import tkinter

class Profile(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=BLUE_GRAY,corner_radius=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0,1,2,3,4,5,6,7,8),weight=1)
        self.master = master
        self.font_title = ctk.CTkFont(family = 'Microsoft Yahei UI Light', size = 25, weight = 'bold')
        self.font_fields = ctk.CTkFont(family = 'Microsoft Yahei UI', size = 13)
        self.current_user = session_manager.get_current_user()
        self.create_widgets()
        self.place_widgets()
        
    def create_widgets(self):
        self.profile = ctk.CTkLabel(self,text = 'Profile', font=self.font_title, text_color= "#F2F2F2")

        self.username = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields,placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=f'{self.current_user.username} years'),
                                       state='disabled')
        
        
        self.age = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields,placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=f'{self.current_user.age} years'),
                                       state='disabled')
        
        self.height = ctk.CTkOptionMenu(self, width=90, height=50,button_color='white', fg_color='white', 
                                          dropdown_fg_color='white', values=['1','2','3'], text_color='black', 
                                          dropdown_text_color='black', button_hover_color='#e6f0ef',state='disabled')
        self.height.set(self.current_user.height)
        
        
        self.weight = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=self.font_fields, placeholder_text='Weight',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black', textvariable=tkinter.StringVar(value=f'{self.current_user.weight} pounds'),
                                       state='disabled')
        
        self.activity = ctk.CTkOptionMenu(self, width=180, height=50,button_color='white', fg_color='white', 
                                          dropdown_fg_color='white', values=['Sendetary', 'Active'], text_color='black', 
                                          dropdown_text_color='black', button_hover_color='#e6f0ef',state='disabled')
        self.activity.set(self.current_user.activity)
        
        self.phase = ctk.CTkOptionMenu(self, width=180, height=50,button_color='white', fg_color='white', 
                                          dropdown_fg_color='white', values=['Cutting', 'Bulking'], text_color='black', 
                                          dropdown_text_color='black', button_hover_color='#e6f0ef',state='disabled')
        self.phase.set(self.current_user.phase)
        
        self.edit = ctk.CTkButton(self, text='Edit',width=240, height=50,border_width=1, border_color='white',fg_color=BLUE_GRAY,
                                            text_color='white',hover_color='#0c1545', font=self.font_title, corner_radius=0,
                                            )
        
        self.save = ctk.CTkButton(self, text='Save',width=240, height=50,border_width=1, border_color='white',fg_color=BLUE_GRAY,
                                            text_color='white',hover_color='#0c1545', font=self.font_title, corner_radius=0,
                                            )
        
        
        
    def place_widgets(self):
        self.profile.grid(row=0, column=0,padx = 20,pady=10, sticky='nw')
        self.username.grid(row = 1, column =0, padx=20,sticky='nw')
        self.age.grid(row=2, column=0, padx=20,sticky='nw')
        self.height.grid(row=3, column =0, padx=20, sticky='nw')
        self.weight.grid(row=4, column=0, padx=20,sticky='nw')
        self.activity.grid(row=5,column=0, padx=20, sticky='nw')
        self.phase.grid(row=6, column=0, padx=20, sticky='nw')
        self.edit.grid(row=8, column=0, padx=20, sticky='nw')


    def edit_command(self):
        self.edit.grid_forget()
        self.save.grid(row=8, column=0, padx=20, sticky='nw')

        attributes_states = [self.username, self.age, self.height, self.weight, self.activity, self.phase]

        for attribute in attributes_states:
            attribute.configure(state='normal')

        new_attributes = {
                            'username':self.username.get(),
                            'age':self.age.get(),
                            'height':self.height.get(),
                            'weight':self.weight.get(),
                            'activity':self.activity.get(),
                            'phase':self.phase.get()
                         }

    def save_command(self):
        pass



    def show(self):
        self.grid(row=0,column=1,sticky='wnse',columnspan=2)
    
    def hide(self):
        self.grid_forget()



