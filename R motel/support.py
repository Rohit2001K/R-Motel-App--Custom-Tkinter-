import mysql.connector as ms
from datetime import date

#Mysql Connection
my_sql=ms.connect(host='localhost',user='',passwd='',database='test')
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