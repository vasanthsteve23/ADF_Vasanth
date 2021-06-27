import mysql.connector

class SQLFILE:
    def insert(self,tup1):
        mydb=mysql.connector.connect(host="localhost",user="root",password="mettur@123",database="adfday5")

        mycursor=mydb.cursor()

        sqlform="Insert into request_info (fname,mname,lname,dob,gender,nationality,city,state,pin,qualification," \
                "salary,req_date,pan) values (%d,%s,%s,%s,%s,%s,%s,%s,%s,%d,%s,%d,%s,%s)"

        mycursor.execute(sqlform,self.tup1)

        mydb.commit()