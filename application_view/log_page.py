import customtkinter as ctk
from themes import BLUE_GRAY_TEST
class Log(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=BLUE_GRAY_TEST,corner_radius=0)
        font = ctk.CTkFont(family='Malgun Gothic', size=30, weight='bold')
        self.label = ctk.CTkLabel(self, text='I am Log page, and my color is green',font=font, fg_color='green')
        self.label.place(x=90,y=90)

    def show(self):
        self.grid(row=0,column=1,sticky='wnse',columnspan=2)
    
    def hide(self):
        self.grid_forget()