""" User informations """
import datetime as dt
from datetime import date
import re
import json
import logging
import mysql.connector
import config as cfg

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

HOSTID = cfg.information["host"]
USERID = cfg.information["user"]
PSWD = cfg.information["password"]
DB=cfg.information["database"]

mydb=mysql.connector.connect(host=HOSTID,user=USERID,password=PSWD,database=DB)

mycursor=mydb.cursor()

class Validation:
    """This is validation class"""
    @classmethod
    def calculateage(cls,dob1):
        """Age calculation"""
        today=date.today()
        age1=today.year-dob1.year-((today.month,today.day)<(dob1.month,dob1.day))
        logging.debug("Calculation of age")
        return age1

    @classmethod
    def age_validate(cls,age1,gender1):
        """Age validation"""
        gender1=gender1.lower()
        rts=""
        if gender1=='male' and age1<21:
            rts = "age is less than 21"
        elif gender1=='female' and age1<18:
            rts = "age is less than 18"
        else:
            rts = "Eligible"
        logging.debug("Age valid completed")
        return rts

    @classmethod
    def nation_valid(cls,nation1):
        """Nation Validation"""
        nation1=nation1.lower()
        nat=['indian','american']
        rts1=""
        if nation1 in nat:
            rts1="Eligible"
        else:
            rts1="Not Eligible"
        logging.debug("Nation validation completed")
        return rts1

    @classmethod
    def state_valid(cls,state1):
        """State validation"""
        state1=state1.lower()
        state1=state1.replace(" ","")
        states=["andhra pradesh","arunachal pradesh","assam","bihar","chhatisgarh",
                "karnataka","madhyapradesh","odisha","tamilnadu","telangana","westbengal"]
        rts2=""
        if state1 in states:
            rts2="Eligible"
        else:
            rts2=state1+" State is not eligible"
        logging.debug("State validation completed")
        return rts2

    @classmethod
    def salary_valid(cls,salary1):
        """Salary validation"""
        rts3=""
        if 10000 <= salary1 <= 90000:
            rts3="Eligible"
        else:
            rts3="Salary is not eligible"
        logging.debug("Salary validation completed")
        return rts3

    @classmethod
    def pan_valid(cls,day):
        """Pan valid"""
        if day>5:
            cris="Eligible"
        else:
            cris="Request recieved in last 5 days from the same user"
        return  cris



fname=input("Enter First name ")
mname=input("Enter middle name ")
lname=input("Enter last name ")
dob=input("Enter DOB YYYY-MM-DD ")
dob=dt.datetime.strptime(dob,'%Y-%m-%d')
dob=dob.date()
gender=input("Enter gender ")
nation=input("Enter Nationality ")
city=input("Enter city ")
state=input("Enter state ")
pin=int(input("Enter pincode "))
qual=input("Enter qualification ")
salary=float(input("Enter salary "))
req_date=dt.datetime.now()
pan_num=input("Enter PAN ")

mycursor.execute("INSERT INTO request_info(fname,mname,lname,dob,gender,nationality,"
                 "city,state,pin,qualification,salary,req_date,pan) VALUES ('{}','{}',"
                 "'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"
                 .format(fname,mname,lname,dob,gender,nation,city,state,
                         pin,qual,salary,req_date,pan_num))
mydb.commit()
mycursor.execute("select req_date from request_info where id="
                 "(select max(id) from request_info group by pan having pan='{}')"
                 .format(pan_num))
value=mycursor.fetchone()
days_s1=0
REQ=str(req_date.date())
str2=re.split('-',REQ)
val4=int(str2[0])
val5=int(str2[1])
val6=int(str2[2])
d1=date(val4,val5,val6)
if value[0] is not None:
    VALUE1=str(value[0].date())
    str1=re.split('-',VALUE1)
    val1 = int(str1[0])
    val2 = int(str1[1])
    val3 = int(str1[2])
    d0=date(val1,val2,val3)
    days_s1=(d1-d0).days
    mycursor.execute("update request_info set req_date='{}' where pan='{}'".format(d1,pan_num))
else:
    mycursor.execute("update request_info set req_date='{}' where pan='{}'".format(d1, pan_num))

v=Validation()
FLAG=1

age=v.calculateage(dob)
ST=""
if FLAG==1:
    STRI=v.age_validate(age,gender)
    if STRI!="Eligible":
        FLAG=0
        ST=STRI

if FLAG==1:
    STR1=v.nation_valid(nation)
    if STR1!="Eligible":
        FLAG=0
        ST=STR1

if FLAG==1:
    STR2=v.state_valid(state)
    if STR2!="Eligible":
        FLAG=0
        ST=STR2

if FLAG == 1:
    STR3=v.salary_valid(salary)
    if STR3!="Eligible":
        FLAG=0
        ST=STR3

if FLAG==1:
    STR4=v.pan_valid(days_s1)
    print(STR4)
    if STR4!="Eligible":
        FLAG=0
        ST=STR4

mycursor.execute("select max(id) from request_info")
rid=mycursor.fetchone()
request_id=int(rid[0])

if FLAG==1:
    RESPONSE="Success"
    dicti={"Request_id":request_id,"Response":RESPONSE}
    dictation=json.dumps(dicti)
    print(dictation)
    mycursor.execute("INSERT INTO response_info(req_id,response) "
                     "VALUES ('{}','{}')".format(request_id,dictation))
    mydb.commit()
else:
    RESPONSE="Failure"
    dicti = {"Request_id": request_id, "Response": RESPONSE,"Reason":ST}
    dictation = json.dumps(dicti)
    print(dictation)
    mycursor.execute("INSERT INTO response_info(req_id,response) "
                     "VALUES ('{}','{}')".format(request_id, dictation))
    mydb.commit()
