import customtkinter as ctk
from PIL import Image
from tkinter import IntVar, StringVar
from ..data.database_manager import Databasemanager
from ..models.gymGoer import Gymbro
from ..utils.constant import BLUE_GRAY
from CTkMessagebox  import CTkMessagebox


class Signin(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,fg_color=BLUE_GRAY, width=830, height=420)
        self.master = master
        image = ctk.CTkImage(light_image=Image.open("src/assets/images/main_logo.jpg"),
                                  dark_image=Image.open("src/assets/images/main_logo.jpg"),
                                  size=(500, 500))
        self.image_label = ctk.CTkLabel(master=self, image=image, fg_color='#27292b',text="")
        self.image_label.place(x = -40, y = -20)
        font_signin = ctk.CTkFont(family = 'Microsoft Yahei UI Light', size = 20, weight = 'bold')
        font_signin_size = ctk.CTkFont(family = 'Microsoft Yahei UI Light', size = 17, weight = 'bold')
        font_username = ctk.CTkFont(family = 'Microsoft Yahei UI', size = 11)
        self.label_signin = ctk.CTkLabel(self,text = 'Sign in', font=font_signin, text_color= "#F2F2F2")
        self.label_signin.place(x = 500, y =60)

        self.user_name = ctk.CTkEntry(self, width=240,height=50, fg_color='white', border_width=2,
                                      font=font_username, placeholder_text='Username',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black')
        self.user_name.place(x=500,y=110)


        self.password = ctk.CTkEntry(self, width=240,height=50, fg_color='white', border_width=2,
                                      font=font_username, placeholder_text='Password',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black')
        self.password.place(x = 500, y = 170)


        self.signin_button = ctk.CTkButton(self, text='Sign in',width=240, height=50,border_width=1, border_color='white',fg_color=BLUE_GRAY,
                                            text_color='white',hover_color='#0c1545', font=font_signin_size, corner_radius=0)
        self.signin_button.place(x = 500, y = 240)
        


        self.or_label = ctk.CTkLabel(self, text='or', fg_color="transparent", width=40,text_color='white',
                                     font=('Microsoft Yahei UI Light',15))
        self.or_label.place(x=600,y=308)

        self.frame_or_line = ctk.CTkFrame(self, width=100, height=2, fg_color='white')
        self.frame_or_line.place(x=500, y=325)

        self.frame_or_line_2 = ctk.CTkFrame(self, width=100, height=2, fg_color='white')
        self.frame_or_line_2.place(x=640, y=325)

        self.create_message = ctk.CTkLabel(self, text="No account currently?", fg_color='transparent', text_color='white',
                                           font=('Microsoft Yahei UI Light', 15))
        self.create_message.place(x=510,y=360)

        self.signup_button = ctk.CTkButton(self, width=6, text='Sign Up', border_width=0, text_color='white', fg_color=BLUE_GRAY,
                                           hover_color=BLUE_GRAY,font=('Microsoft Yahei UI Light', 13,'bold'), cursor='hand2',
                                           command=self.signup)
        self.signup_button.place(x=664,y=360)
        
    def show(self):
        self.grid(row = 0, columns = 2, padx=52, pady=60)

    def hide(self):
        self.grid_forget()

             

    def signup(self):
        self.hide()
        self.master.signup_frame.tkraise()
        self.master.signup_frame.show()

class Signup(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,fg_color=BLUE_GRAY, width=830, height=420)
        self.master = master
        font_signup = ctk.CTkFont(family = 'Microsoft Yahei UI Light', size = 20, weight = 'bold')
        font_signin_size = ctk.CTkFont(family = 'Microsoft Yahei UI Light', size = 17, weight = 'bold')
        font_name = ctk.CTkFont(family = 'Microsoft Yahei UI', size = 11)

        self.label_signin = ctk.CTkLabel(self,text = 'Sign up', font=font_signup, text_color= "#F2F2F2")
        self.label_signin.place(x = 220, y =30)

        self.username_entry = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=font_name, placeholder_text='Username',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black')
        self.username_entry.place(x=220,y=70)


        self.password_entry = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=font_name, placeholder_text='Password',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black')
        self.password_entry.place(x = 410, y = 70)

        self.age_entry = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=font_name, placeholder_text='Age',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black')
        self.age_entry.place(x = 220, y = 130)
        
        self.weight_entry = ctk.CTkEntry(self, width=180,height=50, fg_color='white', border_width=2,
                                      font=font_name, placeholder_text='Weight',placeholder_text_color='#050000',
                                       corner_radius=0, text_color='black')
        self.weight_entry.place(x = 410, y = 130)

        self.activity_entry = ctk.CTkOptionMenu(self, width=180, height=50,button_color='white', fg_color='white', 
                                          dropdown_fg_color='white', values=['Sedentary','Active','Moderate','Very Active'], text_color='black', 
                                          dropdown_text_color='black', button_hover_color='#e6f0ef')
        self.activity_entry.place(x = 220, y = 190)

        self.height_entry = ctk.CTkOptionMenu(self, width=90, height=50,button_color='white', fg_color='white', 
                                          dropdown_fg_color='white', values=['1','2','3'], text_color='black', 
                                          dropdown_text_color='black', button_hover_color='#e6f0ef')
        self.height_entry.place(x = 410, y = 190)

        self.phase_entry = ctk.CTkOptionMenu(self, width=180, height=50,button_color='white', fg_color='white', 
                                          dropdown_fg_color='white', values=['Cut', 'Bulk'], text_color='black', 
                                          dropdown_text_color='black', button_hover_color='#e6f0ef')
        self.phase_entry.place(x = 220, y = 255)
        

        self.gender_label= ctk.CTkLabel(self, text='Gender', font=('Microsoft Yahei UI',18), text_color= "#F2F2F2")
        self.gender_label.place(x=410,y=265)

        # gender_var
        self.gender_var = StringVar(value=0)

        #Male
        self.male_button = ctk.CTkRadioButton(self, text='Male', value='M',variable=self.gender_var,font=('Microsoft Yahei UI',15),
                                              text_color='white', command=self.radiobutton_event)
        self.male_button.place(x = 480, y=270)

        #Female
        self.female_button = ctk.CTkRadioButton(self, text='Female', value='F', variable=self.gender_var,font=('Microsoft Yahei UI',15),
                                                text_color='white',command=self.radiobutton_event)
        self.female_button.place(x=565, y=270)


        self.signup_button = ctk.CTkButton(self, text='Create profile',width=240, height=50,border_width=1, border_color='white',fg_color=BLUE_GRAY,
                                            text_color='white',hover_color='#0c1545', font=font_signin_size, corner_radius=0,
                                            command=self.signup)
        self.signup_button.place(x = 290, y = 340)

    def radiobutton_event(self):
        print("radiobutton toggled, current value:", self.gender_var.get())

    def show(self):
        self.grid(row = 0, columns = 2, padx=52, pady=60)
    
    def hide(self):
        self.grid_forget()

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        age = self.age_entry.get()
        height = self.height_entry.get()
        weight = self.weight_entry.get()
        gender = self.gender_var.get()
        activity = self.activity_entry.get()
        phase= self.phase_entry.get()
        database = Databasemanager()

        athlete = database.get_athlete(username=username,password=password)

        if athlete:
            CTkMessagebox(self, title='Error', fg_color=BLUE_GRAY, bg_color='red',
                            message='User already exists',icon ='cancel',text_color='white')
            
        elif (username == '' or password == '' or age == '' or height == '' or weight == '' or gender == ''):
            CTkMessagebox(self, title='Error', fg_color=BLUE_GRAY, bg_color='red',
                            message='Please complete all categories',icon ='cancel',text_color='white')
            
        else:
            database.add_athlete(username=username, password=password, age=age, height=height, 
                                 weight=weight, activity=activity, phase=phase, gender=gender)
            
            self.grid_forget()
            self.master.signin_frame.tkraise()
            self.master.signin_frame.show()

        database.close()
         