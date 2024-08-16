import customtkinter as ctk
from ..utils.constant import BLUE_GRAY_TEST,BLUE_GRAY
from .HomeFrames import DayNumbers, CurrentWeightAHeight
from ..utils.session_manager import session_manager


class Home(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,fg_color=BLUE_GRAY, corner_radius=0)
        self.rowconfigure((0,1,2,3,4,5,6,7), weight=1,uniform='a')
        self.columnconfigure(0, weight=1)

        # date
        ##self.date = ttk.DateEntry()
        ##self.date.grid(row=0, column = 0)
        self.date = ctk.CTkOptionMenu(self, values=['06/10/2001', '06/09/2001'],fg_color='white', text_color='black',
                                      bg_color='white',dropdown_fg_color='white', dropdown_text_color='black',
                                      button_color='white')
        self.date.grid(row=0, column = 0, sticky='n')

        current_user = session_manager.get_current_user()
        # name label
        self.namelabel = ctk.CTkLabel(self, text=current_user.username, font=('Microsoft Yahei UI Light', 40, 'bold'),bg_color='white',
                                      fg_color=BLUE_GRAY, text_color='white')
        self.namelabel.grid(row = 1, column=0, sticky='nw',padx=20)

        #other
        DayNumbers(self)

        #age height and weight
        CurrentWeightAHeight(self,current_user=current_user)     

    def show(self):
        self.grid(row=0,column=1,sticky='wnse',columnspan=2)

    def hide(self):
        self.grid_forget() 