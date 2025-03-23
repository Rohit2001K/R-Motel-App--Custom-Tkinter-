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
    def __init__(self,email):
        self.window = Tk()
        self.window.geometry("900x600")
        self.window.title("R Motel Staff Window")
        self.home()
        self.window.resizable(False, False)
        self.window.mainloop()
        self.user_email=email

    #class
    @staticmethod
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    #dashboard
    def home(self):
        user = Staff_action(self.user_email)
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

        #msg
        home_msg=canvas.create_text(306.0,138.0,anchor="nw",text=f"Welcome  GT to Staff Dashboard.",fill="#004B6A",font=("Bungee Regular", 20 * -1))

        #sections
        #PASSWORD SECTION
        pass_msg=canvas.create_text(390.0,195.0,anchor="nw",text="Password Reset Requests",fill="#004B6A",font=("Bungee Regular", 20 * -1))

        #PASSWORD RESET REQUEST
        pass_req_img= PhotoImage(file=self.relative_to_assets("password_request_button.png"))
        pass_req_img.image=pass_req_img
        pass_req_button = Button(image=pass_req_img,borderwidth=0,highlightthickness=0,command=lambda: print("PASS REQ"),relief="flat")
        pass_req_button.place(x=260.0,y=240.0,width=280.0,height=40.0)

        #PASSWORD RESET HISTORY
        pass_reset_img= PhotoImage(file=self.relative_to_assets("pass_res_history.png"))
        pass_reset_img.image=pass_reset_img
        pass_reset_button = Button(image=pass_reset_img,borderwidth=0,highlightthickness=0,command=lambda: print("PASS RESET"),relief="flat")
        pass_reset_button.place(x=574.0,y=240.0,width=280.0,height=40.0)

        #USER CHECK OUT
        #msg
        user_check_msg=canvas.create_text(467.0,302.0,anchor="nw",text="User Check Out",fill="#004B6A",font=("Bungee Regular", 20 * -1))

        #Process check out button
        process_check_img= PhotoImage(file=self.relative_to_assets("process_checkout_button.png"))
        process_check_img.image=process_check_img
        process_checkout_button = Button(image=process_check_img,borderwidth=0,highlightthickness=0,command=lambda: print("process_checkout_button"),relief="flat")
        process_checkout_button.place(x=260.0,y=348.0,width=280.0,height=40.0)

        #booking history
        booking_history_img = PhotoImage(file=self.relative_to_assets("booking_history_button.png"))
        booking_history_img.image = booking_history_img
        booking_history_button = Button(image=booking_history_img, borderwidth=0, highlightthickness=0, command=lambda: print("booking_history_button"), relief="flat")
        booking_history_button.place(x=574.0,y=348.0, width=280.0, height=40.0)

        #FOOD SECTION
        #msg
        food_msg=canvas.create_text(487.0,410.0,anchor="nw",text="Food/Meals",fill="#004B6A",font=("Bungee Regular", 20 * -1))

        #food menu
        food_menu_img = PhotoImage(file=self.relative_to_assets("food_menu_button.png"))
        food_menu_img.image = food_menu_img
        food_menu_button = Button(image=food_menu_img, borderwidth=0, highlightthickness=0, command=lambda: print("food_menu_button"), relief="flat")
        food_menu_button.place(x=260.0,y=456.0, width=280.0, height=40.0)

        #view order
        view_orders_img = PhotoImage(file=self.relative_to_assets("view_orders_button.png"))
        view_orders_img.image = view_orders_img
        view_orders_button = Button(image=view_orders_img, borderwidth=0, highlightthickness=0, command=lambda: print("view_orders_button"), relief="flat")
        view_orders_button.place(x=574, y=456, width=280.0, height=40.0)

        #order history
        order_history_img = PhotoImage(file=self.relative_to_assets("order_history_button.png"))
        order_history_img.image = order_history_img
        order_history_button = Button(image=order_history_img, borderwidth=0, highlightthickness=0, command=lambda: print("order_history_button"), relief="flat")
        order_history_button.place(x=260, y=520, width=280.0, height=40.0)














