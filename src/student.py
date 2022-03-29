from connection import connect
class Student:
    def __init__(self,name,roll,branch,password):
        self.name=name
        self.roll=roll
        self.branch=branch
        self.password=password
    
    def login(self):
        conn = connect()
        cur = conn.cursor()
        query ='SELECT name,password from public."StudentData" where name=\''+self.name+'\';'
        cur.execute('SELECT name,password from public."StudentData" where name=\''+self.name+'\';')

        # display the PostgreSQL database server version
        data = cur.fetchone()
        
        if data[0]==self.name and data[1]==self.password:
            print('Logged in Successfully')
        else:
            print('Incorrect username or password')

       
	# close the communication with the PostgreSQL
        cur.close()

std = Student("Tharun","19308","CSED","tharun")
std.login()