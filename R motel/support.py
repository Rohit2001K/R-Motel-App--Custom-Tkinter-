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
    def login_user(self):
        cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (self.user, self.password))
        user_auth = cursor.fetchall()
        if user_auth:
            return user_auth
        else:
            return False

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
            cursor.execute('UPDATE rooms SET available=False WHERE room_no=%s', (room_no,))
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