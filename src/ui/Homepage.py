import customtkinter as ctk
from ..utils.constant import BLUE_GRAY
from .HomeFrames import DayNumbers, CurrentWeightAHeight
from ..utils.session_manager import session_manager
from tkcalendar import DateEntry, Calendar



class Home(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,fg_color=BLUE_GRAY, corner_radius=0)
        self.master = master
        self.rowconfigure((0,1,2,3,4,5,6,7), weight=1,uniform='a')
        self.columnconfigure(0, weight=1)


        self.date_selector = DateEntry(self,width = 18,height=13, background = BLUE_GRAY, 
                                       foreground = 'white',borderwidth = 2, font = ('Microsoft Yahei UI Light', 13, 'bold'),
                                       date_pattern = 'yyyy-mm-dd')
        
        self.date_selector.state(('disabled',))

        self.date_selector.grid(row=0, column = 0, sticky ='ns', pady =10)

        

        self.select_button = ctk.CTkButton(self, text='Select', command=self.update_for_selected_date)

        self.edit_button = ctk.CTkButton(self, text='Edit', command=self.edit_to_update)

        self.edit_button.grid(row=0, column = 0, sticky ='nse', padx=20, pady=10)

        self.current_user = session_manager.get_current_user()
        # name label
        self.namelabel = ctk.CTkLabel(self,font=('Microsoft Yahei UI Light', 40, 'bold'),bg_color='white',
                                      fg_color=BLUE_GRAY, text_color='white', text= self.current_user.username)
        self.namelabel.grid(row = 1, column=0, sticky='nw',padx =20, pady=15)

        #other
        self.day_numbers = DayNumbers(self)

        #age height and weight
        self.current_waH = CurrentWeightAHeight(self)

    def show(self):
        self.grid(row=0,column=1,sticky='wnse',columnspan=2)

    def hide(self):
        self.grid_forget() 


    def update_for_selected_date(self):
        selected_date = self.date_selector.get_date()
        self.select_button.grid_forget()
        self.edit_button.grid(row=0, column = 0, sticky ='nse', padx=20, pady=10)
        self.date_selector.state(('disabled',))
        self.master.refresh_all_frames(selected_date)
    

    def refresh_user(self, selected_date = None):
        if selected_date is None:
            selected_date = self.date_selector.get_date()

        self.current_user = session_manager.get_current_user()
        self.namelabel.configure(text= self.current_user.username)

        self.day_numbers.refresh_user(selected_date)
        self.current_waH.refresh_user()
        self.master.log.refresh_user(selected_date)
       

    def edit_to_update(self):
        self.date_selector.state(('!disabled',))
        self.edit_button.grid_forget()
        self.select_button.grid(row = 0, column = 0, sticky ='nse', padx =20, pady=10)

    
    