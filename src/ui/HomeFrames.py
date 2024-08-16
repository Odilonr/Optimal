import customtkinter as ctk
from ..utils.constant import BLUE_GRAY,BLUE_GRAY_TEST
import tkinter as tk
from ..utils.session_manager import session_manager
    
class DayNumbers(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=BLUE_GRAY, width=300, height=200)
        self.grid(row = 2, column =0 ,rowspan =4,sticky='nswe',padx = 10, pady = 10)
        self.columnconfigure((0,1,2), weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.create_widgets()


    def create_widgets(self):
        self.macros = Macros(self)

        self.canvas = tk.Canvas(self, width=180, height=180, bg=BLUE_GRAY,highlightthickness=0)
        self.canvas.grid(row=0, column=0)
        self.progress_bar = CircleProgressBar(self.canvas, 0,0,180,180,10)

        self.canvas_2 = tk.Canvas(self, width=180, height=180,bg=BLUE_GRAY,highlightthickness=0)
        self.canvas_2.grid(row=0, column=1)
        self.progress_bar_2 = CircleProgressBar(self.canvas_2, 0,0,180,180,10)

        self.canvas_3 = tk.Canvas(self, width=180, height=180,bg=BLUE_GRAY,highlightthickness=0)
        self.canvas_3.grid(row=0, column=2)
        self.progress_bar_3 = CircleProgressBar(self.canvas_3, 0,0,180,180,10)


  
    
        

class Macros(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=BLUE_GRAY)
        self.grid(row = 0, column=3, sticky='nswe')
        self.columnconfigure((0,1),weight=1)
        self.rowconfigure((0,1,2,4,5), weight=1)

        current_user = session_manager.get_current_user()

        self.carbs = ctk.CTkLabel(self, text='Carbs', font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')
        self.carbs.grid(row = 0, column = 0, sticky='nw')
        self.carbs_goal = ctk.CTkLabel(self, text=f'{current_user.macros_goal['Carbs']} g', font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')
        self.carbs_goal.grid(row = 0, column =0, sticky= 'e')
        self.carbs_progress = ctk.CTkProgressBar(self, orientation='horizontal',width=300,height=20, progress_color='#50c878',corner_radius=0)
        self.carbs_progress.grid(row=1,column=0, sticky='w',pady=10)

        self.protein = ctk.CTkLabel(self, text='Protein', font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')
        self.protein.grid(row =2, column = 0, sticky='nw')
        self.protein_goal = ctk.CTkLabel(self, text=f'{current_user.macros_goal['Protein']} g', font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')
        self.protein_goal.grid(row = 2, column =0, sticky= 'e')
        self.protein_progress = ctk.CTkProgressBar(self, orientation='horizontal',width=300,height=20, progress_color='#50c878',corner_radius=0)
        self.protein_progress.grid(row=3,column=0,sticky='w',pady=10)

        self.fat = ctk.CTkLabel(self, text='Fat', font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')
        self.fat.grid(row =4, column = 0, sticky='nw')
        self.fat_goal = ctk.CTkLabel(self, text=f'{current_user.macros_goal['Fat']} g', font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')
        self.fat_goal.grid(row = 4, column =0, sticky= 'e')
        self.fat_progress = ctk.CTkProgressBar(self, orientation='horizontal',width=300,height=20, progress_color='#50c878',corner_radius=0)
        self.fat_progress.grid(row=5,column=0,sticky='w',pady=10)


class CurrentWeightAHeight(ctk.CTkFrame):
    
    def __init__(self, master, current_user):
        super().__init__(master, fg_color=BLUE_GRAY, width=100, height=100)
        self.current_user = current_user
        self.grid(row=6, column =0, sticky='we',padx = 10, pady = 10)
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1,2,3,4,5,6), weight=5)
        
        self.create_widgets()
        self.place_widgets()

    def create_widgets(self):
        self.age = ctk.CTkLabel(self, text=f'AGE: {self.current_user.age}', font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')
        self.height = ctk.CTkLabel(self, text= f'HEIGHT: {self.current_user.height}', font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')
        self.weight = ctk.CTkLabel(self, text= f'WEIGHT: {self.current_user.weight}', font=('Microsoft Yahei UI Light', 20, 'bold'), text_color='white')

    def place_widgets(self):
        self.age.grid(row=0, column=2, sticky='nsw')
        self.height.grid(row=0, column=3,sticky='nsw')
        self.weight.grid(row=0, column=4,sticky='nsw')


class CircleProgressBar(object):
    def __init__(self, canvas, x0, y0, x1, y1, width=2):
        self.canvas = canvas
        
        self.x0, self.y0, self.x1, self.y1 = x0+width, y0+width, x1-width, y1-width
        
        w2 = width / 2
        self.oval_id1 = self.canvas.create_oval(self.x0-w2, self.y0-w2,
                                                self.x1+w2, self.y1+w2,outline='#4e5869',
                                                fill='#4e5869')
        self.oval_id2 = self.canvas.create_oval(self.x0+w2, self.y0+w2,
                                                self.x1-w2, self.y1-w2,outline='#4e5869',
                                                fill=BLUE_GRAY)
       
       


    

