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
        pass_req_button = Button(image=self.pass_req_img,borderwidth=0,highlightthickness=0,command=self.passwd_reset,relief="flat")
        pass_req_button.place(x=260.0,y=240.0,width=280.0,height=40.0)

        #PASSWORD RESET HISTORY
        self.pass_reset_img= PhotoImage(file=self.relative_to_assets("pass_res_history.png"))
        pass_reset_button = Button(image=self.pass_reset_img,borderwidth=0,highlightthickness=0,command=self.prev_reset_requests,relief="flat")
        pass_reset_button.place(x=574.0,y=240.0,width=280.0,height=40.0)

        #USER CHECK OUT
        #msg
        user_check_msg=canvas.create_text(467.0,302.0,anchor="nw",text="User Check Out",fill="#004B6A",font=("Bungee Regular", 20 * -1))

        #Process check out button
        self.process_check_img= PhotoImage(file=self.relative_to_assets("process_checkout_button.png"))
        process_checkout_button = Button(image=self.process_check_img,borderwidth=0,highlightthickness=0,command=self.user_check_out_page,relief="flat")
        process_checkout_button.place(x=260.0,y=348.0,width=280.0,height=40.0)

        #booking history
        self.booking_history_img = PhotoImage(file=self.relative_to_assets("booking_history_button.png"))
        booking_history_button = Button(image=self.booking_history_img, borderwidth=0, highlightthickness=0, command=self.booking_log, relief="flat")
        booking_history_button.place(x=574.0,y=348.0, width=280.0, height=40.0)

        #FOOD SECTION
        #msg
        food_msg=canvas.create_text(487.0,410.0,anchor="nw",text="Food/Meals",fill="#004B6A",font=("Bungee Regular", 20 * -1))

        #food menu
        self.food_menu_img = PhotoImage(file=self.relative_to_assets("food_menu_button.png"))
        food_menu_button = Button(image=self.food_menu_img, borderwidth=0, highlightthickness=0, command=self.food_menu, relief="flat")
        food_menu_button.place(x=260.0,y=456.0, width=280.0, height=40.0)

        #view order
        self.view_orders_img = PhotoImage(file=self.relative_to_assets("view_orders_button.png"))
        view_orders_button = Button(image=self.view_orders_img, borderwidth=0, highlightthickness=0, command=self.food_order_pages, relief="flat")
        view_orders_button.place(x=574, y=456, width=280.0, height=40.0)

        #order history
        self.order_history_img = PhotoImage(file=self.relative_to_assets("order_history_button.png"))
        order_history_button = Button(image=self.order_history_img, borderwidth=0, highlightthickness=0, command=self.food_order_history_page, relief="flat")
        order_history_button.place(x=260, y=520, width=280.0, height=40.0)

    #password reset request
    def passwd_reset(self):
        self.clear_screen() 
        self.background=canvas= Canvas(self.window,bg ="white",height = 600,width = 900,bd = 0,highlightthickness = 0,relief = "ridge") #intial white background
        canvas.place(x = 0, y = 0) #basic setup

        #left pannels 
        self.left_home_img= PhotoImage(file=self.relative_to_assets("account_l_panel.png"))
        left_home=canvas.create_image(92.0,305.0,image=self.left_home_img)

        #back button
        self.back_button(self.home)

        #heading img
        self.home_img = PhotoImage(file=self.relative_to_assets("password_reset_head.png"))
        home_heading= canvas.create_image(541.0,99.0,image=self.home_img)
        
        #tree back
        self.passwd_back_img= PhotoImage(file=self.relative_to_assets("food_order_status_back.png"))
        self.passwd_background= canvas.create_image(541.0,285.0,image=self.passwd_back_img)

        #tree view
        user=Staff_action(self.user_email)
        result=user.password_rest()
        columns = ("Sno.","User Email","Status","Created On")
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

        self.tree.heading("Sno.", text="Sno.")
        self.tree.heading("User Email", text="User Email")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Created On", text="Created On")

        self.tree.column("Sno.", width=50, anchor="center")
        self.tree.column("User Email", width=80, anchor="center")
        self.tree.column("Status", width=100, anchor="center")
        self.tree.column("Created On", width=150, anchor="center")
        self.tree.place(x=280.0, y=170.0, width=520.0, height=230.0)
        for row in result:
            self.tree.insert("", "end", values=row)
        #msg
        self.passwd_reset_msg=canvas.create_text(280.0,419.0,anchor="nw",text="Select pending request",fill="#004B6A",font=("Bungee Regular", 15 * -1))

        #accept button
        self.acc_img = PhotoImage(file=self.relative_to_assets("verify_and_accept_passwd.png"))
        self.acc_button = Button(image=self.acc_img,borderwidth=0,highlightthickness=0,command=self.user_info_fetch,relief="flat")
        self.acc_button.place(x=280.0,y=466.0,width=535.0,height=40.0)

        #cancel button
        self.cancel_img = PhotoImage(file=self.relative_to_assets("cancel_req.png"))
        self.cancel_button = Button(image=self.cancel_img,borderwidth=0,highlightthickness=0,command=self.cancel_passwd_reset,relief="flat")
        self.cancel_button.place(x=280.0,y=525.0,width=535.0,height=40.0)
    
    #cancel password reset request
    def cancel_passwd_reset(self):
        user=Staff_action(self.user_email)
        selected_item=self.tree.selection() 
        if selected_item:
            selected_item=self.tree.item(selected_item, "values")
            user_email = selected_item[1]
            status="cancelled"
            user.update_reset_request_status(user_email,self.user_email,status)
            self.passwd_reset()
            self.background.itemconfig(self.passwd_reset_msg,text="User reset request cancelled..", fill="green")
        else:
            self.background.itemconfig(self.passwd_reset_msg,text="Please select a user request to continue", fill="red")

    #accept and show user info for password reset
    def user_info_fetch(self):
        user=Staff_action(self.user_email)
        selected_item=self.tree.selection() 
        if selected_item:
            #removing 
            self.tree.place_forget()
            self.background.delete(self.passwd_background)
            self.acc_button.place_forget()
            self.cancel_button.place_forget()
            
            #back button
            self.back_button(self.passwd_reset)
            #msg
            self.background.itemconfig(self.passwd_reset_msg,text="Please verify the user's information and ensure it matches",fil='green')
            self.background.coords(self.passwd_reset_msg, 280,374)

            #user info
            selected_item=self.tree.item(selected_item, "values")
            self.reset_user_email = selected_item[1]
            result=user.user_account_info_fetch(self.reset_user_email)

            #fname
            fname=self.background.create_text(280.0,168.0,anchor="nw",text="First Name :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
            user_fname=self.background.create_text(477.0,168.0,anchor="nw",text=f"{result[0][0]}",fill="#004B6A",font=("Bungee Regular", 20 * -1))

            #lname
            lname=self.background.create_text(280.0,213.0,anchor="nw",text="Last Name :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
            user_lname=self.background.create_text(477.0,213.0,anchor="nw",text=f"{result[0][1]}",fill="#004B6A",font=("Bungee Regular", 20 * -1))
            
            #mobile
            mobile=self.background.create_text(280.0,259.0,anchor="nw",text="Mobile No :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
            user_mobile=self.background.create_text(477.0,259.0,anchor="nw",text=f"{result[0][2]}",fill="#004B6A",font=("Bungee Regular", 20 * -1))

            #email
            email=self.background.create_text(280.0,304.0,anchor="nw",text="EMail :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
            user_email=self.background.create_text(477.0,304.0,anchor="nw",text=f"{result[0][3]}",fill="#004B6A",font=("Bungee Regular", 20 * -1))

            #accept button
            self.acc_img = PhotoImage(file=self.relative_to_assets("verify_and_accept_passwd.png"))
            self.acc_button = Button(image=self.acc_img,borderwidth=0,highlightthickness=0,command=self.set_passwd_page,relief="flat")
            self.acc_button.place(x=280.0,y=426.0,width=535.0,height=40.0)

        else:
            self.background.itemconfig(self.passwd_reset_msg,text="Please select a user request to continue", fill="red")


    #set new password
    def set_passwd_page(self):
        self.clear_screen()
        self.background=canvas= Canvas(self.window,bg ="white",height = 600,width = 900,bd = 0,highlightthickness = 0,relief = "ridge") #intial white background
        canvas.place(x = 0, y = 0) #basic setup

        #left pannels 
        self.left_home_img= PhotoImage(file=self.relative_to_assets("account_l_panel.png"))
        left_home=canvas.create_image(92.0,305.0,image=self.left_home_img)

        #back button
        self.back_button(self.passwd_reset)

        #heading img
        self.home_img = PhotoImage(file=self.relative_to_assets("password_reset_head.png"))
        home_heading= canvas.create_image(541.0,99.0,image=self.home_img)

        #new password
        new_passwd_lable=canvas.create_text(265.0,234.0,anchor="nw",text="New Password:",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        self.passwd_img=PhotoImage(file=self.relative_to_assets("passwd_entry.png"))
        passwd_img = canvas.create_image(671.5,256.0,image=self.passwd_img)
        self.password1=Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0,font=(12))
        self.password1.place(x=523.0,y=242.0,width=297.0,height=26.0)

        #confim password
        confirm_passwd_lable=canvas.create_text(265.0,280.0,anchor="nw",text="confirm  Password :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        confirm_passwd_img = canvas.create_image(671.5,305.0,image=self.passwd_img)
        self.password2=Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0,font=(12))
        self.password2.place(x=523.0,y=293,width=297.0,height=26.0)

        #msg
        self.passwd_set_msg=canvas.create_text(265.0,336.0,anchor="nw",text="Enter a new password",fill="#004B6A",font=("Bungee Regular", 15 * -1))

        #submit button
        self.set_passwd_img= PhotoImage(file=self.relative_to_assets("set_new_pass.png"))
        set_new_passwd_button=Button(image=self.set_passwd_img,borderwidth=0,highlightthickness=0,command=self.set_new_passwd,relief="flat")
        set_new_passwd_button.place(x=265.0, y=400.0,width=564.0,height=40.0)

    #set password logical function
    def set_new_passwd(self):
        passwd1=self.password1.get()
        passwd2=self.password2.get()
        if not passwd1 or not passwd2:
            self.background.itemconfig(self.passwd_set_msg, text="Please fill both fields!", fill="red")
        elif passwd1!=passwd2:
            self.background.itemconfig(self.passwd_set_msg, text="Passwords must match!", fill="red")
        else:
            user=Staff_action(self.user_email)
            result=user.user_password_set(self.reset_user_email,passwd1)
            if result:
                status="completed"
                user.update_reset_request_status(self.reset_user_email,self.user_email,status)
                self.passwd_reset()
                self.background.itemconfig(self.passwd_reset_msg, text=f"Password Updated for {self.reset_user_email}", fill="green")  
            else:
                self.background.itemconfig(self.passwd_set_msg, text="Error in settting new password", fill="red")

    #previous reset requests
    def prev_reset_requests(self):
        self.clear_screen()
        self.background=canvas= Canvas(self.window,bg ="white",height = 600,width = 900,bd = 0,highlightthickness = 0,relief = "ridge") #intial white background
        canvas.place(x = 0, y = 0) #basic setup

        #left pannels 
        self.left_home_img= PhotoImage(file=self.relative_to_assets("account_l_panel.png"))
        left_home=canvas.create_image(92.0,305.0,image=self.left_home_img)

        #back button
        self.back_button(self.home)

        #heading img
        self.home_img = PhotoImage(file=self.relative_to_assets("all_reset_req_head.png"))
        home_heading= canvas.create_image(541.0,99.0,image=self.home_img)

        #tree back
        self.passwd_back_img= PhotoImage(file=self.relative_to_assets("food_order_status_back.png"))
        self.passwd_background= canvas.create_image(541.0,285.0,image=self.passwd_back_img)

        #tree
        user = Staff_action(self.user_email)
        result=user.previous_rest_request()

        columns = ("Sno.","User Email","Done By","Status","Created On")
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

        self.tree.heading("Sno.", text="Sno.")
        self.tree.heading("User Email", text="User Email")
        self.tree.heading("Done By", text="Done By")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Created On", text="Created On")

        self.tree.column("Sno.", width=30, anchor="center")
        self.tree.column("User Email", width=150, anchor="center")
        self.tree.column("Done By", width=150, anchor="center")
        self.tree.column("Status", width=80, anchor="center")
        self.tree.column("Created On", width=140, anchor="center")
        self.tree.place(x=280.0, y=170.0, width=520.0, height=230.0)
        for row in result:
            self.tree.insert("", "end", values=row)    

    def user_check_out_page(self):
        self.clear_screen()
        self.background=canvas= Canvas(self.window,bg ="white",height = 600,width = 900,bd = 0,highlightthickness = 0,relief = "ridge") #intial white background
        canvas.place(x = 0, y = 0) #basic setup

        #left pannels 
        self.left_home_img= PhotoImage(file=self.relative_to_assets("booking_l_panel.png"))
        left_home=canvas.create_image(92.0,305.0,image=self.left_home_img)

        #back button
        self.back_button(self.home)

        #heading img
        self.home_img = PhotoImage(file=self.relative_to_assets("active_booking_head.png"))
        home_heading= canvas.create_image(541.0,99.0,image=self.home_img)

        #tree back
        self.passwd_back_img= PhotoImage(file=self.relative_to_assets("active_booking_back.png"))
        self.passwd_background= canvas.create_image(541.0,285.0,image=self.passwd_back_img)

        #tree
        user=Staff_action(self.user_email)
        result=user.current_bookings()
        columns = ("Id","Email","RoomNo.", "Check In", "Check Out","Days","Price","Status")
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

        self.tree.heading("Id", text="Id")
        self.tree.heading("Email", text="Email")
        self.tree.heading("RoomNo.", text="RoomNo.")
        self.tree.heading("Check In", text="Check In")
        self.tree.heading("Check Out", text="Check Out")
        self.tree.heading("Days", text="Days")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Status", text="Status")

        self.tree.column("Id", width=40, anchor="center")
        self.tree.column("Email", width=80, anchor="center")
        self.tree.column("RoomNo.", width=50, anchor="center")
        self.tree.column("Check In", width=80, anchor="center")
        self.tree.column("Check Out", width=80, anchor="center")
        self.tree.column("Days", width=40, anchor="center")
        self.tree.column("Price", width=80, anchor="center")
        self.tree.column("Status", width=80, anchor="center")

        self.tree.tag_configure('overdue', foreground='red',background='yellow')
        self.tree.place(x=233.0, y=170.0, width=620.0, height=230.0)
        for row in result:
            if row[-1] == 'Overdue':
                self.tree.insert("", "end", values=row, tags=('overdue',))
            else:
                self.tree.insert("", "end", values=row)

        #msg
        self.check_out_msg=canvas.create_text(231.0,419.0,anchor="nw",text="Select room for check out",fill="#004B6A",font=("Bungee Regular", 15 * -1))

        #see user details button
        self.user_detail_img = PhotoImage(file=self.relative_to_assets("see_user_button.png"))
        self.see_user_button = Button(image=self.user_detail_img,borderwidth=0,highlightthickness=0,command=self.check_out_user_details,relief="flat")
        self.see_user_button.place(x=231.0,y=466.0,width=632.0,height=40.0)

        #check out button
        self.confirm_check_img = PhotoImage(file=self.relative_to_assets("confirm_check_out_button.png"))
        self.check_out_button = Button(image=self.confirm_check_img,borderwidth=0,highlightthickness=0,command=self.check_out,relief="flat")
        self.check_out_button.place(x=231.0,y=525.0,width=632.0,height=40.0)

    #user check out
    def check_out(self):
        selected_room = self.tree.selection() 
        if selected_room:
            booking_details=self.tree.item(selected_room, "values")
            id=booking_details[0]
            room_no=booking_details[2]
            user=Staff_action(self.user_email)
            result=user.check_out(id,room_no)
            if result==True:
                self.user_check_out_page()
                self.background.itemconfig(self.check_out_msg,text='Checkout complete. Thank you!', fill="green")
            else:
                self.background.itemconfig(self.check_out_msg,text='Error In Checking Out User...', fill="red")
        else:
            self.background.itemconfig(self.check_out_msg,text="Please select a room to continue", fill="red")

    #check out user details
    def check_out_user_details(self):
        selected_item = self.tree.selection()
        selected_item = self.tree.item(selected_item[0])
        values = selected_item["values"]
        user_email=values[1]
        if selected_item:
            #removing 
            self.tree.place_forget()
            self.background.delete(self.passwd_background)
            self.check_out_button.place_forget()
            self.see_user_button.place_forget()
            self.background.delete(self.check_out_msg)
            
            self.back_button(self.user_check_out_page)

            #user info fetch
            user=Staff_action(self.user_email)
            result=user.user_account_info_fetch(user_email)

            #fname
            fname=self.background.create_text(280.0,168.0,anchor="nw",text="First Name :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
            user_fname=self.background.create_text(477.0,168.0,anchor="nw",text=f"{result[0][0]}",fill="#004B6A",font=("Bungee Regular", 20 * -1))

            #lname
            lname=self.background.create_text(280.0,213.0,anchor="nw",text="Last Name :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
            user_lname=self.background.create_text(477.0,213.0,anchor="nw",text=f"{result[0][1]}",fill="#004B6A",font=("Bungee Regular", 20 * -1))
            
            #mobile
            mobile=self.background.create_text(280.0,259.0,anchor="nw",text="Mobile No :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
            user_mobile=self.background.create_text(477.0,259.0,anchor="nw",text=f"{result[0][2]}",fill="#004B6A",font=("Bungee Regular", 20 * -1))

            #email
            email=self.background.create_text(280.0,304.0,anchor="nw",text="EMail :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
            user_email=self.background.create_text(477.0,304.0,anchor="nw",text=f"{result[0][3]}",fill="#004B6A",font=("Bungee Regular", 20 * -1))


        else:
            self.background.itemconfig(self.check_out_msg,text="Please select a room to continue", fill="red")

    def booking_log(self):
        self.clear_screen()
        self.background=canvas= Canvas(self.window,bg ="white",height = 600,width = 900,bd = 0,highlightthickness = 0,relief = "ridge") #intial white background
        canvas.place(x = 0, y = 0) #basic setup

        #left pannels 
        self.left_home_img= PhotoImage(file=self.relative_to_assets("booking_l_panel.png"))
        left_home=canvas.create_image(92.0,305.0,image=self.left_home_img)

        #back button
        self.back_button(self.home)

        #heading img
        self.home_img = PhotoImage(file=self.relative_to_assets("booking_history_head.png"))
        home_heading= canvas.create_image(541.0,99.0,image=self.home_img)

        #tree back
        self.passwd_back_img= PhotoImage(file=self.relative_to_assets("active_booking_back.png"))
        self.passwd_background= canvas.create_image(541.0,285.0,image=self.passwd_back_img)

        #tree
        user=Staff_action(self.user_email)
        result=user.booking_history()
        columns = ("Id","Email","RoomNo.", "Check In", "Check Out","Days","Price","Status")
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

        self.tree.heading("Id", text="Id")
        self.tree.heading("Email", text="Email")
        self.tree.heading("RoomNo.", text="RoomNo.")
        self.tree.heading("Check In", text="Check In")
        self.tree.heading("Check Out", text="Check Out")
        self.tree.heading("Days", text="Days")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Status", text="Status")

        self.tree.column("Id", width=40, anchor="center")
        self.tree.column("Email", width=80, anchor="center")
        self.tree.column("RoomNo.", width=50, anchor="center")
        self.tree.column("Check In", width=80, anchor="center")
        self.tree.column("Check Out", width=80, anchor="center")
        self.tree.column("Days", width=40, anchor="center")
        self.tree.column("Price", width=80, anchor="center")
        self.tree.column("Status", width=80, anchor="center")
        for row in result:
            self.tree.insert("", "end", values=row)

        self.tree.tag_configure('overdue', foreground='red',background='yellow')
        self.tree.place(x=233.0, y=170.0, width=620.0, height=230.0)

    def food_menu(self):
        self.clear_screen()
        self.background=canvas= Canvas(self.window,bg ="white",height = 600,width = 900,bd = 0,highlightthickness = 0,relief = "ridge") #intial white background
        canvas.place(x = 0, y = 0) #basic setup

        #left pannels 
        self.left_home_img= PhotoImage(file=self.relative_to_assets("food_l_panel.png"))
        left_home=canvas.create_image(92.0,305.0,image=self.left_home_img)

        #back button
        self.back_button(self.home)

        #heading img
        self.home_img = PhotoImage(file=self.relative_to_assets("food_menu_head.png"))
        home_heading= canvas.create_image(541.0,99.0,image=self.home_img)

        #tree back
        self.passwd_back_img= PhotoImage(file=self.relative_to_assets("food_menu_back.png"))
        self.passwd_background= canvas.create_image(541.0,285.0,image=self.passwd_back_img)

        #tree
        user=Staff_action(self.user_email)
        result=user.show_food_items()

        columns = ("Id","Name","Price", "Availability")
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
        self.tree.heading("Id", text="Id")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Availability", text="Availability")

        self.tree.column("Id", width=40, anchor="center")
        self.tree.column("Name", width=100, anchor="center")
        self.tree.column("Price", width=50, anchor="center")
        self.tree.column("Availability", width=100, anchor="center")
        for row in result:
            self.tree.insert("", "end", values=row)

        self.tree.tag_configure('overdue', foreground='red',background='yellow')
        self.tree.place(x=273.0, y=170.0, width=535.0, height=230.0)


        #msg
        self.food_menu_msg=canvas.create_text(274.0,419.0,anchor="nw",text="change food item availability or add new item",fill="#004B6A",font=("Bungee Regular", 15 * -1))

        #add new item button 
        self.add_new_img = PhotoImage(file=self.relative_to_assets("add_new_item_button.png"))
        self.add_new_item_button = Button(image=self.add_new_img,borderwidth=0,highlightthickness=0,command=self.add_new_food,relief="flat")
        self.add_new_item_button.place(x=270.0,y=467.0,width=544.0,height=40.0)

        #item status buttons
        self.make_item_avi_img = PhotoImage(file=self.relative_to_assets("make_item_avi_button.png"))
        self.make_item_avi_button = Button(image=self.make_item_avi_img,borderwidth=0,highlightthickness=0,command=lambda:self.change_food_avi('available'),relief="flat")
        self.make_item_avi_button.place(x=270.0,y=527.0,width=260.0,height=40.0)

        self.make_item_out_img = PhotoImage(file=self.relative_to_assets("make_item_out_button.png"))
        self.make_item_out_button = Button(image=self.make_item_out_img,borderwidth=0,highlightthickness=0,command=lambda:self.change_food_avi('out of stock'),relief="flat")
        self.make_item_out_button.place(x=558.0,y=527.0,width=260.0,height=40.0)

    #change food item status
    def change_food_avi(self,status):
        user=Staff_action(self.user_email)
        selected_item=self.tree.selection() 
        if selected_item:
            selected_item=self.tree.item(selected_item, "values")
            food_name=selected_item[1]
            action=user.food_item_status(status,food_name)
            if not action:
                self.background.itemconfig(self.food_menu_msg,text="ERROR Please Contact Admin", fill="red")
            else:
                self.food_menu()
                self.background.itemconfig(self.food_menu_msg,text="Food item availability status updated", fill="green")
        else:
            self.background.itemconfig(self.food_menu_msg,text="Please select a item", fill="red")

    #add new food item
    def add_new_food(self):
        user=Staff_action(self.user_email)
        #removing 
        self.tree.place_forget()
        self.background.delete(self.passwd_background)
        self.make_item_avi_button.place_forget()
        self.add_new_item_button.place_forget()
        self.make_item_out_button.place_forget()
            
        #back button
        self.back_button(self.food_menu)

        #form
        #food name
        food_name=self.background.create_text(274.0,220.0,anchor="nw",text="Food name :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        self.name_entry_img=PhotoImage(file=self.relative_to_assets("food_entry_img.png"))
        name_entry_img_background=self.background.create_image(634.5,242.0,image=self.name_entry_img)
        self.food_name = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0,font=(10))
        self.food_name.place(x=460.0,y=228.0,width=349.0,height=26.0)

        #price
        food_price=self.background.create_text(274.0,266.0,anchor="nw",text="Price :",fill="#004B6A",font=("Bungee Regular", 20 * -1))
        self.price_entry_img=PhotoImage(file=self.relative_to_assets("food_entry_img.png"))
        price_entry_img_background=self.background.create_image(634.5,288.0,image=self.price_entry_img)
        self.food_price = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0,font=(10))
        self.food_price.place(x=460.0,y=274.0,width=349.0,height=26.0)

        #msg
        self.background.itemconfig(self.food_menu_msg,text="Fill above details to list new item",fil='#004B6A')
        self.background.coords(self.food_menu_msg,274.0,325.0,)

        #add new item button 
        self.add_new_img = PhotoImage(file=self.relative_to_assets("add_new_item_button.png"))
        add_new_item_button = Button(image=self.add_new_img,borderwidth=0,highlightthickness=0,command=self.add_new_item,relief="flat")
        add_new_item_button.place(x=274.0,y=366.0,width=544.0,height=40.0)

    #add new food item logical function
    def add_new_item(self):
        user=Staff_action(self.user_email)
        food_name=self.food_name.get()
        food_price=self.food_price.get()
        if not food_name or not food_price:
            self.background.itemconfig(self.food_menu_msg,text='Please enter the food name and price', fill="red")
        else:
            action=user.list_new_item(food_name,food_price)
            if action==False:
                self.background.itemconfig(self.food_menu_msg,text='Please recheck the name and price', fill="red")
            else:
                self.food_menu()
                self.background.itemconfig(self.food_menu_msg,text='New item has been listed', fill="green")

    #food orders
    def food_order_pages(self):
        self.clear_screen()
        self.background=canvas= Canvas(self.window,bg ="white",height = 600,width = 900,bd = 0,highlightthickness = 0,relief = "ridge") #intial white background
        canvas.place(x = 0, y = 0) #basic setup

        #left pannels 
        self.left_home_img= PhotoImage(file=self.relative_to_assets("food_l_panel.png"))
        left_home=canvas.create_image(92.0,305.0,image=self.left_home_img)

        #back button
        self.back_button(self.home)

        #heading img
        self.home_img = PhotoImage(file=self.relative_to_assets("food_orders.png"))
        home_heading= canvas.create_image(541.0,99.0,image=self.home_img)

        #tree back
        self.passwd_back_img= PhotoImage(file=self.relative_to_assets("food_menu_back.png"))
        self.passwd_background= canvas.create_image(541.0,285.0,image=self.passwd_back_img)

        
        #msg
        self.food_order_msg=canvas.create_text(274.0,419.0,anchor="nw",text="change food orders status",fill="#004B6A",font=("Bungee Regular", 15 * -1))

        #item status buttons
        self.prepar_img=PhotoImage(file=self.relative_to_assets("preparing_button.png"))
        preparing_button=Button(image=self.prepar_img,borderwidth=0,highlightthickness=0,command=lambda:self.change_food_avi('available'),relief="flat")
        preparing_button.place(x=274.0,y=467.0,width=260.0,height=40.0)

        self.deliv_img=PhotoImage(file=self.relative_to_assets("delivery_button.png"))
        deliverd_button=Button(image=self.deliv_img,borderwidth=0,highlightthickness=0,command=lambda:self.change_food_avi('available'),relief="flat")
        deliverd_button.place(x=558.0,y=467.0,width=260.0,height=40.0)

        self.cancel_img=PhotoImage(file=self.relative_to_assets("cancel_button.png"))
        cancel_button=Button(image=self.cancel_img,borderwidth=0,highlightthickness=0,command=lambda:self.change_food_avi('available'),relief="flat")
        cancel_button.place(x=274.0,y=527.0,width=260.0,height=40.0)







    def food_order_history_page(self):
        self.clear_screen()
        self.background=canvas= Canvas(self.window,bg ="white",height = 600,width = 900,bd = 0,highlightthickness = 0,relief = "ridge") #intial white background
        canvas.place(x = 0, y = 0) #basic setup

        #left pannels 
        self.left_home_img= PhotoImage(file=self.relative_to_assets("food_l_panel.png"))
        left_home=canvas.create_image(92.0,305.0,image=self.left_home_img)

        #back button
        self.back_button(self.home)

        #heading img
        self.home_img = PhotoImage(file=self.relative_to_assets("food_order_history_head.png"))
        home_heading= canvas.create_image(541.0,99.0,image=self.home_img)

        #tree back
        self.passwd_back_img= PhotoImage(file=self.relative_to_assets("food_menu_back.png"))
        self.passwd_background= canvas.create_image(541.0,285.0,image=self.passwd_back_img)

        #tree
        user=Staff_action(self.user_email)
        result=user.previous_food_requests()

        columns = ("OrderId","room_no","food_id","food_name","quantity","Price","status")
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
        self.tree.heading("OrderId", text="OrderId")
        self.tree.heading("room_no", text="room_no")
        self.tree.heading("food_id", text="food_id")
        self.tree.heading("food_name", text="food_name")
        self.tree.heading("quantity", text="quantity")
        self.tree.heading("Price", text="Price")
        self.tree.heading("status", text="status")

        self.tree.column("OrderId", width=50, anchor="center")
        self.tree.column("room_no", width=50, anchor="center")
        self.tree.column("food_id", width=50, anchor="center")
        self.tree.column("food_name", width=100, anchor="center")
        self.tree.column("quantity", width=50, anchor="center")
        self.tree.column("Price", width=50, anchor="center")
        self.tree.column("status", width=100, anchor="center")
        for row in result:
            self.tree.insert("", "end", values=row)

        self.tree.tag_configure('overdue', foreground='red',background='yellow')
        self.tree.place(x=273.0, y=170.0, width=535.0, height=230.0)









    #back button
    def back_button(self, command=None):
        self.back_button_img = PhotoImage(file=self.relative_to_assets("back_button.png"))
        back_button = Button(image=self.back_button_img, borderwidth=0, highlightthickness=0, command=command, relief="flat")
        back_button.place(x=209.0, y=18.0, width=45.0, height=48.0)
        
    #clear everything function
    def clear_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()
            


staff_window = Tk()  
Motel_app = staff_app(staff_window,"motel@staff.com") 
staff_window.mainloop()










