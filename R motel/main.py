from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,ttk
from support import User_actions
from tkinter import *
import re
import datetime

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
        sing_up_button=Button(image=sing_up_img,borderwidth=0,highlightthickness=0,command=self.sign_up_page,relief="flat")
        sing_up_button.place(x=740.0,y=543.0,width=94.0,height=24.0)
        sing_up_img.image=sing_up_img

    #main login function
    def LoginUser(self):
        #email=self.email.get()
        #password=self.password.get()
        email="test6"
        password="test6"
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
                self.home()
                

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

    #sign up page
    def sign_up_page(self):
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
        heading_logo_img= PhotoImage(file=self.relative_to_assets("sign_up_heading.png"))
        heading_logo = canvas.create_image(621.0,85.0,image=heading_logo_img)
        heading_logo_img.image=heading_logo_img

        #fields
        #first name text and entry
        first_name=canvas.create_text(365.0,174.0,anchor="nw",text="First Name :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        fname_img_open = PhotoImage(file=self.relative_to_assets("sign_up_entry.png"))
        fname_img = canvas.create_image(692.0,199.0,image=fname_img_open)
        self.fname= Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0,font=(11))
        self.fname.place(x=547.0,y=184.0,width=290.0,height=30.0)
        fname_img_open.image=fname_img_open

        #last name
        last_name=canvas.create_text(365.0,221.0,anchor="nw",text="Last Name :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        fname_img_open = PhotoImage(file=self.relative_to_assets("sign_up_entry.png"))
        fname_img = canvas.create_image(692.0,247.0,image=fname_img_open)
        self.lname= Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0,font=(11))
        self.lname.place(x=547.0,y=231.0,width=290.0,height=30.0)
        fname_img_open.image=fname_img_open

        #mobile number
        first_name=canvas.create_text(365.0,272.0,anchor="nw",text="Mobile No. :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        fname_img_open = PhotoImage(file=self.relative_to_assets("sign_up_entry.png"))
        fname_img = canvas.create_image(692.0,298.0,image=fname_img_open)
        self.mobile= Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0,font=(11))
        self.mobile.place(x=547.0,y=282.0,width=290.0,height=30.0)
        fname_img_open.image=fname_img_open

        #email
        first_name=canvas.create_text(365.0,323.0,anchor="nw",text="Email :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        fname_img_open = PhotoImage(file=self.relative_to_assets("sign_up_entry.png"))
        fname_img = canvas.create_image(692.0,349.0,image=fname_img_open)
        self.email= Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0,font=(11))
        self.email.place(x=547.0,y=333.0,width=290.0,height=30.0)
        fname_img_open.image=fname_img_open

        #password
        first_name=canvas.create_text(365.0,374.0,anchor="nw",text="Password :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        fname_img_open = PhotoImage(file=self.relative_to_assets("sign_up_entry.png"))
        fname_img = canvas.create_image(692.0,400.0,image=fname_img_open)
        self.password1= Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0,show="*",font=(11))
        self.password1.place(x=547.0,y=384.0,width=290.0,height=30.0)
        fname_img_open.image=fname_img_open

        #confirm password 
        first_name=canvas.create_text(365.0,425.0,anchor="nw",text="Re Password :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        fname_img_open = PhotoImage(file=self.relative_to_assets("sign_up_entry.png"))
        fname_img = canvas.create_image(692.0,451.0,image=fname_img_open)
        self.password2= Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0,show="*",font=(11))
        self.password2.place(x=547.0, y=435.0,width=290.0,height=30.0)
        fname_img_open.image=fname_img_open

        #message field
        self.singup_msg=canvas.create_text(365.0,478.0,anchor="nw",text="Please Enter  Your Information",fill="#004B6A",font=("Bungee Regular", 12 * -1))

        #submit button
        submit_button_img = PhotoImage(file=self.relative_to_assets("signup_submit.png"))
        submit_button = Button(image=submit_button_img,borderwidth=0,highlightthickness=0,command=self.submit_user_signup,relief="flat")
        submit_button.place(x=365.0,y=517.0,width=481.0,height=40.0)
        submit_button_img.image=submit_button_img

    #singup logical function
    def submit_user_signup(self):
        email_pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        mobile_pattern=r'^\d{10}$'
        fname=self.fname.get()
        lname=self.lname.get()
        mobile=self.mobile.get()
        email=self.email.get()
        pass1=self.password1.get()
        pass2=self.password2.get()
        if not fname or not lname or not mobile or not email or not pass1 or not pass2:
            self.background.itemconfig(self.singup_msg, text="Please fill all fields!", fill="red")
        elif re.match(email_pattern, email):
            if re.match(mobile_pattern,mobile):
                if pass1==pass2:
                    password=self.password1.get()
                    user=User_actions()
                    result=user.create_user(fname,lname,mobile,email,password)
                    if result:
                        self.background.itemconfig(self.singup_msg, text="Account created successfully.", fill="Blue")
                    else:
                        self.background.itemconfig(self.singup_msg, text="An account with this email address already exists.", fill="red")
                else:
                    self.background.itemconfig(self.singup_msg, text="Passwords must match!", fill="red")
            else:
                self.background.itemconfig(self.singup_msg, text="Enter valid mobile number!", fill="red")
        else:
            self.background.itemconfig(self.singup_msg, text="Enter valid email.", fill="red")
            
                
    #home page
    def home(self):
        self.clear_screen() 
        self.background=canvas= Canvas(self.window,bg ="white",height = 600,width = 900,bd = 0,highlightthickness = 0,relief = "ridge") #intial white background
        canvas.place(x = 0, y = 0) #basic setup

        #left panel
        left_home_img= PhotoImage(file=self.relative_to_assets("home_left_img.png"))
        left_home=canvas.create_image(92.0,305.0,image=left_home_img)
        left_home_img.image=left_home_img

        #heading
        home_img = PhotoImage(file=self.relative_to_assets("home_page_head.png"))
        home_heading= canvas.create_image(512.0,88.0,image=home_img)
        home_img.image=home_img

        #text
        help_text=canvas.create_text(264.0,164.0,anchor="nw",text="Your comfort is our priority.\nPlease choose an option to get started,",fill="#004B6A",font=("Bungee Regular", 18 * -1))

        #buttons
        #account button
        account_button_img= PhotoImage(file=self.relative_to_assets("account_button.png"))
        account_button = Button(image=account_button_img,borderwidth=0,highlightthickness=0,command=self.my_account,relief="flat")
        account_button.place(x=264.0,y=274.0,width=248.23699951171875,height=40.0)
        account_button_img.image=account_button_img

        #account info button
        account_info_img = PhotoImage(file=self.relative_to_assets("account_info_button.png"))
        account_info_button = Button(image=account_info_img,borderwidth=0,highlightthickness=0,command=self.account_info,relief="flat")
        account_info_button.place(x=594.0,y=274.0,width=248.23699951171875,height=40.0)
        account_info_img.image= account_info_img

        #booking button
        booking_button_img = PhotoImage(file=self.relative_to_assets("booking_button.png"))
        booking_button = Button(image=booking_button_img,borderwidth=0,highlightthickness=0,command=self.room_booking,relief="flat")
        booking_button.place(x=264.0,y=362.0,width=248.23699951171875,height=40.0)
        booking_button_img.image=booking_button_img

        #Booking history button
        all_booking_img = PhotoImage(file=self.relative_to_assets("all_booking_button.png"))
        all_booking_button= Button(image=all_booking_img,borderwidth=0,highlightthickness=0,command=self.booking_history,relief="flat")
        all_booking_button.place(x=594.0,y=362.0,width=248.23699951171875,height=40.0)
        all_booking_img.image=all_booking_img 

        #food button
        order_food_img = PhotoImage(file=self.relative_to_assets("order_food_button.png"))
        order_food_button = Button(image=order_food_img,borderwidth=0,highlightthickness=0,command=self.meals_order_page,relief="flat")
        order_food_button.place(x=264.0,y=451.0,width=248.23699951171875,height=40.0)
        order_food_img.image=order_food_img

        #order status button
        order_status_img= PhotoImage(file=self.relative_to_assets("order_status_button.png"))
        order_status_button = Button(image=order_status_img,borderwidth=0,highlightthickness=0,command=lambda: print("order status clicked"),relief="flat")
        order_status_button.place(x=594.0,y=451.0,width=248.23699951171875,height=40.0)
        order_status_img.image=order_status_img

    #account info page
    def account_info(self):
        self.clear_screen() 
        self.background=canvas= Canvas(self.window,bg ="white",height = 600,width = 900,bd = 0,highlightthickness = 0,relief = "ridge") #intial white background
        canvas.place(x = 0, y = 0) #basic setup

        #left pannels 
        left_home_img= PhotoImage(file=self.relative_to_assets("account_l_panel.png"))
        left_home=canvas.create_image(92.0,305.0,image=left_home_img)
        left_home_img.image=left_home_img

        #back button
        back_button_img= PhotoImage(file=self.relative_to_assets("back_button.png"))
        back_button= Button(image=back_button_img,borderwidth=0,highlightthickness=0,command=self.home,relief="flat")
        back_button.place(x=209.0,y=18.0,width=45.0,height=48.0)
        back_button_img.image=back_button_img

        #heading
        home_img = PhotoImage(file=self.relative_to_assets("account_info_head.png"))
        home_heading= canvas.create_image(512.0,118.0,image=home_img)
        home_img.image=home_img

        #logical function
        user=User_actions()
        result=user.user_account(self.user_email)
        total_spend=user.user_spends(self.user_email)

        #fname
        fname=canvas.create_text(231.0,238.0,anchor="nw",text="First Name :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        user_fname=canvas.create_text(477.0,238.0,anchor="nw",text=f"{result[0][1]}",fill="#004B6A",font=("Bungee Regular", 20 * -1))

        #lname
        lname=canvas.create_text(231.0,283.0,anchor="nw",text="Last Name :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        user_lname=canvas.create_text(477.0,283.0,anchor="nw",text=f"{result[0][2]}",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        
        #mobile
        mobile=canvas.create_text(231.0,329.0,anchor="nw",text="Mobile No :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        user_mobile=canvas.create_text(477.0,329.0,anchor="nw",text=f"{result[0][3]}",fill="#004B6A",font=("Bungee Regular", 20 * -1))

        #email
        email=canvas.create_text(231.0,374.0,anchor="nw",text="EMail :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        user_email=canvas.create_text(477.0,374.0,anchor="nw",text=f"{result[0][5]}",fill="#004B6A",font=("Bungee Regular", 20 * -1))

        #total
        total=canvas.create_text(231.0,420.0,anchor="nw",text="Total Spends :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        total_spend=canvas.create_text(477.0,419.0,anchor="nw",text=f"Rs.{total_spend}",fill="#004B6A",font=("Bungee Regular", 20 * -1))

        #bottom msg
        msg=canvas.create_text(231.0,476.0,anchor="nw",text="TO change account info and password vist My account",fill="#004B6A",font=("Bungee Regular", 15 * -1))

    def my_account(self):
        self.clear_screen() 
        self.background=canvas= Canvas(self.window,bg ="white",height = 600,width = 900,bd = 0,highlightthickness = 0,relief = "ridge") #intial white background
        canvas.place(x = 0, y = 0) #basic setup

        #logical function
        user = User_actions()
        result=user.account_info_fetch(self.user_email)
        fname=result[0][0]
        lname=result[0][1]
        mob_no=result[0][2]
        email=result[0][3]

        #left pannels 
        left_home_img= PhotoImage(file=self.relative_to_assets("account_l_panel.png"))
        left_home=canvas.create_image(92.0,305.0,image=left_home_img)
        left_home_img.image=left_home_img

        #back button
        self.back_button()
        #heading
        home_img = PhotoImage(file=self.relative_to_assets("my account_head.png"))
        home_heading= canvas.create_image(512.0,118.0,image=home_img)
        home_img.image=home_img

        #fname
        fname_label = canvas.create_text(239.0, 190.0, anchor="nw", text="First Name :", fill="#004B6A", font=("Bungee Regular", 20 * -1))
        fname_img = PhotoImage(file=self.relative_to_assets("my_acc_entry_img.png"))
        fname_back = canvas.create_image(558.5, 214.0, image=fname_img)
        self.fname = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0,font=(11))
        self.fname.place(x=410.0, y=200.0, width=297.0, height=26.0)
        fname_img.image = fname_img
        self.fname.insert(0, fname) 

        #lname
        lname_label = canvas.create_text(239.0, 235.0, anchor="nw", text="Last Name :", fill="#004B6A", font=("Bungee Regular", 20 * -1))
        lname_img = PhotoImage(file=self.relative_to_assets("my_acc_entry_img.png"))
        lname_back = canvas.create_image(558.5, 261.0, image=lname_img)
        self.lname = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0,font=(11))
        self.lname.place(x=410.0, y=247.0, width=297.0, height=26.0)
        lname_img.image = lname_img
        self.lname.insert(0, lname) 

        #mobile no
        mobile=canvas.create_text(239.0,285.0,anchor="nw",text="Mobile No :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        mobile_img=entry_1= PhotoImage(file=self.relative_to_assets("my_acc_entry_img.png"))
        mobile_back= canvas.create_image(558.5,309.0,image=lname_img)
        self.mobile= Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0,font=(11))
        self.mobile.place(x=410.0,y=295.0,width=297.0,height=26.0)
        mobile_img.image=mobile_img
        self.mobile.insert(0,mob_no)

        #password help msg
        help_msg=canvas.create_text(337.0,331.0,anchor="nw",text="Leave Password Blank to keep old password",fill="#004B6A",font=("Bungee Regular", 15 * -1))

        #password1
        password1=canvas.create_text(239.0,368.0,anchor="nw",text="Password:",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        password1_img=entry_1= PhotoImage(file=self.relative_to_assets("my_acc_entry_img.png"))
        password1_back= canvas.create_image(558.5,392.0,image=password1_img)
        self.password1= Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0,font=(11),show="*")
        self.password1.place(x=410.0,y=378.0,width=297.0,height=26.0)
        password1_img.image=password1_img

        #password2
        password2=canvas.create_text(239.0,410.0,anchor="nw",text="RE PASSWORD:",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        password2_img=entry_1= PhotoImage(file=self.relative_to_assets("my_acc_entry_img.png"))
        password2_back= canvas.create_image(558.5,434.0,image=password2_img)
        self.password2= Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0,font=(11),show="*")
        self.password2.place(x=410.0,y=420.0,width=297.0,height=26.0)
        password2_img.image=password2_img

        #msg
        self.my_acc_msg=canvas.create_text(239.0,461.0,anchor="nw",text="TO change account info and password please fill above",fill="#004B6A",font=("Bungee Regular", 15 * -1))

        #submit button
        sub_img = PhotoImage(file=self.relative_to_assets("my_acc_sub.png"))
        submit_button = Button(image=sub_img,borderwidth=0,highlightthickness=0,command=self.account_updation,relief="flat")
        submit_button.place(x=239.0,y=503.0,width=586.0,height=40.0)
        sub_img.image=sub_img

    #updating info without entring password
    def account_updation_without_pass(self):
        user = User_actions()
        email=self.user_email
        fname=self.fname.get()
        lname=self.lname.get()
        mobile=self.mobile.get()
        result=user.user_account_update(email,fname,lname,mobile)
        mobile_pattern=r'^\d{10}$'
        if re.match(mobile_pattern,mobile):
            if not result:
                    self.background.itemconfig(self.my_acc_msg, text="ERROR IN UPDATING USER INFO", fill="red")
            else:
                self.background.itemconfig(self.my_acc_msg, text="User information updated", fill="green")
        else:
            self.background.itemconfig(self.my_acc_msg, text="Enter valid mobile number!", fill="red")


    #updating user info with password and other info
    def account_updation(self):
        user = User_actions()
        email=self.user_email
        passwd1=self.password1.get()
        passwd2=self.password2.get()
        if not passwd1 or not passwd2:
            self.account_updation_without_pass()    
        else:
            if passwd1==passwd2:
                result=user.user_account_password_update(email,passwd1)
                self.account_updation_without_pass() 
                if result:
                    self.background.itemconfig(self.my_acc_msg, text="User information updated", fill="green")
                    self.password1.delete(0,END)
                    self.password2.delete(0,END)
                else:
                    self.background.itemconfig(self.my_acc_msg, text="ERROR IN UPDATING USER PASSWORD", fill="red")
            else:
                self.background.itemconfig(self.my_acc_msg, text="Password and re password must match", fill="red")

    #room booking form
    def room_booking(self):
        self.clear_screen() 
        self.background=canvas= Canvas(self.window,bg ="white",height = 600,width = 900,bd = 0,highlightthickness = 0,relief = "ridge") #intial white background
        canvas.place(x = 0, y = 0) #basic setup

        #left pannels 
        left_home_img= PhotoImage(file=self.relative_to_assets("booking_l_panel.png"))
        left_home=canvas.create_image(92.0,305.0,image=left_home_img)
        left_home_img.image=left_home_img

        #back button
        self.back_button()

        #heading
        home_img = PhotoImage(file=self.relative_to_assets("room_booking_head.png"))
        home_heading= canvas.create_image(512.0,118.0,image=home_img)
        home_img.image=home_img

        #tree back
        room_back_img= PhotoImage(file=self.relative_to_assets("room_tree_back.png"))
        room_background= canvas.create_image(539.0,281.0,image=room_back_img)
        room_back_img.image=room_back_img

        #msg
        self.room_booking_msg=canvas.create_text(283.0,394.0,anchor="nw",text="Enter Date (DD-MM-YYYY)",fill="#004B6A",font=("Bungee Regular", 15 * -1))

        #check in date
        check_in=canvas.create_text(283.0,425.0,anchor="nw",text="Check IN Date :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        check_in_img=PhotoImage(file=self.relative_to_assets("check_date_img.png"))
        check_in_background = canvas.create_image(643.0,451.0,image=check_in_img)
        check_in_img.image=check_in_img
        self.check_in_date=entry_1 = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.check_in_date.place(x=499.0,y=437.0,width=288.0,height=26.0)

        #check out date
        check_out=canvas.create_text(283.0,469.0,anchor="nw",text="Check out Date :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        check_out_background = canvas.create_image(643.0,495.0,image=check_in_img)
        self.check_out_date=entry_1 = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.check_out_date.place(x=499.0,y=481.0,width=288.0,height=26.0)

        #tree views
        user = User_actions()
        result = user.room_booking()
        columns = ("Room Number", "Beds", "Price")
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",background="white",fieldbackground="white",foreground="black",bordercolor="white",font=("Arial", 12),rowheight=25)
        style.configure("Treeview.Heading",
                        background="white",
                        foreground="black",
                        font=("Arial", 11))
        style.map("Treeview",
                background=[("selected", "#ADD8E6")],
                foreground=[("selected", "black")])
        self.tree = ttk.Treeview(canvas, columns=columns, show="headings", style="Treeview")
        self.tree.heading("Room Number", text="Room Number")
        self.tree.heading("Beds", text="Beds")
        self.tree.heading("Price", text="Price")

        self.tree.column("Room Number", width=100, anchor="center")
        self.tree.column("Beds", width=100, anchor="center")
        self.tree.column("Price", width=100, anchor="center")
        self.tree.place(x=340.0, y=180.0, width=400.0, height=200.0)
        for row in result:
            self.tree.insert("", "end", values=row)

        #sbumit button
        sub_img = PhotoImage(file=self.relative_to_assets("my_acc_sub.png"))
        submit_button = Button(image=sub_img,borderwidth=0,highlightthickness=0,command=self.book_room,relief="flat")
        submit_button.place(x=250.0,y=528.0,width=586.0,height=40.0)
        sub_img.image=sub_img


    #get room booking data and feed into DBMS 
    def book_room(self):
        selected_room = self.tree.selection()
        user = User_actions()

        #error if room not selected
        if not selected_room:
            self.background.itemconfig(self.room_booking_msg, text="Please select a room.", fill="red")
            return
        check_in_date = self.check_in_date.get()
        check_out_date = self.check_out_date.get()

        #dates validation
        try:
            in_day, in_month, in_year = check_in_date.split('-')
            check_in_day = int(in_day)
            check_in_month = int(in_month)
            check_in_year = int(in_year)
            check_in = datetime.date(check_in_year, check_in_month, check_in_day)
            today = datetime.date.today()
            if check_in < today:
                self.background.itemconfig(self.room_booking_msg, text="Check-in date cannot be earlier than today.", fill="red")
                return
        except ValueError:
            self.background.itemconfig(self.room_booking_msg, text="Invalid Check-in Date (DD-MM-YYYY)", fill="red")
            return
        try:
            out_day, out_month, out_year = check_out_date.split('-')
            check_out_day = int(out_day)
            check_out_month = int(out_month)
            check_out_year = int(out_year)
            check_out = datetime.date(check_out_year, check_out_month, check_out_day)
            if check_out <= check_in:
                self.background.itemconfig(self.room_booking_msg, text="Check-out must be after check-in date.", fill="red")
                return
        except ValueError:
            self.background.itemconfig(self.room_booking_msg, text="Invalid Check-out Date (DD-MM-YYYY)", fill="red")
            return
        
        #feeding room booking data
        room = self.tree.item(selected_room, "values")
        try:
            day_count = (check_out - check_in).days
            room_no = room[0]
            price = user.price_fetch(room_no)
            price_total = day_count * price
            email = self.user_email
            self.auth_login.room_booking_conform(email, room_no, check_in, check_out, day_count, price_total)
            self.room_booking() 
            self.background.itemconfig(self.room_booking_msg,text=f"Booking confirmed! Total: Rs.{price_total}",fill="green")
        except Exception as e:
            print(f"Error: {e}")
            self.background.itemconfig(self.room_booking_msg,text="Error processing booking. Check dates and try again.",fill="red")

    def booking_history(self):
        self.clear_screen() 
        self.background=canvas= Canvas(self.window,bg ="white",height = 600,width = 900,bd = 0,highlightthickness = 0,relief = "ridge") #intial white background
        canvas.place(x = 0, y = 0) #basic setup

        #left pannels 
        left_home_img= PhotoImage(file=self.relative_to_assets("booking_l_panel.png"))
        left_home=canvas.create_image(92.0,305.0,image=left_home_img)
        left_home_img.image=left_home_img

        #back button
        self.back_button()

        #heading
        home_img = PhotoImage(file=self.relative_to_assets("booking_history_head.png"))
        home_heading= canvas.create_image(545.0,133.0,image=home_img)
        home_img.image=home_img

        #tree back
        room_back_img= PhotoImage(file=self.relative_to_assets("booking_history_back.png"))
        room_background= canvas.create_image(550.0,341.0,image=room_back_img)
        room_back_img.image=room_back_img

        #tree views
        user = User_actions()
        result=user.user_booking_history(self.user_email)
        columns = ("Room Number", "Check in date", "Check out date")
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",background="white",fieldbackground="white",foreground="black",bordercolor="white",font=("Arial", 12),rowheight=25)
        style.configure("Treeview.Heading",
                        background="white",
                        foreground="black",
                        font=("Arial", 11))
        style.map("Treeview",
                background=[("selected", "#ADD8E6")],
                foreground=[("selected", "black")])
        self.tree = ttk.Treeview(canvas, columns=columns, show="headings", style="Treeview")
        self.tree.heading("Room Number", text="Room Number")
        self.tree.heading("Check in date", text="Check in date")
        self.tree.heading("Check out date", text="Check out date")

        self.tree.column("Room Number", width=100, anchor="center")
        self.tree.column("Check in date", width=100, anchor="center")
        self.tree.column("Check out date", width=100, anchor="center")
        self.tree.place(x=340.0, y=220.0, width=400.0, height=250.0)
        for row in result:
            self.tree.insert("", "end", values=row)

    def meals_order_page(self):
        self.clear_screen() 
        self.background=canvas= Canvas(self.window,bg ="white",height = 600,width = 900,bd = 0,highlightthickness = 0,relief = "ridge") #intial white background
        canvas.place(x = 0, y = 0) #basic setup

        #left pannels 
        left_home_img= PhotoImage(file=self.relative_to_assets("food_l_panel.png"))
        left_home=canvas.create_image(92.0,305.0,image=left_home_img)
        left_home_img.image=left_home_img

        #back button
        self.back_button()

        #heading
        home_img = PhotoImage(file=self.relative_to_assets("meal_order_head.png"))
        home_heading= canvas.create_image(541.0,99.0,image=home_img)
        home_img.image=home_img

        #tree back
        room_back_img= PhotoImage(file=self.relative_to_assets("food_order_tree_back.png"))
        room_background= canvas.create_image(551.0,285.0,image=room_back_img)
        room_back_img.image=room_back_img

        #msg
        self.meal_order_msg=canvas.create_text(295.0,416.0,anchor="nw",text="Select food item and enter quantity",fill="#004B6A",font=("Bungee Regular", 15 * -1))

        #quantity section
        quantity_lable=canvas.create_text(295.0,449.0,anchor="nw",text="Quantity :",fill="#004B6A",font=("Bungee Regular", 20 * -1))

        #plus button add_button.png
        add_button_img = PhotoImage(file=self.relative_to_assets("add_button.png"))
        add_button = Button(image=add_button_img,borderwidth=0,highlightthickness=0,command=lambda: print("+ clicked"),relief="flat")
        add_button.place(x=433.0,y=459.0,width=48.73284912109375,height=29.0)
        add_button_img.image=add_button_img

        #entry
        entry_img = PhotoImage(file=self.relative_to_assets("quantity_entry.png"))
        entry_back = canvas.create_image(551.5,472.0,image=entry_img)
        self.quantity = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.quantity.place(x=495.0,y=459.0, width=113.0,height=26.0)
        entry_img.image=entry_img 

        #minus button add_button.png
        minus_button_img = PhotoImage(file=self.relative_to_assets("minus_button.png"))
        minus_button = Button(image=minus_button_img,borderwidth=0,highlightthickness=0,command=lambda: print("- clicked"),relief="flat")
        minus_button.place(x=623.0,y=459.0,width=48.73284912109375,height=29.0)
        minus_button_img.image=minus_button_img

        #submit button 
        sub_img = PhotoImage(file=self.relative_to_assets("place_order_button.png"))
        submit_button = Button(image=sub_img,borderwidth=0,highlightthickness=0,command=self.place_food_order,relief="flat")
        submit_button.place(x=295.0,y=508.0,width=520.0,height=40.0)
        sub_img.image=sub_img

        #tree view
        user = User_actions()
        result=user.food_items_fetch()
        columns = ("item_id","Name", "Price")
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",background="white",fieldbackground="white",foreground="black",bordercolor="white",font=("Arial", 12),rowheight=25)
        style.configure("Treeview.Heading",
                        background="white",
                        foreground="black",
                        font=("Arial", 11))
        style.map("Treeview",
                background=[("selected", "#ADD8E6")],
                foreground=[("selected", "black")])
        self.tree = ttk.Treeview(canvas, columns=columns, show="headings", style="Treeview")

        self.tree.heading("item_id", text="item_id")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Price", text="Price")

        self.tree.column("item_id", width=80, anchor="center")
        self.tree.column("Name", width=100, anchor="center")
        self.tree.column("Price", width=100, anchor="center")
        self.tree.place(x=340.0, y=170.0, width=400.0, height=210.0)
        for row in result:
            self.tree.insert("", "end", values=row)
    
    #food order main funtion
    def place_food_order(self):
        user = User_actions()
        selected_item = self.tree.selection()
        if selected_item:
            selected_item = self.tree.item(selected_item[0])
            values = selected_item["values"]
            food_id = values[0] 
            food_name = values[1] 
            food_price=values[2]
            float_price=float(food_price)
            int_price=int(float_price)
            quantity = self.quantity.get()
            if not quantity:
                self.background.itemconfig(self.meal_order_msg,text="Please enter quantity !", fill="red")
            else:
                email=self.user_email
                total_quantity=int(quantity)
                total_price=(float_price*total_quantity)
                place_order = user.food_order(email, food_id, food_name,total_price, quantity)
                if place_order:
                    self.meals_order_page()
                    self.background.itemconfig(self.meal_order_msg,text=f"Order placed successfully.Your total is   Rs.{total_price}", fill="green")
                else:
                    self.background.itemconfig(self.meal_order_msg,text="You have no active room bookings.", fill="red")
        else:
            self.background.itemconfig(self.meal_order_msg,text="Please select a food item first", fill="red")
            
    #back button
    def back_button(self):
        back_button_img= PhotoImage(file=self.relative_to_assets("back_button.png"))
        back_button= Button(image=back_button_img,borderwidth=0,highlightthickness=0,command=self.home,relief="flat")
        back_button.place(x=209.0,y=18.0,width=45.0,height=48.0)
        back_button_img.image=back_button_img

    #clear everything function
    def clear_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()
            
Motel_app = app() 