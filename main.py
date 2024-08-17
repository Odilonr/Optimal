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
from src.utils.constant import BLUE_GRAY, TITLE_BAR_COLOR, BLUE_GRAY_TEST



class App(ctk.CTk):
     current_user = None

     def __init__(self):
          super().__init__(fg_color=BLUE_GRAY)
          self.title('')
          try:
               self.iconbitmap('the_icon.ico')
          except:
               pass
          self.geometry('925x500+300+200')
          self.resizable(False,False)
          self.change_title_bar_color()

          self.signin_frame = Signin(master=self)
          self.signup_frame = Signup(master=self)
          self.signin_frame.show()
          self.signin_frame.signin_button.configure(command=self.signin_approval)
          
          #configurations           
          self.toplevel_window = None

    
     def open_toplevel(self):
         if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
              self.toplevel_window = TopLevelWindow(master=self)
              self.grab_set()
              self.withdraw()
         else:
              self.toplevel_window.focus()

     def signin_approval(self):
        user_name = self.signin_frame.user_name.get().lower()
        password = self.signin_frame.password.get()
        
        database.open(db_name='health_tracker.db')

        gymbro = database.get_athlete(username=user_name, password=password)

        if gymbro:
           session_manager.login(gymbro)
           self.open_toplevel()
        elif user_name == '' or password == '':
            CTkMessagebox(self, title='Error',
                            message='Please fill both',icon ='cancel',text_color='white')
        else:
            CTkMessagebox(self, title='Error',
                            message='Wrong credentials',icon ='cancel',text_color='white')
        
     def change_title_bar_color(self):
      try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR =  TITLE_BAR_COLOR  
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
      except:
            pass


if __name__ == '__main__':
     app = App()
     app.mainloop()