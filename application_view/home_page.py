import customtkinter as ctk
from themes import BLUE_GRAY_TEST
from .home_frames import DayNumbers, CurrentWeightAHeight

class Home(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,fg_color=BLUE_GRAY_TEST, corner_radius=0)
        self.rowconfigure((0,1,2,3,4,5,6,7), weight=1,uniform='a')
        self.columnconfigure(0, weight=1)

        # date
        ##self.date = ttk.DateEntry()
        ##self.date.grid(row=0, column = 0)
        self.date = ctk.CTkOptionMenu(self, values=['06/10/2001', '06/09/2001'],fg_color='white', text_color='black')
        self.date.grid(row=0, column = 0, sticky='n')

        # name label
        self.namelabel = ctk.CTkLabel(self, text='Odilon', font=('Microsoft Yahei UI Light', 40, 'bold'),
                                      fg_color=BLUE_GRAY_TEST)
        self.namelabel.grid(row =1, column=0, sticky='n')

        #other
        DayNumbers(self)

        #age height and weight
        CurrentWeightAHeight(self)     

    def show(self):
        self.grid(row=0,column=1,sticky='wnse',columnspan=2)

    def hide(self):
        self.grid_forget() 