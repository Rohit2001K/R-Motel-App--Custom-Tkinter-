from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,ttk
from support import User_actions
from tkinter import *
import re
import datetime
from support import Staff_action

OUTPUT_PATH = Path(__file__).parent  # Script directory
ASSETS_PATH = OUTPUT_PATH / "assets" / "staff assets"

class staff_app:
    def __init__(self,window,email):
        self.window =window
        self.window.geometry("900x600")
        self.window.title("R Motel Staff Window")
        self.window.resizable(False, False)
        self.user_email=email
        self.home()

    #class
    @staticmethod
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    #dashboard
    def home(self):
        self.background=canvas= Canvas(self.window,bg ="white",height = 600,width = 900,bd = 0,highlightthickness = 0,relief = "ridge") #intial white background
        canvas.place(x = 0, y = 0) #basic setup

        #left panel
        self.left_home_img= PhotoImage(file=self.relative_to_assets("home_left_img.png"))
        left_home=canvas.create_image(92.0,305.0,image=self.left_home_img)

        #heading
        self.home_img = PhotoImage(file=self.relative_to_assets("home_page_head.png"))
        home_heading= canvas.create_image(512.0,88.0,image=self.home_img)

        #msg
        home_msg=canvas.create_text(306.0,138.0,anchor="nw",text=f"Welcome  GT to Staff Dashboard.",fill="#004B6A",font=("Bungee Regular", 20 * -1))

        #sections
        #PASSWORD SECTION
        pass_msg=canvas.create_text(390.0,195.0,anchor="nw",text="Password Reset Requests",fill="#004B6A",font=("Bungee Regular", 20 * -1))

        #PASSWORD RESET REQUEST
        self.pass_req_img= PhotoImage(file=self.relative_to_assets("password_request_button.png"))
        pass_req_button = Button(image=self.pass_req_img,borderwidth=0,highlightthickness=0,command=lambda: print("PASS REQ"),relief="flat")
        pass_req_button.place(x=260.0,y=240.0,width=280.0,height=40.0)

        #PASSWORD RESET HISTORY
        self.pass_reset_img= PhotoImage(file=self.relative_to_assets("pass_res_history.png"))
        pass_reset_button = Button(image=self.pass_reset_img,borderwidth=0,highlightthickness=0,command=lambda: print("PASS RESET"),relief="flat")
        pass_reset_button.place(x=574.0,y=240.0,width=280.0,height=40.0)

        #USER CHECK OUT
        #msg
        user_check_msg=canvas.create_text(467.0,302.0,anchor="nw",text="User Check Out",fill="#004B6A",font=("Bungee Regular", 20 * -1))

        #Process check out button
        self.process_check_img= PhotoImage(file=self.relative_to_assets("process_checkout_button.png"))
        process_checkout_button = Button(image=self.process_check_img,borderwidth=0,highlightthickness=0,command=lambda: print("process_checkout_button"),relief="flat")
        process_checkout_button.place(x=260.0,y=348.0,width=280.0,height=40.0)

        #booking history
        self.booking_history_img = PhotoImage(file=self.relative_to_assets("booking_history_button.png"))
        booking_history_button = Button(image=self.booking_history_img, borderwidth=0, highlightthickness=0, command=lambda: print("booking_history_button"), relief="flat")
        booking_history_button.place(x=574.0,y=348.0, width=280.0, height=40.0)

        #FOOD SECTION
        #msg
        food_msg=canvas.create_text(487.0,410.0,anchor="nw",text="Food/Meals",fill="#004B6A",font=("Bungee Regular", 20 * -1))

        #food menu
        self.food_menu_img = PhotoImage(file=self.relative_to_assets("food_menu_button.png"))
        food_menu_button = Button(image=self.food_menu_img, borderwidth=0, highlightthickness=0, command=lambda: print("food_menu_button"), relief="flat")
        food_menu_button.place(x=260.0,y=456.0, width=280.0, height=40.0)

        #view order
        self.view_orders_img = PhotoImage(file=self.relative_to_assets("view_orders_button.png"))
        view_orders_button = Button(image=self.view_orders_img, borderwidth=0, highlightthickness=0, command=lambda: print("view_orders_button"), relief="flat")
        view_orders_button.place(x=574, y=456, width=280.0, height=40.0)

        #order history
        self.order_history_img = PhotoImage(file=self.relative_to_assets("order_history_button.png"))
        order_history_button = Button(image=self.order_history_img, borderwidth=0, highlightthickness=0, command=lambda: print("order_history_button"), relief="flat")
        order_history_button.place(x=260, y=520, width=280.0, height=40.0)














