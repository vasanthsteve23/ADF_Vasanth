import re
try:
    vas=set({})

    file=open("vas.txt","r")

    for line in file:
        line=line.strip()
        string = re.sub("[^0-9a-zA-Z]"," ",line).split(" ")

        for s in string:
            p = len(s)
            if s!="":
              vas.add(str(p)+s)

    l=list(sorted(list(vas),key=len))

    with open('vasnew.txt', 'w') as f:
        for items in l:
            f.write('%s ' % items)
        print("File written successfully")
    f.close()
except:
    print("Exception found")