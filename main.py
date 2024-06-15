import customtkinter as ctk
try:
	from ctypes import windll, byref, sizeof, c_int
except:
	pass

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color='#030929')
        self.title('')
        try:
                self.iconbitmap('empty.ico')
        except:
              pass
        self.geometry('700x400')
        self.change_title_bar_color()
        self.mainloop()

	
    def change_title_bar_color(self):
          try:
               HWND = windll.user32.GetParent(self.winfo_id())
               DWMWA_ATTRIBUTE = 35
               COLOR =  0x00290903
               windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
          except:
            pass
           
          



App()