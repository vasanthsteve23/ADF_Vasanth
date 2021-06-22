try:
    name=input("Enter name : ")
    age=input("Enter age : ")
    gender=input("Enter gender : ")
    salary=float(input("Enter salary : "))
    state=input("Enter state : ")
    city=input("Enter city : ")


    print("  USER  DETAILS  ")
    print("Name   : ",name)
    print("age    : ",age)
    print("gender : ",gender)
    print("salary : ",salary)
    print("state  : ",state)
    print("city   : ",city)
except:
    print("Exception found")