import customtkinter as ctk
from CTkMessagebox  import CTkMessagebox
from tkinter import BOTH
try:
	from ctypes import windll, byref, sizeof, c_int
except:
	pass
from themes import BLUE_GRAY,TITLE_BAR_COLOR,BLUE_GRAY_TEST
from application_view.authentitication import Signin, Signup
from application_view.top_level import TopLevelWindow


dummy_data = {
      'username':'odilon',
      'password':'1234',
      'age': 23,
      'weight': 210,
      'height':75,
      'calories':1600,
      'steps':9500,
      'sleep':8
}

class App(ctk.CTk):
    def __init__(self):
          super().__init__(fg_color=BLUE_GRAY_TEST)
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
          ##self.signin_frame.show()
          

          #configurations
          ##self.signin_frame.signin_button.configure(command=self.signin_approval)  
           
          self.toplevel_window = None

          self.open_toplevel()


    def signin_approval(self):
         user_name = self.signin_frame.user_name.get().lower()
         password = self.signin_frame.password.get()
         if user_name == dummy_data['username'] and password == dummy_data['password']:
               self.open_toplevel()
         elif user_name == '' or password == '':
              CTkMessagebox(self, title='Error', fg_color=BLUE_GRAY, bg_color='#030426',
                            message='You need to enter both both the username and password',icon ='cancel')
              
         elif user_name != dummy_data['username'] or user_name != dummy_data['password']:
              CTkMessagebox(self, title='Error', fg_color=BLUE_GRAY, bg_color='#030426',
                            message='Wrong Username or Password, try again',icon ='cancel')
              
    
    def open_toplevel(self):
         if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
              self.toplevel_window = TopLevelWindow(master=self)
              self.grab_set()
              self.withdraw()
         else:
              self.toplevel_window.focus()
        
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