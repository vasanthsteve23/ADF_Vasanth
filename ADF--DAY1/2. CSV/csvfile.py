import csv
try:
    f=open("sample.csv","r")
    reader=csv.reader(f)

    people={}

    for row in reader:
        people[row[0]]={'age':row[1],'dept':row[2]}

    print(people)
except:
    print("Exception occurs")