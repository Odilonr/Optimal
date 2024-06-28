import customtkinter as ctk
from themes import BLUE_GRAY_TEST

class Profile(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=BLUE_GRAY_TEST,corner_radius=0)
        font = ctk.CTkFont(family='Malgun Gothic', size=30, weight='bold')
        self.label = ctk.CTkLabel(self, text='I am Profile page, and my color is pink',font=font, fg_color='pink')
        self.label.place(x=90,y=90)

    def show(self):
        self.grid(row=0,column=1,sticky='wnse',columnspan=2)
    
    def hide(self):
        self.grid_forget()