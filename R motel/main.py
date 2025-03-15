from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from support import User_actions

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"

class app:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("900x600")
        self.window.title("R Motel")
        self.login_form()
        self.window.resizable(False, False)
        self.window.mainloop()

    #class
    @staticmethod
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    #login window
    def login_form(self):
        self.background=canvas= Canvas(self.window,bg ="white",height = 600,width = 900,bd = 0,highlightthickness = 0,relief = "ridge") #intial white background

        #loading login img and placing
        login_img=canvas.place(x = 0, y = 0)
        login_page_left_img = PhotoImage(file=self.relative_to_assets("login_form1.png"))
        Login_img1 = canvas.create_image(180.0,298.0,image=login_page_left_img)
        canvas.image = login_page_left_img

        #welcome text
        welcom_text=canvas.create_text(567.0,74.0,anchor="nw",text="Welcome",fill="#004B6A",font=("Bungee Regular", 45 * -1))
        login_img= PhotoImage(file=self.relative_to_assets("login_img.png"))
        login_img_stack=canvas.create_image(518.0,122.0,image=login_img)
        login_img.image=login_img
    

        #username field
        useremail_text=canvas.create_text(487.0,184.0,anchor="nw",text="Email :",fill="#004B6A",font=("Bungee Regular", 16 * -1))
        useremail_img=PhotoImage(file=self.relative_to_assets("username_entry.png"))
        useremail_img_background= canvas.create_image(635.0,231.0,image=useremail_img)
        self.email = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0,font=(10))
        self.email.place(x=486.0,y=217.0,width=292.0,height=30.0)
        useremail_img.image =useremail_img

        #password field
        password_text=canvas.create_text(487.0,262.0,anchor="nw",text="Password:",fill="#004B6A",font=("Bungee Regular", 16 * -1))
        password_img = PhotoImage(file=self.relative_to_assets("username_entry.png"))
        password_img_background=canvas.create_image(635.0,308.0,image=password_img)
        self.password=Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0,show="*",font=(12))
        self.password.place(x=486.0,y=293.0,width=292.0,height=30.0)
        password_img.image=password_img

        #login form message
        self.login_msg=canvas.create_text(486.0,335.0,anchor="nw",text="Please Enter  Your Email and Password",fill="#004B6A",font=("Bungee Regular", 12 * -1))

        #login button
        button_img=button_image_1 = PhotoImage(file=self.relative_to_assets("login_button.png"))
        login_button=Button(image=button_img,borderwidth=0,highlightthickness=0,command=self.LoginUser,relief="flat")
        login_button.place(x=486.0,y=370.0,width=310.0,height=40.0)
        button_img.image=button_img
        
        #or
        or_img = PhotoImage(file=self.relative_to_assets("login_or.png"))
        login_or_img=canvas.create_image(640.0,457.0,image=or_img)
        or_img.image=or_img

        #forgot password UI
        email_img=PhotoImage(file=self.relative_to_assets("login_form_email.png"))
        login_email_img = canvas.create_image(509.0,500.0,image=email_img)
        email_img.image=email_img
        forgot_password=canvas.create_text(530.0,480.0,anchor="nw",text="Forgot Password?",fill="#004B6A",font=("Bungee Regular", 16 * -1))
        forgot_password_button_img=PhotoImage(file=self.relative_to_assets("forgot_password.png"))
        forgot_password_button=Button(image=forgot_password_button_img,borderwidth=0,highlightthickness=0,command=self.user_forgot_password,relief="flat")
        forgot_password_button.place(x=740.0,y=490.0,width=94.0,height=24.0)
        forgot_password_button_img.image=forgot_password_button_img

        #sign up UP
        signup_img=PhotoImage(file=self.relative_to_assets("login_form_signup.png"))
        login_signup_img= canvas.create_image(509.0,550.0,image=signup_img)
        signup_img.image=signup_img
        sing_up=canvas.create_text(530.0,533.0,anchor="nw",text="Don’t Have Account?",fill="#004B6A",font=("Bungee Regular", 16 * -1))
        sing_up_img=PhotoImage(file=self.relative_to_assets("signup.png"))
        sing_up_button=Button(image=sing_up_img,borderwidth=0,highlightthickness=0,command=lambda: print("signup clicked"),relief="flat")
        sing_up_button.place(x=740.0,y=543.0,width=94.0,height=24.0)
        sing_up_img.image=sing_up_img

    #main login function
    def LoginUser(self):
        email=self.email.get()
        password=self.password.get()
        if not email or not password:
            self.background.itemconfig(self.login_msg, text="Please Enter Your Email and Password First!", fill="red")
        else:
            self.auth_login = User_actions(email,password)  
            result = self.auth_login.login_user() 
            if result==False:
                self.background.itemconfig(self.login_msg, text="Invalid username or password!", fill="red")
            elif result[0][4]==True: 
                #self.show_staff_dashboard()
                pass
            else: 
                self.user_name = result[0][1]  
                self.user_email =email  
                self.clear_screen()  
                print("WORKING")

    #forgot password page       
    def user_forgot_password(self):
        self.clear_screen() 
        self.background=canvas= Canvas(self.window,bg ="white",height = 600,width = 900,bd = 0,highlightthickness = 0,relief = "ridge") #intial white background

        #left side page
        canvas.place(x = 0, y = 0) #basic setup
        forgot_pass_img_open=PhotoImage(file=self.relative_to_assets("forget_pass.png"))
        forgot_pass_img = canvas.create_image(168.0,305.0,image=forgot_pass_img_open)
        forgot_pass_img_open.image=forgot_pass_img_open

        #back button
        back_button_img= PhotoImage(file=self.relative_to_assets("back_button.png"))
        back_button= Button(image=back_button_img,borderwidth=0,highlightthickness=0,command=self.login_form,relief="flat")
        back_button.place(x=369.0,y=18.0,width=45.0,height=48.0)
        back_button_img.image=back_button_img

        #heading
        heading_logo_img= PhotoImage(file=self.relative_to_assets("forgot_password_head.png"))
        heading_logo = canvas.create_image(614.0,129.0,image=heading_logo_img)
        heading_logo_img.image=heading_logo_img

        #helping text
        text=canvas.create_text(360.0,190.0,anchor="nw",text="If you wish to reset your password due to forgetfulness,you can \n request a reset here. We will forward your request to  a staff member.\nfor verification. Please approach a staff member for further\n assistance.",
        fill="#004B6A",font=("Bungee Regular", 12 * -1))

        #email field
        email=canvas.create_text(380.0,336.0,anchor="nw",text="Email :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        #entry field
        forgot_email_img = PhotoImage(file=self.relative_to_assets("forgot_email_entry.png"))
        forgot_email=canvas.create_image(662.0,360.0,image=forgot_email_img)
        self.forgot_email= Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0,font=(12))
        self.forgot_email.place(x=501.0,y=345.0,width=322.0,height=30.0)
        forgot_email_img.image=forgot_email_img

        #forgot password message field
        self.forgot_pass_msg=canvas.create_text(383.0,387.0,anchor="nw",text="Please Enter Registered Your Email Address",fill="#004B6A",font=("Bungee Regular", 14 * -1))

        #submit button
        submit_button_img= PhotoImage(file=self.relative_to_assets("forgot_passwd_button.png"))
        submit_button= Button(image=submit_button_img,borderwidth=0,highlightthickness=0,command=self.forgot_passwd_request,relief="flat")
        submit_button.place(x=390.0,y=433.0,width=452.0,height=40.0)
        submit_button_img.image=submit_button_img

    #forgot password logic fucntion
    def forgot_passwd_request(self):
        user = User_actions()
        email=self.forgot_email.get()
        if not email:
            self.background.itemconfig(self.forgot_pass_msg, text="Please Enter Your Email First!", fill="red")
        else:
            result=user.password_reset(email)
            if result=="done":
                self.background.itemconfig(self.forgot_pass_msg, text="Request Submitted", fill="blue")
            elif result=="pending request":
                self.background.itemconfig(self.forgot_pass_msg, text="Email is already used for a request!", fill="red")
            elif result=="user_exsist_false":
                self.background.itemconfig(self.forgot_pass_msg, text="No user found with this email", fill="red")





    #clear everything function
    def clear_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()
            
Motel_app = app() 