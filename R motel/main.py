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
        background=canvas = Canvas(self.window,bg ="white",height = 600,width = 900,bd = 0,highlightthickness = 0,relief = "ridge") #intial white background

        #loading login img and placing
        login_img=canvas.place(x = 0, y = 0)
        login_page_left_img = PhotoImage(file=self.relative_to_assets("login_form1.png"))
        Login_img1 = canvas.create_image(180.0,300.0,image=login_page_left_img)
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
        self.email = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.email.place(x=486.0,y=217.0,width=292.0,height=30.0)
        useremail_img.image =useremail_img

        #password field
        password_text=canvas.create_text(487.0,262.0,anchor="nw",text="Password:",fill="#004B6A",font=("Bungee Regular", 16 * -1))
        password_img = PhotoImage(file=self.relative_to_assets("username_entry.png"))
        password_img_background=canvas.create_image(635.0,308.0,image=password_img)
        self.password=Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.password.place(x=486.0,y=293.0,width=292.0,height=30.0)
        password_img.image=password_img

        #login button
        button_img=button_image_1 = PhotoImage(file=self.relative_to_assets("login_button.png"))
        login_button=Button(image=button_img,borderwidth=0,highlightthickness=0,command=self.LoginUser,relief="flat")
        login_button.place(x=480.0,y=350.0,width=310.0,height=40.0)
        button_img.image=button_img
        
        
    #main login function
    def LoginUser(self):
        self.email=self.email.get()
        password=self.password.get()
        if not self.email or not password:
            pass #message(Please Fill INFO)
        else:
            self.auth_login = User_actions(self.email,password)  
            result = self.auth_login.login_user() 
            if result==False:
                '''
                self.login_msg.config(text=f'Invalid username or password')
                self.user_email.delete(0, END) 
                self.password.delete(0, END)
                '''
            elif result[0][4]==True: 
                #self.show_staff_dashboard()
                pass
            else: 
                self.user_name = result[0][1]  
                self.user_email = self.email  
                self.clear_screen()  
                print("WORKING")
    
    #clear everything function
    def clear_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()
            
Motel_app = app()