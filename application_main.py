import customtkinter as ctk
from themes import BLUE_GRAY
from PIL import Image

class Homepage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,fg_color='red', height=900, width=500)
        self.back_button = ctk.CTkButton(master=self, text='Log out', height=10, width=10)
        self.back_button.grid(row=0,column=0, padx=20, pady=20)
        

