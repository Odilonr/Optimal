import customtkinter as ctk
try:
	from ctypes import windll, byref, sizeof, c_int
except:
	pass
from PIL import Image
from themes import BLUE_GRAY, BLUE_GRAY_HEX
from login import Login

dummy_data = {
      'name':'Odilon',
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

        image = ctk.CTkImage(light_image=Image.open("coleur_different.jpg"),
                                  dark_image=Image.open("coleur_different.jpg"),
                                  size=(500, 500))
        self.image_label = ctk.CTkLabel(master=self, image=image, fg_color='#27292b',text="")
        self.image_label.place(x = 8, y = 8)

        self.login_frame = Login(master=self)
        self.login_frame.grid(row = 0, columns = 2, padx=500, pady=60)

        self.mainloop()

	
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