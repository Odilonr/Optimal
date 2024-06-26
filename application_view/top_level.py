import customtkinter as ctk
from PIL import Image
from themes import TITLE_BAR_COLOR, BLUE_GRAY_TEST
try:
	from ctypes import windll, byref, sizeof, c_int
except:
	pass
from .home_page import Home
from .log_page import Log
from .profile_page import Profile


class TopLevelWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master, fg_color=BLUE_GRAY_TEST)
        self.title = 'Main'
        try:
               self.iconbitmap('the_icon.ico')
        except:
            pass
        
        self.geometry('925x500+300+200')
        self.resizable(False,False)

        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=30)
        self.rowconfigure(0,weight=1)


        # widgets
        self.menu = Menu(self)
        self.home = Home(self)
        
        self.frames = {}
        for frame in (Home, Log, Profile):
            f = frame(self)
            f.show()
            self.frames[frame] = f
        self.switch(Home)

        self.change_title_bar_color()

    def switch(self, frame):
        self.frames[frame].tkraise()


    def change_title_bar_color(self):
      try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR =  TITLE_BAR_COLOR  
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
      except:
            pass


class Menu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='#00060f',width=50,corner_radius=10)
        self.master = master
        self.create_widgets()
        self.create_layout()
        self.show()

    def show(self):
        self.grid(row=0, column=0, sticky='wnse',columnspan=1)

    def hide(self):
        self.grid_forget()
   
    def create_widgets(self):
        self.home_icon = ctk.CTkImage(light_image=Image.open("images/home_icon.png"),
                                  dark_image=Image.open("images/home_icon.png"),
                                  size=(20, 20))
        self.log_icon = ctk.CTkImage(light_image=Image.open("images/loggin_icon.png"),
                                  dark_image=Image.open("images/loggin_icon.png"),
                                  size=(20, 20))
        self.profile_icon = ctk.CTkImage(light_image=Image.open("images/profile_icon.png"),
                                  dark_image=Image.open("images/profile_icon.png"),
                                  size=(20, 20))
        self.logout_icon = ctk.CTkImage(light_image=Image.open("images/logout_icon.png"),
                                  dark_image=Image.open("images/logout_icon.png"),
                                  size=(20, 20))
        
        font_menu = ctk.CTkFont(family='Microsoft Yahei UI Light', size=20, weight='bold')
        font_menu_elements = ctk.CTkFont(family='Microsoft Yahei UI Light', size=15, weight='bold')
        self.menu_label = ctk.CTkLabel(self,corner_radius=0, text='Menu', fg_color='#00060f', font=font_menu,
                                       )
        self.home_button = ctk.CTkButton(self,text='Home',fg_color='#00060f',image=self.home_icon, font=font_menu_elements, 
                                         text_color='White',anchor='w', command=self.home)
        self.logg_button = ctk.CTkButton(self,text='Logging',fg_color='#00060f',image=self.log_icon,font=font_menu_elements, 
                                         text_color='white',anchor='w',command=self.log)
        self.profile_button = ctk.CTkButton(self, text='Profile',fg_color='#00060f',image=self.profile_icon,font=font_menu_elements, 
                                            text_color='white',anchor='w', command=self.profile)
        self.logout_button = ctk.CTkButton(self,text='Logout', fg_color='#00060f',image=self.logout_icon, font=font_menu_elements, 
                                           text_color='white',anchor='w',command=self.logout)

    def create_layout(self):
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0,1,2,3,4,5,6,7,8,10), weight=1, uniform='a')
        self.menu_label.grid(row = 0, column=0, sticky='nswe')
        self.home_button.grid(row = 1, column = 0,sticky='nswe', columnspan=3)
        self.logg_button.grid(row = 2, column = 0, sticky='nswe')
        self.profile_button.grid(row = 3, column = 0, sticky='nswe')
        self.logout_button.grid(row =9, column = 0,  sticky = 'nswe')

    def logout(self):
        self.master.destroy()
        self.master.master.deiconify()

    def home(self):
        self.master.switch(Home)

    def log(self):
        self.master.switch(Log)

    def profile(self):
        self.master.switch(Profile)

