import customtkinter as ctk
from CTkMessagebox  import CTkMessagebox
try:
	from ctypes import windll, byref, sizeof, c_int
except:
	pass
from src.ui.authentitication import Signin, Signup
from src.ui.toplevelwindow import TopLevelWindow
from src.data.database_manager import database
from src.utils.session_manager import session_manager
from src.scheduler import start_scheduler, initialize_daily_records
from src.utils.constant import BLUE_GRAY, TITLE_BAR_COLOR



class App(ctk.CTk):
     current_user = None

     def __init__(self):
          super().__init__(fg_color=BLUE_GRAY)
          self.title('')
          try:
               self.iconbitmap('the_icon.ico')
          except:
               pass
          
          
          self.desired_width = 925
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
          

          self.change_title_bar_color()

          self.signin_frame = Signin(master=self)
          self.signup_frame = Signup(master=self)
          self.signin_frame.show()
          self.signin_frame.signin_button.configure(command=self.signin_approval)
          
          #configurations           
          self.toplevel_window = None


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

     def signin_approval(self):
        user_name = self.signin_frame.user_name.get().lower()
        password = self.signin_frame.password.get()
        
        database.open(db_name='health_tracker.db')

        gymbro = database.get_athlete(username=user_name, password=password)

        if gymbro:
           database.open(db_name='health_tracker.db')
           session_manager.login(gymbro)
           self.open_toplevel()
        elif user_name == '' or password == '':
            CTkMessagebox(self, title='Error',
                            message='Please fill both',icon ='cancel',text_color='white',
                            fg_color = '#2d3038',bg_color='black',cancel_button_color='white', title_color='white')
        else:
            CTkMessagebox(self, title='Error',
                            message='Wrong credentials',icon ='cancel',text_color='white',fg_color = '#2d3038',
                            bg_color='black',cancel_button_color='white', title_color='white')
        

     def change_title_bar_color(self):
          try:
               HWND = windll.user32.GetParent(self.winfo_id())
               DWMWA_ATTRIBUTE = 35
               COLOR =  TITLE_BAR_COLOR  
               windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
          except:
               pass

     

     def open_toplevel(self):
         if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
              self.toplevel_window = TopLevelWindow(master=self)
              self.grab_set()
              self.withdraw()
         else:
              self.toplevel_window.focus()


if __name__ == '__main__':
     initialize_daily_records()
     start_scheduler()
     app = App()
     app.mainloop()