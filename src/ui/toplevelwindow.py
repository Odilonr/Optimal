import customtkinter as ctk
from PIL import Image
from ..utils.constant import TITLE_BAR_COLOR, BLUE_GRAY_TEST,BLUE_GRAY
try:
	from ctypes import windll, byref, sizeof, c_int
except:
	pass
from .Homepage import Home
from .FoodLog import Log
from .ProfilePage import Profile
from ..utils.session_manager import session_manager


class TopLevelWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master, fg_color=BLUE_GRAY)
        self.title = 'Main'

        try:
               self.iconbitmap('the_icon.ico')
        except:
            pass
    
        
        self.desired_width = 1020
        self.desired_height = 500
        
        self.geometry(f'{self.desired_width}x{self.desired_height}')
        self.resizable(False, False)
        self.minsize(self.desired_width, self.desired_height)
        self.maxsize(self.desired_width, self.desired_height)
        
        if self.winfo_toplevel().wm_overrideredirect():
            self.overrideredirect(True)
        
        self.update_idletasks()
        
        # Center the window
        self.center_window()
        
        # Bind focus events
        self.bind("<FocusIn>", self.on_focus)
        self.bind("<FocusOut>", self.on_focus)
        
        # Start size check
        self.check_size()

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=30)
        self.rowconfigure(0,weight=1)
        # Rest of your initialization code...

        # widgets
        self.home = Home(self)
        self.menu = Menu(self)
        self.log = Log(self)
        self.profile = Profile(self)

      

        self.frames = {
                        Home: self.home,
                        Log: self.log,
                        Profile: self.profile
                        }
        
        self.current_frame = Home
        
        self.switch(Home)

        self.change_title_bar_color()

    def on_closing(self):
        """Handle the window close event."""
        self.logout()

    def logout(self):
        """Perform logout actions."""
        session_manager.logout()
        self.destroy()  # Close the TopLevelWindow
        self.master.deiconify()


    def refresh_all_frames(self, selected_date = None): 
        if selected_date is None:
             selected_date = self.home.date_selector.get_date()
        for frame in self.frames.values():
              if hasattr(frame, 'refresh_user'):
                   frame.refresh_user(selected_date)


    def switch(self, frame_class):
        self.current_frame = frame_class
        for frame in self.frames.values():
             frame.hide()
        self.frames[frame_class].show()
        self.refresh_all_frames()



    def change_title_bar_color(self):
      try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR =  TITLE_BAR_COLOR  
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
      except:
            pass
      
    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.desired_width) // 2
        y = (screen_height - self.desired_height) // 2
        self.geometry(f'{self.desired_width}x{self.desired_height}+{x}+{y}')

    def on_focus(self, event):
        self.center_window()
        self.update_idletasks()

    def check_size(self):
        current_width = self.winfo_width()
        current_height = self.winfo_height()
        if current_width != self.desired_width or current_height != self.desired_height:
            self.center_window()
        self.after(100, self.check_size)
      

class Menu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=BLUE_GRAY_TEST,width=50,corner_radius=10)
        self.master = master
        self.create_widgets()
        self.create_layout()
        self.show()

    def show(self):
        self.grid(row=0, column=0, sticky='wnse',columnspan=1)

    def hide(self):
        self.grid_forget()
   
    def create_widgets(self):
        self.home_icon = ctk.CTkImage(light_image=Image.open("src/assets/images/home_icon.png"),
                                  dark_image=Image.open("src/assets/images/home_icon.png"),
                                  size=(20, 20))
        self.log_icon = ctk.CTkImage(light_image=Image.open("src/assets/images/loggin_icon.png"),
                                  dark_image=Image.open("src/assets/images/loggin_icon.png"),
                                  size=(20, 20))
        self.profile_icon = ctk.CTkImage(light_image=Image.open("src/assets/images/profile_icon.png"),
                                  dark_image=Image.open("src/assets/images/profile_icon.png"),
                                  size=(20, 20))
        self.logout_icon = ctk.CTkImage(light_image=Image.open("src/assets/images/logout_icon.png"),
                                  dark_image=Image.open("src/assets/images/logout_icon.png"),
                                  size=(20, 20))
        
        font_menu = ctk.CTkFont(family='Microsoft Yahei UI Light', size=20, weight='bold')
        font_menu_elements = ctk.CTkFont(family='Microsoft Yahei UI Light', size=15, weight='bold')
        self.menu_label = ctk.CTkLabel(self,corner_radius=0, text='Menu', fg_color=BLUE_GRAY_TEST, font=font_menu,
                                       text_color='white')
        self.home_button = ctk.CTkButton(self,text='Home',fg_color=BLUE_GRAY_TEST,image=self.home_icon, font=font_menu_elements, 
                                         text_color='White',anchor='w', command=self.home)
        self.logg_button = ctk.CTkButton(self,text='Logging',fg_color=BLUE_GRAY_TEST,image=self.log_icon,font=font_menu_elements, 
                                         text_color='white',anchor='w',command=self.log)
        self.profile_button = ctk.CTkButton(self, text='Profile',fg_color=BLUE_GRAY_TEST,image=self.profile_icon,font=font_menu_elements, 
                                            text_color='white',anchor='w', command=self.profile)
        self.logout_button = ctk.CTkButton(self,text='Logout', fg_color=BLUE_GRAY_TEST,image=self.logout_icon, font=font_menu_elements, 
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
        self.master.logout()

    def home(self):
        self.master.home.refresh_user()
        self.master.switch(Home)


    def log(self):
        self.master.log.refresh_user()
        self.master.switch(Log)
        

    def profile(self):
        self.master.switch(Profile)

