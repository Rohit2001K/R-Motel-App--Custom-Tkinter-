import mysql.connector as ms
from datetime import date

#Mysql Connection
my_sql=ms.connect(host='localhost',user='root',passwd='1030',database='test')
if my_sql.is_connected():
    cursor=my_sql.cursor()

#user class
class User_actions:
 
    def __init__(self, user=None, password=None):
        self.user = user
        self.password = password

    #login user
    def login_user(self,email,password):
        cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email,password))
        user_auth = cursor.fetchall()
        if user_auth:
            return user_auth
        else:
            return False
    
    #password for hashing
    def get_passwd(self, email):
        cursor.execute("SELECT password FROM users WHERE email=%s", (email,))
        user_auth = cursor.fetchone()
        
        if user_auth:
            return user_auth[0] 
        else:
            return None

#PASSWORD RESET REQUEST SECTON
     
    #user password reset
    def password_reset(self, email):
        pending_request = self.check_previous_request(email)
        user_exsist=self.check_user_exsist(email)
        if pending_request:
            return "pending request"
        elif not user_exsist:
            return "user_exsist_false"
        else:
            try:
                cursor.execute("INSERT INTO password_reset_requests (email) VALUES (%s)", (email,))
                my_sql.commit()
                return "done"
            except:
                return "error"

    #check if user has submitted any request before
    def check_previous_request(self,email):
        cursor.execute('SELECT * FROM password_reset_requests where email=%s and request_status="pending"',(email,))
        result=cursor.fetchall()
        if result:
            return True
        return False
    
    #checking if requested user exsist or not
    def check_user_exsist(self,email):
        cursor.execute("SELECT email FROM users Where email=%s",(email,))
        result=cursor.fetchall()
        if result:
            return True
        return False
    
    #UserSing Up
    def create_user(self,fname,lname,mno,email,password):
        try:
            user_exist=self.check_user_exsist(email)
            if user_exist:
                return False
            else:
                cursor.execute('INSERT INTO Users (fname, lname, mobile, email, password) VALUES (%s, %s, %s, %s, %s)', (fname, lname, mno, email, password))
                result=my_sql.commit()
                return True
        except:
            return False 
        
#USER ACCOUNT
    def user_account(self,email):
        cursor.execute('select * from users where email=%s',(email,))
        result=cursor.fetchall()
        return result

    #fetching user total spends on room booking        
    def user_spends(self,email):
        #room booking total 
        cursor.execute('select price from bookings where email=%s',(email,))   
        room_booking_price=cursor.fetchall()
        total_room_price=0
        for i in room_booking_price:
            for j in i:
                total_room_price+=int(j)
        #food total
        return total_room_price   
    
    #user account info fetching
    def account_info_fetch(self,email):
        cursor.execute('select fname,lname,mobile,email from users where email=%s',(email,))
        result=cursor.fetchall()
        return result
    
    #updating user account info without password
    def user_account_update(self,email,fname,lname,mobile):
        try:
            cursor.execute('UPDATE users SET fname=%s, lname=%s, mobile=%s WHERE email=%s', (fname, lname, mobile, email))
            my_sql.commit()
            return True
        except:
            return False
        
    #updating user account password
    def user_account_password_update(self,email,passwd):
        try:
            cursor.execute('UPDATE users SET password=%s where email=%s', (passwd, email,))
            my_sql.commit()
            return True
        except:
            return False
    
#ROOM BOOKING
    #showing all available room to user
    def room_booking(self):
        cursor.execute('select room_no,beds,price from Rooms where available=True')
        result=cursor.fetchall()
        return result    

    #fetching room prices
    def price_fetch(self,room_no):
        cursor.execute('select price from rooms where room_no=%s',(room_no,))
        result=cursor.fetchall()
        result=result[0][0]
        return result
    
    #making booked room unavailable and insert booking data into DBMS
    def room_booking_conform(self,email, room_no, check_in_date, check_out_date, days,price):
        try:
            cursor.execute('UPDATE rooms SET available=False,booked=True WHERE room_no=%s', (room_no,))
            my_sql.commit()
            cursor.execute('INSERT INTO bookings (email, room_no, check_in, check_out, days,price) VALUES (%s, %s, %s, %s, %s,%s)',(email, room_no, check_in_date, check_out_date, days,price))
            my_sql.commit()
        except :
            print("Error in inserting:")

    #User booking history    
    def user_booking_history(self,email):
        cursor.execute('select room_no,check_in,check_out,days,price from bookings where email=%s',(email,))
        result=cursor.fetchall()
        return result

#Food section
    #show food items to user
    def food_items_fetch(self):
        cursor.execute('select * from food_items where availability="available"')
        result=cursor.fetchall()
        return result
    
    #food order main function    
    def food_order(self, email, food_id, food_name,price,quantity):
        room_no = self.pending_checkout(email)
        if room_no:
            user = self.user_account(email)
            user_id = user[0][0]
            room_no = room_no[0] 
            try:
                cursor.execute('INSERT INTO orders (user_id, room_no, food_id, food_name, price, quantity) VALUES (%s, %s, %s, %s, %s, %s)', (user_id, room_no, food_id, food_name, price, quantity))
                my_sql.commit() 
                return True
            except: 
                return False
        else:
            return False
        
    #pending checkout to fetch user room no  
    def pending_checkout(self, email):
        cursor.execute("""
            SELECT room_no
            FROM bookings
            WHERE email = %s AND check_out_status = 'Pending'
            ORDER BY booking_id DESC
            LIMIT 1
        """, (email,))
        result = cursor.fetchone()  
        return result
    
    #user food order status
    def order_status_check(self,email):
        uid=self.user_account(email)
        uid=uid[0][0]
        cursor.execute('select order_id,room_no,food_name,quantity,price,status from orders where user_id=%s',(uid,))
        result=cursor.fetchall()
        return result

#staff dashboard
class Staff_action:
    def __init__(self,email):
        self.email=email

    def staff_info(self):
        cursor.execute('SELECT fname FROM users where email=%s',(self.email,))
        result=cursor.fetchone()
        return result[0]

#USER PASSWORD RESET REQUEST FUNCTIONS       
    #password_reset tree data fetch
    def password_rest(self):
        try:
            cursor.execute("select sno,email,request_status,request_time from password_reset_requests where request_status='pending'")
            result=cursor.fetchall()
            return result
        except:
            return False
        
    #user data fetch after selecting user from tree      
    def user_account_info_fetch(self,email):
        cursor.execute('select fname,lname,mobile,email from users where email=%s',(email,))
        result=cursor.fetchall()
        return result
    #setting user password (updating users table) 
    def user_password_set(self,email,passwd):
        try:
            cursor.execute('update users set password=%s where email=%s',(passwd,email,))
            my_sql.commit()
            return True
        except:
            my_sql.rollback()
            return False
    #Updating status 
    def update_reset_request_status(self,user_email,staff_email,status):
        try:
            cursor.execute('update password_reset_requests set request_status=%s ,staff_member_email=%s where email=%s',(status,staff_email,user_email,))
            my_sql.commit()
            return True
        except:
            my_sql.rollback()
            return False
    #fetching previous password reset requestes
    def previous_rest_request(self):
        cursor.execute("select sno,email,staff_member_email,request_status,request_time from password_reset_requests where request_status!='pending'")
        result=cursor.fetchall()
        return result
    
        #checking if requested user exsist or not
    def check_user_exsist(self,email):
        cursor.execute("SELECT email FROM users Where email=%s",(email,))
        result=cursor.fetchall()
        if result:
            return True
        return False
    #create staff account
    def create_staff_user(self,fname,lname,mno,email,password,type):
        try:
            user_exist=self.check_user_exsist(email)
            if user_exist:
                return False
            else:
                cursor.execute('INSERT INTO users (fname,lname,mobile,staff_member, email, password) VALUES(%s, %s, %s,%s, %s, %s)', (fname, lname, mno,type, email, password))
                result=my_sql.commit()
                return True
        except:
            return False 

#booking
    def current_bookings(self):
        today = date.today()  
        cursor.execute("""
            SELECT booking_id, email, room_no, check_in, check_out, days, price,
                CASE
                    WHEN check_out <= %s AND check_out_status != 'Completed' THEN 'Overdue'
                    ELSE check_out_status
                END AS status
            FROM bookings
            WHERE check_out_status != 'Completed'
        """, (today,))
        result = cursor.fetchall()
        return result

    def room_price_fetch(self,room_no):
        cursor.execute("SELECT price from rooms where room_no=%s",(room_no,))
        result=cursor.fetchone()
        return result

    def booking_history(self):
        cursor.execute('SELECT booking_id,email,room_no,check_in,check_out,days,price,scheduled_check_out FROM bookings where check_out_status="Completed"')
        result = cursor.fetchall()
        return result

    def check_out(self,id,room_no,price,check_out_date,original_check_out):
        try:
            cursor.execute('update bookings set check_out_status="Completed" ,check_out=%s,scheduled_check_out=%s where booking_id=%s',(check_out_date,original_check_out,id,))
            cursor.execute('UPDATE rooms SET available=True,booked=False WHERE room_no=%s', (room_no,))
            cursor.execute('update bookings set price=%s where room_no=%s',(price,room_no,))
            my_sql.commit()
            return True
        except Exception as e:
            my_sql.rollback()  
            print(f"Error occurred: {e}")
            return False
    
    #room setting
    def room_setting(self):
        cursor.execute('select room_no,beds,price,available from Rooms where booked=False')
        result=cursor.fetchall()
        return result   

    #changing room availability
    def room_availability_status(self,room_no,status):
        try:
            cursor.execute('update rooms set available=%s where room_no=%s',(status,room_no,))
            my_sql.commit()
            return True
        except:
            return False




#FOOD SECTION
#showing all food items
    def show_food_items(self):
        cursor.execute('select * from food_items')
        result=cursor.fetchall()
        return result
#adding new food iteam into menu 
    def list_new_item(self,name,price):
        try:
            cursor.execute('insert into food_items (name,price) values (%s,%s)',(name,price,))
            my_sql.commit()
            return True
        except:
            return False
#updating food iteam availablity status  
    def food_item_status(self,status,name):
        try:
            cursor.execute('UPDATE food_items SET availability = %s WHERE name = %s', (status, name))
            my_sql.commit()
            return True
        except:
            return False
#fetching food requsets with pending status
    def food_req(self):
        cursor.execute('select order_id,room_no,food_id,food_name,quantity,price,status from orders where status!="delivered" and status!="cancelled"')
        result=cursor.fetchall()
        return result
    
#fetching delivered and cancelled food requests
    def previous_food_requests(self):
        cursor.execute('select order_id,room_no,food_id,food_name,quantity,price,status from orders where status!="pending" && status!="preparing"')
        result=cursor.fetchall()
        return result

    def food_req_status(self,status,id):
        try:
            cursor.execute('update orders set status=%s where order_id=%s',(status,id,))
            my_sql.commit()
            return True
        except:
            return False