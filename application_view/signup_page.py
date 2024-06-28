import customtkinter as ctk
from themes import BLUE_GRAY,BLUE_GRAY_TEST
from PIL import Image


class Signup(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,fg_color=BLUE_GRAY_TEST, width=830, height=420)
        self.master = master
        font_signup = ctk.CTkFont(family = 'Microsoft Yahei UI Light', size = 20, weight = 'bold')
        font_signin_size = ctk.CTkFont(family = 'Microsoft Yahei UI Light', size = 17, weight = 'bold')
        font_name = ctk.CTkFont(family = 'Microsoft Yahei UI', size = 11)

        self.label_signin = ctk.CTkLabel(self,text = 'Sign up', font=font_signup, text_color= "#F2F2F2")
        self.label_signin.place(x = 220, y =30)

        self.user_name = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=font_name, placeholder_text='Username',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black')
        self.user_name.place(x=220,y=70)


        self.password = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=font_name, placeholder_text='Password',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black')
        self.password.place(x = 410, y = 70)

        self.age = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=font_name, placeholder_text='Age',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black')
        self.age.place(x = 220, y = 130)
        
        self.weight = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=font_name, placeholder_text='Weight',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black')
        self.weight.place(x = 410, y = 130)

        self.activity = ctk.CTkOptionMenu(self, width=180, height=50,button_color='white', fg_color='white', 
                                          dropdown_fg_color='white', values=['Sendetary', 'Active'], text_color='black', 
                                          dropdown_text_color='black', button_hover_color='#e6f0ef')
        self.activity.place(x = 220, y = 190)

        self.height = ctk.CTkOptionMenu(self, width=90, height=50,button_color='white', fg_color='white', 
                                          dropdown_fg_color='white', values=['1','2','3'], text_color='black', 
                                          dropdown_text_color='black', button_hover_color='#e6f0ef')
        self.height.place(x = 410, y = 190)

        self.goal = ctk.CTkOptionMenu(self, width=180, height=50,button_color='white', fg_color='white', 
                                          dropdown_fg_color='white', values=['Cutting', 'Bulking','Maintaining'], text_color='black', 
                                          dropdown_text_color='black', button_hover_color='#e6f0ef')
        self.goal.place(x = 220, y = 255)
        

        self.gender_label= ctk.CTkLabel(self, text='Gender', font=('Microsoft Yahei UI',18), text_color= "#F2F2F2")
        self.gender_label.place(x=410,y=265)

        # gender_var
        self.gender_var = ctk.StringVar(value='None')

        #Male
        self.male_button = ctk.CTkRadioButton(self, text='Male', value='M', variable=self.gender_var,font=('Microsoft Yahei UI',15))
        self.male_button.place(x = 480, y=270)

        #Female
        self.female_button = ctk.CTkRadioButton(self, text='Female', value='F', variable=self.gender_var,font=('Microsoft Yahei UI',15))
        self.female_button.place(x=565, y=270)


        self.signup_button = ctk.CTkButton(self, text='Create profile',width=240, height=50,border_width=1, border_color='white',fg_color=BLUE_GRAY,
                                            text_color='white',hover_color='#0c1545', font=font_signin_size, corner_radius=0,
                                            command=self.signup)
        self.signup_button.place(x = 290, y = 340)

    def show(self):
        self.grid(row = 0, columns = 2, padx=52, pady=60)
    
    def hide(self):
        self.grid_forget()

    def signup(self):
         self.grid_forget()
         self.master.signin_frame.tkraise()
         self.master.signin_frame.show()