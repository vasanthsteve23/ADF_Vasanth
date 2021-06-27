import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="mettur@123",database="sample")

mycursor=mydb.cursor()

mycursor.execute("select * from employee")

myresult=mycursor.fetchall()

for db in myresult:
    print(db)

fname=input("Enter First name ")
mname=input("Enter middle name ")
lname=input("Enter last name ")
dob=input("Enter DOB ")
gender=input("Enter gender ")
nation=input("Enter Nationality ")
city=input("Enter city ")
state=input("Enter state ")
pin=int(input("Enter pincode "))
qual=input("Enter qualification ")
salary=float(input("Enter salary "))
pan=input("Enter PAN ")