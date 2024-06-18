import customtkinter as ctk
from themes import BLUE_GRAY
import locale
locale.setlocale(locale.LC_ALL,"")

class Login(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, fg_color=BLUE_GRAY, width=350, height=420)
        font_signin = ctk.CTkFont(family = 'Microsoft Yahei UI Light', size = 20, weight = 'bold')
        font_signin_size = ctk.CTkFont(family = 'Microsoft Yahei UI Light', size = 17, weight = 'bold')
        font_username = ctk.CTkFont(family = 'Microsoft Yahei UI', size = 11)
        self.label_signin = ctk.CTkLabel(self,text = 'Sign in', font=font_signin, text_color= "#F2F2F2")
        self.label_signin.place(x = 50, y =60)

        self.user_name = ctk.CTkEntry(self, width=240,height=50, fg_color='white', border_width=2,
                                      font=font_username, placeholder_text='Username',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black')
        self.user_name.place(x=50,y=110)


        self.password = ctk.CTkEntry(self, width=240,height=50, fg_color='white', border_width=2,
                                      font=font_username, placeholder_text='Password',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black')
        self.password.place(x = 50, y = 170)


        self.signin_button = ctk.CTkButton(self, text='Sign in',width=240, height=50,border_width=1, border_color='white',fg_color=BLUE_GRAY,
                                            text_color='white',hover_color='#0c1545', font=font_signin_size, corner_radius=0)
        self.signin_button.place(x = 50, y = 240)


        self.or_label = ctk.CTkLabel(self, text='or', fg_color="transparent", width=40,text_color='white',
                                     font=('Microsoft Yahei UI Light',15))
        self.or_label.place(x=150,y=308)

        self.frame_or_line = ctk.CTkFrame(self, width=100, height=2, fg_color='white')
        self.frame_or_line.place(x=50, y=325)

        self.frame_or_line_2 = ctk.CTkFrame(self, width=100, height=2, fg_color='white')
        self.frame_or_line_2.place(x=190, y=325)

        self.create_message = ctk.CTkLabel(self, text="No account currently?", fg_color='transparent', text_color='white',
                                           font=('Microsoft Yahei UI Light', 15))
        self.create_message.place(x=60,y=360)

        self.signup_button = ctk.CTkButton(self, width=6, text='Sign Up', border_width=0, text_color='white', fg_color=BLUE_GRAY,
                                           hover_color=BLUE_GRAY,font=('Microsoft Yahei UI Light', 15,'bold'), cursor='hand2')
        self.signup_button.place(x=210,y=360)







