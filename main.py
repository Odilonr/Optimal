import customtkinter as ctk
from tkinter import BOTH
try:
	from ctypes import windll, byref, sizeof, c_int
except:
	pass
from PIL import Image
from themes import BLUE_GRAY, BLUE_GRAY_HEX
from login import Signin, Signup
from application_main import Homepage


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
      super().__init__(fg_color=BLUE_GRAY)
      self.title('')
      try:
          self.iconbitmap('empty.ico')
      except:
        pass
      self.geometry('925x500+300+200')
      self.resizable(False,False)
      self.change_title_bar_color()

      self.signin_frame = Signin(master=self)
      self.signup_frame = Signup(master=self)
      self.homepage = Homepage(master=self)

      self.signin_frame.grid(row = 0, columns = 2, padx=52, pady=60)

      self.signin_frame.signup_button.configure(command=self.switch_from_login_to_signup)
      self.signup_frame.signup_button.configure(command=self.switch_from_signup_to_login)

      self.signin_frame.signin_button.configure(command = self.signin_approval)
      
      self.homepage.back_button.configure(command = self.log_out)

      self.mainloop()
  
    def switch_from_login_to_signup(self):
         self.signin_frame.forget
         self.signup_frame.tkraise()
         self.signup_frame.grid(row = 0, columns = 2, padx=52, pady=60)
         

    def switch_from_signup_to_login(self):
         self.signup_frame.forget
         self.signin_frame.tkraise()
         self.signin_frame.grid(row = 0, columns = 2, padx=52, pady=60)

    def signin_approval(self):
         user_name = self.signin_frame.user_name.get().lower()
         password = self.signin_frame.password.get()
         if user_name == dummy_data['username'] and password == dummy_data['password']:
              self.signin_frame.grid_forget()
              self.signup_frame.grid_forget()
              self.homepage.tkraise()
              self.homepage.grid(row = 3, columns = 2, sticky = "nsew")
              
         elif user_name == '' or password == '':
              print('Enter Both username and password')

         elif user_name != dummy_data['username'] or user_name != dummy_data['password']:
              print('Wrong username or password')

    def log_out(self):
         self.homepage.grid_forget()
         self.signup_frame.grid_forget()
         self.signin_frame.tkraise()
         self.signin_frame.grid(row = 0, columns = 2, padx=52, pady=60)

      
         
         
          
	
    def change_title_bar_color(self):
      try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR =  BLUE_GRAY_HEX
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
      except:
            pass


          


if __name__ == '__main__':
    App()