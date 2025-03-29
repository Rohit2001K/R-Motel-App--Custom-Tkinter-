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
        self.tree.place(x=290.0, y=170.0, width=500.0, height=210.0)
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
        self.tree.place(x=280.0, y=170.0, width=520.0, height=210.0)
        for row in result:
            self.tree.insert("", "end", values=row)    



















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
Motel_app = staff_app(staff_window,"motel@stuff.come") 
staff_window.mainloop()










