import customtkinter as ctk
from themes import BLUE_GRAY_TEST

class DayNumbers(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=BLUE_GRAY_TEST, width=300, height=200)
        self.grid(row = 2, column =0 ,rowspan =4,sticky='nswe',padx = 10, pady = 10)
        self.columnconfigure((0,1,2), weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.macros = Macros(self)
        self.create_widgets()
        self.place_widgets()


    def create_widgets(self):
       
        self.calories = ctk.CTkFrame(self, fg_color='blue')
        self.steps = ctk.CTkFrame(self, fg_color='blue')
        self.sleep = ctk.CTkFrame(self, fg_color='blue')
        #self.macros = Macros(self)

    def place_widgets(self):
        self.calories.grid(row = 0, column=0)
        self.steps.grid(row = 0, column=1)
        self.sleep.grid(row = 0, column=2)
        ##self.macros.grid(row = 0, column=2, sticky='nswe')

class Macros(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=BLUE_GRAY_TEST)
        self.grid(row = 0, column=3, sticky='nswe')
        self.columnconfigure(0,weight=1)
        self.rowconfigure((0,1,2), weight=1)

        self.carbs = ctk.CTkLabel(self, text='Carbs', font=('Microsoft Yahei UI Light', 20, 'bold'))
        self.carbs.grid(row =0, column = 0, sticky='nw')

        self.carbs_progress = ctk.CTkProgressBar(self, orientation='horizontal',width=200,height=20, progress_color='#50c878',corner_radius=0)
        self.carbs_progress.grid(row=0,column=0, sticky='w')

        self.protein = ctk.CTkLabel(self, text='Protein', font=('Microsoft Yahei UI Light', 20, 'bold'))
        self.protein.grid(row =1, column = 0, sticky='nw')

        self.protein_progress = ctk.CTkProgressBar(self, orientation='horizontal',width=200,height=20, progress_color='#50c878',corner_radius=0)
        self.protein_progress.grid(row=1,column=0,sticky='w')

        self.fat = ctk.CTkLabel(self, text='Fat', font=('Microsoft Yahei UI Light', 20, 'bold'))
        self.fat.grid(row =2, column = 0, sticky='nw')

        self.carbs_progress = ctk.CTkProgressBar(self, orientation='horizontal',width=200,height=20, progress_color='#50c878',corner_radius=0)
        self.carbs_progress.grid(row=2,column=0,sticky='w')



class CurrentWeightAHeight(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=BLUE_GRAY_TEST, width=100, height=100)
        self.grid(row=7, column =0, sticky='we',padx = 10, pady = 10)
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1,2,3,4,5,6), weight=5)
        self.create_widgets()
        self.place_widgets()

    def create_widgets(self):
        self.age = ctk.CTkLabel(self, text='A: 23', font=('Microsoft Yahei UI Light', 20, 'bold'))
        self.height = ctk.CTkLabel(self, text="H: 6'2",font=('Microsoft Yahei UI Light', 20, 'bold'))
        self.weight = ctk.CTkLabel(self, text= "W: 215",font=('Microsoft Yahei UI Light', 20, 'bold'))

    def place_widgets(self):
        self.age.grid(row=0, column=2, sticky='nsw')
        self.height.grid(row=0, column=3,sticky='nsw')
        self.weight.grid(row=0, column=4,sticky='nsw')