import mysql.connector
import datetime as dt
from datetime import date
import re
import json
import logging
import config as cfg

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

host1 = cfg.information["host"]
user1 = cfg.information["user"]
pswd = cfg.information["password"]
db=cfg.information["database"]

mydb=mysql.connector.connect(host=host1,user=user1,password=pswd,database=db)

mycursor=mydb.cursor()

class Validation:
    def calculateage(self,dob):
        today=date.today()
        age=today.year-dob.year-((today.month,today.day)<(dob.month,dob.day))
        logging.debug("Calculation of age '{}'".format(age))
        return age

    def ageValidate(self,age,gender):
        gender=gender.lower()
        if gender=='male' and age<21:
            logging.debug("Age invalid for this men")
            return "age is less than 21"
        elif gender=='female' and age<18:
            logging.debug("Age invalid for this women")
            return "age is less than 18"
        else:
            logging.debug("User eligible")
            return "Eligible"


    def nationValid(self,nation):
        nation=nation.lower()
        if nation=='indian' or nation=='american':
            logging.debug("User eligible")
            return "Eligible"
        else:
            logging.debug("Nation invalid for this user")
            return "Not Eligible"

    def stateValid(self,state):
        state=state.lower()
        state=state.replace(" ","")
        states=["andhra pradesh","arunachal pradesh","assam","bihar","chhatisgarh",
                "karnataka","madhyapradesh","odisha","tamilnadu","telangana","westbengal"]
        if state in states:
            logging.debug("User eligible")
            return "Eligible"
        else:
            logging.debug(" State is not eligible for this user")
            return state+" State is not eligible"

    def salaryValid(self,salary):
        if salary>=10000 and salary<=90000:
            logging.debug("User eligible")
            return "Eligible"
        else:
            logging.debug("Salary is not eligible for this user")
            return "Salary is not eligible"

    # def fiveValid(self,days):
    #     if days>5:
    #         logging.debug("User eligible")
    #         return "Eligible"
    #     else:
    #         logging.debug("Last activity was held within 5 days,Not Eligible")
    #         return "Last request were must be greater than 5 days"



# fname=input("Enter First name ")
# mname=input("Enter middle name ")
# lname=input("Enter last name ")
# dob=input("Enter DOB YYYY-MM-DD ")
# dob=dt.datetime.strptime(dob,'%Y-%m-%d')
# dob=dob.date()
# gender=input("Enter gender ")
# nation=input("Enter Nationality ")
# city=input("Enter city ")
# state=input("Enter state ")
# pin=int(input("Enter pincode "))
# qual=input("Enter qualification ")
# salary=float(input("Enter salary "))
req_date=dt.datetime.now()
pan_num=input("Enter PAN ")

# mycursor.execute("INSERT INTO request_info(fname,mname,lname,dob,gender,nationality,"
#                  "city,state,pin,qualification,salary,req_date,pan) VALUES ('{}','{}',"
#                  "'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"
#                  .format(fname,mname,lname,dob,gender,nation,city,state,pin,qual,salary,req_date,pan_num))
#
# mydb.commit()

mycursor.execute("select req_date from request_info where id = (select max(id) "
                 "from request_info group by pan having pan='{}')".format(pan_num))

val=mycursor.fetchone()
# val1=str(val[0].date())
# req1=str(req_date.date())
#
# str1=re.split('-',val1)
# str2=re.split('-',req1)
#
# x=int(str1[0])
# y=int(str1[1])
# z=int(str1[2])
#
# x1=int(str2[0])
# y1=int(str2[1])
# z1=int(str2[2])
#
# d0=date(x,y,z)
# d1=date(x1,y1,z1)
# no_of_days=d1-d0
# print(no_of_days.days)

# v=Validation()
# flag=1
#
# age=v.calculateage(dob)
# st=""
# if flag==1:
#   str=v.ageValidate(age,gender)
#   if str!="Eligible":
#       flag=0
#       st=str
#
# if flag==1:
#   str1=v.nationValid(nation)
#   if str1!="Eligible":
#       flag=0
#       st=str1
#
# if flag==1:
#   str2=v.stateValid(state)
#   if str2!="Eligible":
#       flag=0
#       st=str2
#
# if flag == 1:
#   str3=v.salaryValid(salary)
#   if str3!="Eligible":
#       flag=0
#       st=str3

# if flag==1:
#     str4=v.fiveValid(no_of_days)
#     print(str4)
#     if str4!="Eligible":
#         flag=0
#         st=str4

mycursor.execute("select max(id) from request_info")
rid=mycursor.fetchone()
request_id=int(rid[0])

# if flag==1:
#     response="Success"
#     dict={"Request_id":request_id,"Response":response}
#     dictation=json.dumps(dict)
#     print(dictation)
#     mycursor.execute("INSERT INTO response_info(req_id,response) VALUES ('{}','{}')".format(request_id,dictation))
#     mydb.commit()
# else:
#     response="Failure"
#     dict = {"Request_id": request_id, "Response": response,"Reason":st}
#     dictation = json.dumps(dict)
#     print(dictation)
#     mycursor.execute("INSERT INTO response_info(req_id,response) VALUES ('{}','{}')".format(request_id, dictation))
#     mydb.commit()
